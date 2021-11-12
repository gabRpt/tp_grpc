# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import booking_pb2 as booking__pb2


class BookingStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetListBookings = channel.unary_stream(
                '/Booking/GetListBookings',
                request_serializer=booking__pb2.EmptyMessage.SerializeToString,
                response_deserializer=booking__pb2.Book.FromString,
                )
        self.GetListBookingsFromUser = channel.unary_stream(
                '/Booking/GetListBookingsFromUser',
                request_serializer=booking__pb2.UserId.SerializeToString,
                response_deserializer=booking__pb2.Book.FromString,
                )
        self.AddBooking = channel.unary_unary(
                '/Booking/AddBooking',
                request_serializer=booking__pb2.Reservation.SerializeToString,
                response_deserializer=booking__pb2.AddBookingReturnMessage.FromString,
                )


class BookingServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetListBookings(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetListBookingsFromUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddBooking(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BookingServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetListBookings': grpc.unary_stream_rpc_method_handler(
                    servicer.GetListBookings,
                    request_deserializer=booking__pb2.EmptyMessage.FromString,
                    response_serializer=booking__pb2.Book.SerializeToString,
            ),
            'GetListBookingsFromUser': grpc.unary_stream_rpc_method_handler(
                    servicer.GetListBookingsFromUser,
                    request_deserializer=booking__pb2.UserId.FromString,
                    response_serializer=booking__pb2.Book.SerializeToString,
            ),
            'AddBooking': grpc.unary_unary_rpc_method_handler(
                    servicer.AddBooking,
                    request_deserializer=booking__pb2.Reservation.FromString,
                    response_serializer=booking__pb2.AddBookingReturnMessage.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Booking', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Booking(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetListBookings(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/Booking/GetListBookings',
            booking__pb2.EmptyMessage.SerializeToString,
            booking__pb2.Book.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetListBookingsFromUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/Booking/GetListBookingsFromUser',
            booking__pb2.UserId.SerializeToString,
            booking__pb2.Book.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddBooking(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Booking/AddBooking',
            booking__pb2.Reservation.SerializeToString,
            booking__pb2.AddBookingReturnMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
