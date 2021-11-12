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
BOOKING_URI = '[::]:3001'
BOOKING_DATABASE_PATH = '{}/databases/bookings.json'


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
                
        return booking_pb2.Book(
                    userid = "",
                    dates = ""
                )
        
    def AddBooking(self, request, context):
        # Création de la connexion et du stub
        with grpc.insecure_channel(CREATE_SHOWTIME_CHANNEL_URI) as channel:
            stubShowtime = showtime_pb2_grpc.ShowtimeStub(channel)
            
            # Récupération des films disponible à la date transmise
            date = showtime_pb2.Date(date = request.date)
            movies = stubShowtime.GetMovieByDate(date)
            
            # Variables            
            currentBookingDates = []
            movieIsScreened = False
            
            for movie in movies.movies:
                if movie == request.movie:
                    movieIsScreened = True
                    break

            if movieIsScreened:
                # Le film est projeté à la date transmise
                for book in self.db:
                    if book["userid"] == request.userid:
                        currentBookingDates = book["dates"]
                
                if currentBookingDates:
                    #L'utilisateur existe dans la BD
                                        
                    for bookDate in currentBookingDates:
                        if bookDate["date"] == request.date:
                            # L'utilisateur à déjà réservé un film à la date transmise
                            for movie in bookDate["movies"]:
                                if movie == request.movie:
                                    # L'utilisateur à déjà réservé le film à cette date
                                    return booking_pb2.AddBookingReturnMessage(message = ADD_BOOKING_ALREADY_ADDED_MESSAGE)

                            # Ajouter le film
                            print("Ajout du film")
                            bookDate["movies"].append(request.movie)
                            
                            return booking_pb2.AddBookingReturnMessage(message = ADD_BOOKING_SUCCESS_MESSAGE)
                    
                    # Create Date
                    print("create date")
                    info = {
                        "date" : request.date,
                        "movies": [request.movie]
                    }
                    currentBookingDates.append(info)
                    
                    return booking_pb2.AddBookingReturnMessage(message = ADD_BOOKING_SUCCESS_MESSAGE)
                    
                    
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

                    return booking_pb2.AddBookingReturnMessage(message = ADD_BOOKING_SUCCESS_MESSAGE)
                    
            else:
                #Le film n'est pas disponible à la date transmise
                return booking_pb2.AddBookingReturnMessage(message = ADD_BOOKING_MOVIE_NOT_SCREENED_MESSAGE)
            
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    booking_pb2_grpc.add_BookingServicer_to_server(BookingServicer(), server)
    server.add_insecure_port(BOOKING_URI)
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()