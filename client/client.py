import grpc
# import movie_pb2
# import movie_pb2_grpc

import showtime_pb2
import showtime_pb2_grpc

import booking_pb2
import booking_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:3002') as channel:
        
        # ======================= MOVIE =====================
        # stub = movie_pb2_grpc.MovieStub(channel)

        # print("-------------- GetMovieByID --------------")
        # movieid = movie_pb2.MovieID(id = "a8034f44-aee4-44cf-b32c-74cf452aaaae")
        # get_movie_by_id(stub, movieid)
        
        
        
        #======================= SHOWTIME =====================
        stub = showtime_pb2_grpc.ShowtimeStub(channel)

        print("-------------- GetMovieFromShowtimeByDate --------------")
        date = showtime_pb2.Date(date = "20151130")
        get_movie_by_date_from_showtime(stub, date)
        
        
        print("-------------- GetMovieFromShowtimeByDate --------------")
        empty = showtime_pb2.Empty()
        get_list_movies_schedule(stub, empty)
        
        
        
        # ======================= BOOKINGS =====================
        #stub = booking_pb2_grpc.BookingStub(channel)
        
        # print("-------------- GetListBookings --------------")
        # empty = booking_pb2.EmptyMessage()
        # get_list_bookings(stub,empty)

        # print("-------------- GetListBookingsFromUser --------------")
        #userid = booking_pb2.UserId(userid = "dwight_schrute")
#         get_list_bookings_from_user(stub,userid)
#         print("=====================================================")
#         empty = booking_pb2.EmptyMessage()
#         val = stub.AddBooking(empty)
  
def get_movie_by_id(stub,id):
    movie = stub.GetMovieByID(id)
    print(movie)

# Showtime
def get_movie_by_date_from_showtime(stub,date):
    dates = stub.GetMovieByDate(date)
    print(dates)

def get_list_movies_schedule(stub,empty):
    schedules = stub.GetListTimes(empty)
    for schedule in schedules:
        print("--------------------------------")
        print("Date ", schedule.date)
        for movie in schedule.movies:
            print("    - ", movie)
            
        print("--------------------------------")

#Booking
def get_list_bookings(stub,empty):
    books = stub.GetListBookings(empty)
    for book in books:
        print("--------------------------------")
        print("UserId ", book.userid)
        for date in book.dates:
            print("    - ", date.date)
            for movie in date.movies:
                print("        - ", movie)
        print("--------------------------------")

def get_list_bookings_from_user(stub,userid):
    books = stub.GetListBookingsFromUser(userid)
    for book in books:
        print("--------------------------------")
        print("UserId ", book.userid)
        for date in book.dates:
            print("    - ", date.date)
            for movie in date.movies:
                print("        - ", movie)
        print("--------------------------------")


if __name__ == '__main__':
    run()