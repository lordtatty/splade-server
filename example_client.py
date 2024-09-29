import grpc
import splade_pb2
import splade_pb2_grpc

def run():
    channel = grpc.insecure_channel(
        'localhost:50051',
        options=[
            ('grpc.max_send_message_length', 1024 * 1024 * 100),
            ('grpc.max_receive_message_length', 1024 * 1024 * 100),
        ]
    )
    stub = splade_pb2_grpc.EmbeddingServiceStub(channel)
    request = splade_pb2.TextRequest(text="Test input")
    try:
        response = stub.GetEmbedding(request)
        print("Received embedding with length:", len(response.embedding))
    except grpc.RpcError as e:
        print(f"gRPC error: {e.code()} - {e.details()}")

if __name__ == '__main__':
    run()
