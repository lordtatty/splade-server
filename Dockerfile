# Stage 1: Build stage
FROM python:3.9-slim AS build

# Set environment variables to avoid Python buffering
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy Pipfile and Pipfile.lock to the container
COPY Pipfile Pipfile.lock ./

# Install pipenv
RUN pip install --no-cache-dir pipenv

# Generate requirements.txt and install dependencies
RUN pipenv requirements > requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install grpcio-tools and any requirements for downloading the model
RUN pip install grpcio-tools spladerunner

# Compile the proto file
COPY splade.proto .
RUN python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. splade.proto

# Copy the server code and download script to the container
COPY . .

# Run the model download script to pre-download the model
RUN python download_model.py

# Stage 2: Production stage
FROM python:3.9-slim

# Set environment variables to avoid Python buffering
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy Pipfile and Pipfile.lock to the container
COPY Pipfile Pipfile.lock ./

# Install pipenv
RUN pip install --no-cache-dir pipenv

# Generate requirements.txt and install dependencies
RUN pipenv requirements > requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install SPLADERunner for lightweight inference
RUN pip install spladerunner

# Copy the necessary files from the build stage, including the downloaded model
COPY --from=build /app /app

# Expose the port that the server listens on
EXPOSE 50051

# Run the server
CMD ["python", "server.py", "--model", "Splade_PP_en_v1"]
