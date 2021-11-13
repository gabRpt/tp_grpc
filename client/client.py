import grpc
import movie_pb2
import movie_pb2_grpc

import showtime_pb2
import showtime_pb2_grpc

import booking_pb2
import booking_pb2_grpc

MOVIE_URI = 'localhost:3001'
SHOWTIME_URI = 'localhost:3002'
BOOKING_URI = 'localhost:3003'

def run():
    with grpc.insecure_channel(MOVIE_URI) as channel:
        
        # ======================= MOVIE =====================
        # stub = movie_pb2_grpc.MovieStub(channel)

        # print("-------------- GetMovieByID --------------")
        # movieid = movie_pb2.MovieID(id = "a8034f44-aee4-44cf-b32c-74cf452aaaae")
        # get_movie_by_id(stub, movieid)

        # print("-------------- GetListMovies --------------")
        # get_list_movies(stub)

        # print("-------------- CreateMovie --------------")
        # print("--- Create the movie ----")
        # myMovie = movie_pb2.MovieData(title = "Avatar", rating = 10.0, director = "James Cameron", id = "qdzqzdqd-aee4-44cf-b32c-74cf452aaaad")
        # create_movie(stub,myMovie)
        # print("--- Test if the movie is added ----")
        # get_list_movies(stub)

        # print("-------------- DeleteMovie --------------")
        # print("--- Delete the movie ----")
        # movieid = movie_pb2.MovieID(id = "qdzqzdqd-aee4-44cf-b32c-74cf452aaaad")
        # delete_movie(stub,movieid)
        # print("--- Test if the movie is deleted ----")
        # get_list_movies(stub)

        # print("-------------- GetMovieByTitle --------------")
        # movieTitle = movie_pb2.MovieTitle(title = "Creed")
        # get_movie_by_title(stub,movieTitle)

        # print("-------------- UpdateMovieRating --------------")
        # myMovie = movie_pb2.MovieData(title = "The Good Dinosaur", rating = 10.0, director = "Peter Sohn", id = "720d006c-3a57-4b6a-b18f-9b713b073f3c")
        # update_movie_rating(stub,myMovie)
        # print("--- Test if the movie is updated ----")
        # movieid = movie_pb2.MovieID(id = "720d006c-3a57-4b6a-b18f-9b713b073f3c")
        # get_movie_by_id(stub,movieid)

        
        #======================= SHOWTIME =====================
        # stub = showtime_pb2_grpc.ShowtimeStub(channel)

        # print("=============== BEGIN ===============")
        # print("-------------- GetMovieByDate --------------")
        # date = showtime_pb2.Date(date = "20151130")
        # get_movie_by_date_from_showtime(stub, date)


        # print("-------------- GetListTimes --------------")
        # empty = showtime_pb2.EmptyMsg()
        # get_list_movies_schedule(stub, empty)
        # print("=============== END ===============")
        
        # ======================= BOOKINGS =====================
        # stub = booking_pb2_grpc.BookingStub(channel)
        
        # print("=============== BEGIN ===============")
        # print("--------------- GetListBookingsFromUser ---------------")
        # userid = booking_pb2.UserId(userid = "chris_rivers")
        # get_list_bookings_from_user(stub,userid)
        
        # print("--------------- AddBooking ---------------")
        # reservation = booking_pb2.Reservation(
        #     userid = "chris_rivers",
        #     movie = "7daf7208-be4d-4944-a3ae-c1c2f516f3e6",
        #     date = "20151204"
        # )
        # print(stub.AddBooking(reservation))
        
        # print("--------------- GetListBookings ---------------")
        # empty = booking_pb2.EmptyMessage()
        # get_list_bookings(stub,empty)
        # print("=============== END ===============")
  

#============================= Movie =============================
def get_movie_by_id(stub,id):
    movie = stub.GetMovieByID(id)
    print(movie)

def get_list_movies(stub):
    allmovies = stub.GetListMovies(movie_pb2.Empty())
    for movie in allmovies:
        print("Movie called %s" % (movie.title))

def create_movie(stub,movieData):
    empty = stub.CreateMovie(movieData)

def delete_movie(stub,id):
    empty = stub.DeleteMovie(id)

def get_movie_by_title(stub,title):
    movie = stub.GetMovieByTitle(title)
    print(movie)

def update_movie_rating(stub,movieData):
    empty = stub.UpdateMovieRating(movieData)

#============================= Showtime =============================
def get_movie_by_date_from_showtime(stub,date):
    dates = stub.GetMovieByDate(date)
    print(dates)

def get_list_movies_schedule(stub,empty):
    schedules = stub.GetListTimes(empty)
    for schedule in schedules:
        print("Date ", schedule.date)
        for movie in schedule.movies:
            print("    - ", movie)
            

#============================= Booking =============================
def get_list_bookings(stub,empty):
    books = stub.GetListBookings(empty)
    for book in books:
        print("UserId ", book.userid)
        for date in book.dates:
            print("    - ", date.date)
            for movie in date.movies:
                print("        - ", movie)

def get_list_bookings_from_user(stub,userid):
    books = stub.GetListBookingsFromUser(userid)
    for book in books:
        print("UserId ", book.userid)
        for date in book.dates:
            print("    - ", date.date)
            for movie in date.movies:
                print("        - ", movie)


if __name__ == '__main__':
    run()