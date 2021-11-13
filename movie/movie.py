import json
import grpc
from concurrent import futures
import movie_pb2
import movie_pb2_grpc

MOVIE_URI = '[::]:3001'
MOVIE_DATABASE_PATH = '{}/databases/movies.json'

class MovieServicer(movie_pb2_grpc.MovieServicer):

    def __init__(self):
        with open(MOVIE_DATABASE_PATH.format("."), "r") as jsf:
            self.db = json.load(jsf)["movies"]


    def GetMovieByID(self, request, context):
        for movie in self.db:
            if movie['id'] == request.id:
                print("Movie found!")
                return movie_pb2.MovieData(
                    title = movie['title'],
                    rating = movie['rating'],
                    director = movie['director'],
                    id = movie['id']
                )
                
        return movie_pb2.MovieData(title="", rating="", director="", id="")


    def GetListMovies(self, request, context):
        for movie in self.db:
            yield movie_pb2.MovieData(
                title = movie['title'],
                rating = movie['rating'],
                director = movie['director'],
                id = movie['id']
            )


    def CreateMovie(self, request, context):
        theMovieExist=False
        for movie in self.db:
            if movie["id"] == request.id:
                theMovieExist=True
                print("Movie Already exist !")
        if theMovieExist == False:
            jsonStr = {
                "title": request.title,
                "rating": request.rating,
                "director": request.director ,
                "id": request.id
            }
            self.db.append(jsonStr)
            print("Movie added !")
        return movie_pb2.Empty()


    def DeleteMovie(self, request, context):
        for movie in self.db:
            if movie["id"] == request.id:
                self.db.remove(movie)
                print("Movie deleted !")
                return movie_pb2.Empty()
        print("Movie not found !")
        return movie_pb2.Empty()


    def GetMovieByTitle(self, request, context):
        for movie in self.db:
            if movie["title"] == request.title:
                print("Movie Found !")
                return movie_pb2.MovieData(
                    title = movie['title'],
                    rating = movie['rating'],
                    director = movie['director'],
                    id = movie['id']
                )
                
        print("Movie not Found !")
        return movie_pb2.MovieData(title="", rating="", director="", id="")


    def UpdateMovieRating(self, request, context):
        for movie in self.db:
            if movie["id"] == request.id:
                movie["rating"] = int(request.rating)
                print("Updated !")
                return movie_pb2.Empty()
            
        print("Not Found !")
        return movie_pb2.Empty()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    movie_pb2_grpc.add_MovieServicer_to_server(MovieServicer(), server)
    server.add_insecure_port(MOVIE_URI)
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()