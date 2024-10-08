# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import splade_pb2 as splade__pb2

GRPC_GENERATED_VERSION = '1.66.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in splade_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class EmbeddingServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetEmbedding = channel.unary_unary(
                '/splade.EmbeddingService/GetEmbedding',
                request_serializer=splade__pb2.TextRequest.SerializeToString,
                response_deserializer=splade__pb2.EmbeddingResponse.FromString,
                _registered_method=True)
        self.GetEmbeddingStrs = channel.unary_unary(
                '/splade.EmbeddingService/GetEmbeddingStrs',
                request_serializer=splade__pb2.TextRequest.SerializeToString,
                response_deserializer=splade__pb2.TokenEmbeddingResponse.FromString,
                _registered_method=True)


class EmbeddingServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetEmbedding(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetEmbeddingStrs(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EmbeddingServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetEmbedding': grpc.unary_unary_rpc_method_handler(
                    servicer.GetEmbedding,
                    request_deserializer=splade__pb2.TextRequest.FromString,
                    response_serializer=splade__pb2.EmbeddingResponse.SerializeToString,
            ),
            'GetEmbeddingStrs': grpc.unary_unary_rpc_method_handler(
                    servicer.GetEmbeddingStrs,
                    request_deserializer=splade__pb2.TextRequest.FromString,
                    response_serializer=splade__pb2.TokenEmbeddingResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'splade.EmbeddingService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('splade.EmbeddingService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class EmbeddingService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetEmbedding(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/splade.EmbeddingService/GetEmbedding',
            splade__pb2.TextRequest.SerializeToString,
            splade__pb2.EmbeddingResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetEmbeddingStrs(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/splade.EmbeddingService/GetEmbeddingStrs',
            splade__pb2.TextRequest.SerializeToString,
            splade__pb2.TokenEmbeddingResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
