import logging
import os
import sys
from spladerunner import Expander
import splade_pb2
import splade_pb2_grpc
import grpc
from concurrent import futures
from grpc_reflection.v1alpha import reflection
import grpc_health.v1.health_pb2_grpc as health_pb2_grpc
import grpc_health.v1.health_pb2 as health_pb2
from grpc_health.v1 import health
import threading

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Model and cache directory settings
MODEL_NAME = "Splade_PP_en_v1"
CACHE_DIR = "./splade_model"

# Check if the model exists locally
model_dir = os.path.join(CACHE_DIR, MODEL_NAME)
if not os.path.exists(model_dir):
    logging.error(f"Model directory '{model_dir}' not found. Please run 'download_model.py' to download the model.")
    sys.exit(1)

# Initialize SPLADERunner Expander
logging.info(f"Initializing SPLADERunner Expander with model '{MODEL_NAME}' from cache directory '{CACHE_DIR}'...")
expander = Expander(model_name=MODEL_NAME, cache_dir=CACHE_DIR)
logging.info("SPLADERunner Expander initialized successfully.")

class EmbeddingService(splade_pb2_grpc.EmbeddingServiceServicer):
    def GetEmbedding(self, request, context):
        logging.info("Received request for GetEmbedding")
        text = request.text
        logging.info(f"Input text: {text}")

        try:
            # Generate sparse embedding using SPLADERunner
            sparse_rep = expander.expand(text)
            logging.info("Sparse representation generated")

            # Extract indices and values from SPLADERunner response
            indices = sparse_rep[0]['indices']
            values = sparse_rep[0]['values']

            # Create embedding dictionary for response
            embedding = dict(zip(indices, values))

        except Exception as e:
            logging.error(f"An error occurred in GetEmbedding: {e}", exc_info=True)
            context.set_details(str(e))
            context.set_code(grpc.StatusCode.INTERNAL)
            return splade_pb2.EmbeddingResponse()

        # Create the response
        return splade_pb2.EmbeddingResponse(embedding=embedding)

    def GetEmbeddingStrs(self, request, context):
        logging.info("Received request for GetEmbeddingStrs")
        text = request.text
        logging.info(f"Input text: {text}")

        try:
            # Generate sparse embedding in lucene format using SPLADERunner
            sparse_rep = expander.expand(text, outformat="lucene")
            logging.info("Lucene sparse representation generated")

            # Extract the dictionary of tokens and values
            token_embedding = sparse_rep[0]  # Directly get the token-value mapping from the response

        except Exception as e:
            logging.error(f"An error occurred in GetEmbeddingStrs: {e}", exc_info=True)
            context.set_details(str(e))
            context.set_code(grpc.StatusCode.INTERNAL)
            return splade_pb2.TokenEmbeddingResponse()

        # Create the response
        return splade_pb2.TokenEmbeddingResponse(embedding=token_embedding)

class LoggingInterceptor(grpc.ServerInterceptor):
    def intercept_service(self, continuation, handler_call_details):
        logging.info(f"Intercepted call to: {handler_call_details.method}")
        return continuation(handler_call_details)

def serve():
    logging.info("Starting server setup...")
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10),
        interceptors=[LoggingInterceptor()],
        options=[
            ('grpc.max_send_message_length', 1024 * 1024 * 100),
            ('grpc.max_receive_message_length', 1024 * 1024 * 100),
        ]
    )

    # Add EmbeddingService to the server
    splade_pb2_grpc.add_EmbeddingServiceServicer_to_server(EmbeddingService(), server)

    # Add Health Checking Service to the server
    health_servicer = health.HealthServicer()
    health_pb2_grpc.add_HealthServicer_to_server(health_servicer, server)

    # Set the health status to SERVING
    health_servicer.set('', health_pb2.HealthCheckResponse.SERVING)

    # Enable reflection
    SERVICE_NAMES = (
        splade_pb2.DESCRIPTOR.services_by_name['EmbeddingService'].full_name,
        reflection.SERVICE_NAME,
        health.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)

    server.add_insecure_port('0.0.0.0:50051')
    logging.info("Server is running on port 50051 with reflection enabled...")

    try:
        server.start()
        server.wait_for_termination()
    except KeyboardInterrupt:
        logging.info("Shutting down the server gracefully...")
        server.stop(0)

if __name__ == '__main__':
    # Start the gRPC server
    serve()
