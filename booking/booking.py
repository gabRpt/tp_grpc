import json
import grpc
from concurrent import futures
import booking_pb2
import booking_pb2_grpc

import showtime_pb2
import showtime_pb2_grpc

class BookingServicer(booking_pb2_grpc.BookingServicer):
    def __init__(self):
        with open('{}/databases/bookings.json'.format("."), "r") as jsf:
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
        with grpc.insecure_channel('localhost:3002') as channel:
            stub = showtime_pb2_grpc.ShowtimeStub(channel)
            date = showtime_pb2.Date(date = "20151130")
            print("--1--")
            dates = stub.GetMovieByDate(date)
            print("--2--")
            print(dates)
            return booking_pb2.AddBookingReturnMessage(message = "Yes")
            
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    booking_pb2_grpc.add_BookingServicer_to_server(BookingServicer(), server)
    server.add_insecure_port('[::]:3001')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()