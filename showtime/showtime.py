import json
import grpc
from concurrent import futures
import showtime_pb2
import showtime_pb2_grpc

class ShowtimeServicer(showtime_pb2_grpc.ShowtimeServicer):
    def __init__(self):
        with open('{}/databases/times.json'.format("."), "r") as jsf:
            self.db = json.load(jsf)["schedule"]
    
    def GetMovieByDate(self, request, context):
        for schedule in self.db:
            if schedule['date'] == request.date:
                print("Date found!")
                return showtime_pb2.Movies(movies=schedule['movies'])
        return showtime_pb2.Movies(movies=None)
    
    def GetListTimes(self, request, context):
        for schedule in self.db:
            yield showtime_pb2.MoviesSchedules(
                date=schedule['date'],
                movies=schedule['movies']
            )
    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    showtime_pb2_grpc.add_ShowtimeServicer_to_server(ShowtimeServicer(), server)
    server.add_insecure_port('[::]:3002')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()