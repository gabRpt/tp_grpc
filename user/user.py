from flask import Flask, render_template, request, jsonify, make_response
import json
import requests
from werkzeug.exceptions import NotFound

import grpc
import movie_pb2
import movie_pb2_grpc

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
def showUsersByMovieBooked(movieName):

#     jsonResponse=[] # Variable qui stocke la réponse JSON soit les noms de deux qui ont une réservation pour le film
#
#     # Récupération du movieID à partir du MovieName -> /moviesbytitle
#     uri = 'http://localhost:3201/moviesbytitle'
#     params={"title": movieName}
#     movie = requests.get(uri,params)
#
#     if movie.status_code == STATUS_CODE_ERROR:
#         return make_response(jsonify({"error":"Movie not found"},OTHER_URIS_GET_MOVIE_BOOKED_ERROR),400)
#
#     movieJSON = movie.content.decode('utf8').replace("'", '"')
#     movieID = json.loads(movieJSON)[0]["id"]
#
#     # Récupération des bookings -> /bookings
#     uri = 'http://localhost:3200/bookings'
#     bookings = requests.get(uri)
#
#     if bookings.status_code == STATUS_CODE_ERROR:
#         return make_response(jsonify({"error":"Problem"},OTHER_URIS_GET_MOVIE_BOOKED_ERROR),400)
#
#     bookingsJSON = bookings.content.decode('utf8').replace("'", '"')
#     bookings = json.loads(bookingsJSON)
#
#     # for each user
#         # si il va le voir alors on l'ajoute dans une liste
#     for object in bookings[0]:
#         for date in object['dates']:
#             for movie in date['movies']:
#                 if movieID == movie:
#                     jsonResponse.append(object['userid'])
#
#     return make_response(jsonify(jsonResponse,OTHER_URIS_GET_MOVIE_BOOKED),200)
      return make_response(jsonify(OTHER_URIS_GET_MOVIE_BOOKED),200)


if __name__ == "__main__":
    print("Server running in port %s"%(PORT))
    app.run(host=HOST, port=PORT)

