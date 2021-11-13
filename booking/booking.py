import json
import grpc
from concurrent import futures
import booking_pb2
import booking_pb2_grpc

import showtime_pb2
import showtime_pb2_grpc

ADD_BOOKING_SUCCESS_MESSAGE = "Movie successfully added"
ADD_BOOKING_ALREADY_ADDED_MESSAGE = "Movie already added"
ADD_BOOKING_MOVIE_NOT_SCREENED_MESSAGE = "Movie not available on the specified date"

CREATE_SHOWTIME_CHANNEL_URI = 'localhost:3002'
BOOKING_URI = '[::]:3003'
BOOKING_DATABASE_PATH = '{}/databases/bookings.json'

STATUS_CODE_SUCCESS = 200
STATUS_CODE_ERROR = 400


class BookingServicer(booking_pb2_grpc.BookingServicer):
    def __init__(self):
        with open(BOOKING_DATABASE_PATH.format("."), "r") as jsf:
            self.db = json.load(jsf)["bookings"]

    def GetListBookings(self, request, context):
        for book in self.db:
            yield booking_pb2.Book(
                userid = book["userid"],
                dates = book["dates"]
            )
            
    def GetListBookingsFromUser(self, request, context):
        for book in self.db:
            if book["userid"] == request.userid:
                yield booking_pb2.Book(
                    userid = book["userid"],
                    dates = book["dates"]
                )
        
        #Empty if nothing found
        return booking_pb2.Book(
                    userid = "",
                    dates = ""
                )
        
    def AddBooking(self, request, context):
        # Creating the connection and stub
        with grpc.insecure_channel(CREATE_SHOWTIME_CHANNEL_URI) as channel:
            stubShowtime = showtime_pb2_grpc.ShowtimeStub(channel)
            
            # Recovery of films available on the date transmitted
            date = showtime_pb2.Date(date = request.date)
            movies = stubShowtime.GetMovieByDate(date)
                       
            currentBookingDates = []
            movieIsScreened = False
            
            # To add a movie to the database, we need to check the following:
            # 1. If the movie is screened on the date transmitted
            # 2. If the user has already reserved the movie on the date transmitted
            # 3. If the user exists in booking's database, 
            #       if yes, we need to check if he has reserved any other movie at the date transmitted
            #           if yes we add the movie to the database at the specified date
            #           if not we create the date and add the movie
            #       if not we need to create the user and add the movie w/ the date
            
            for movie in movies.movies:
                if movie == request.movie:
                    movieIsScreened = True
                    break
                
            if movieIsScreened:
                # The film is screened on the date transmitted
                for book in self.db:
                    if book["userid"] == request.userid:
                        currentBookingDates = book["dates"]
                
                if currentBookingDates:
                    #The user exists in the database
                                        
                    for bookDate in currentBookingDates:
                        if bookDate["date"] == request.date:
                            # The user has already reserved a film on the date transmitted
                            for movie in bookDate["movies"]:
                                if movie == request.movie:
                                    # The user has already booked the film on this date
                                    return booking_pb2.AddBookingReturnMessage(
                                            code = STATUS_CODE_ERROR,
                                            message = ADD_BOOKING_ALREADY_ADDED_MESSAGE
                                        )

                            # Add movie
                            print("Add movie")
                            bookDate["movies"].append(request.movie)
                            
                            return booking_pb2.AddBookingReturnMessage(
                                    code = STATUS_CODE_SUCCESS,
                                    message = ADD_BOOKING_SUCCESS_MESSAGE
                                )
                    
                    # Create Date
                    print("create date")
                    info = {
                        "date" : request.date,
                        "movies": [request.movie]
                    }
                    currentBookingDates.append(info)
                    
                    return booking_pb2.AddBookingReturnMessage(
                            code = STATUS_CODE_SUCCESS,
                            message = ADD_BOOKING_SUCCESS_MESSAGE
                        )
                    
                    
                else:
                    #Create user
                    print("create user")                    
                    info = {
                        "userid": request.userid,
                        "dates": [
                            {
                                "date" : request.date,
                                "movies": [request.movie]
                            }
                        ]
                    }
                    self.db.append(info)

                    return booking_pb2.AddBookingReturnMessage(
                            code = STATUS_CODE_SUCCESS,
                            message = ADD_BOOKING_SUCCESS_MESSAGE
                        )
                    
            else:
                #The film is not available on the transmitted date
                return booking_pb2.AddBookingReturnMessage(
                        code = STATUS_CODE_ERROR,
                        message = ADD_BOOKING_MOVIE_NOT_SCREENED_MESSAGE
                    )
            
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    booking_pb2_grpc.add_BookingServicer_to_server(BookingServicer(), server)
    server.add_insecure_port(BOOKING_URI)
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()