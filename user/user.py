from flask import Flask, render_template, request, jsonify, make_response
import json
import requests
from werkzeug.exceptions import NotFound

import grpc
import movie_pb2
import movie_pb2_grpc
import booking_pb2
import booking_pb2_grpc


app = Flask(__name__)

PORT = 3203
HOST = 'localhost'

with open('{}/databases/users.json'.format("."), "r") as jsf:
   users = json.load(jsf)["users"]

OTHER_URIS_GET_USERS={"List users":"/users"}
OTHER_URIS_GET_MOVIE_BOOKED_ERROR={"List users":"/users"}
OTHER_URIS_GET_MOVIE_BOOKED={"List users":"/users"}
STATUS_CODE_ERROR=400


# root message
@app.route("/", methods=['GET'])
def home():
    return make_response("<h1>Test</h1>",200)


# Get all bookings informations
@app.route("/users", methods=['GET'])
def showBookings():
    return make_response(jsonify(users,OTHER_URIS_GET_USERS),200)

# Which User gonna see that movie
@app.route("/user/<movieName>", methods=['GET'])
def showUsersIDByMovieBooked(movieName):
     with grpc.insecure_channel('localhost:3001') as channel:
        stub = movie_pb2_grpc.MovieStub(channel)
        movieTitle = movie_pb2.MovieTitle(title=movieName)
        movieByTheTitle = stub.GetMovieByTitle(movieTitle)

     with grpc.insecure_channel('localhost:3003') as channel:
        stub = booking_pb2_grpc.BookingStub(channel)
        empty = booking_pb2.EmptyMessage()
        listBookingsGRPC = stub.GetListBookings(empty)
        bookings=[]
        for book in listBookingsGRPC:
            bookings.append(book)

     jsonResponse=[] # Variable qui stocke la réponse JSON soit les noms de deux qui ont une réservation pour le film

     for book in bookings:
        for date in book.dates:
            for movieid in date.movies:
                if movieid == movieByTheTitle.id:
                    jsonResponse.append(book.userid)

     return make_response(jsonify(jsonResponse,OTHER_URIS_GET_MOVIE_BOOKED),200)

if __name__ == "__main__":
    print("Server running in port %s"%(PORT))
    app.run(host=HOST, port=PORT)

