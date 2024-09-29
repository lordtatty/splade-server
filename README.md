# SPLADE++ gRPC Server using SPLADERunner

This project provides a gRPC server implementation for generating sparse embeddings using **SPLADE++** via **SPLADERunner**. The gRPC server is designed for integration into information retrieval pipelines, supporting both embedding generation and token-based representations.

## Table of Contents

<table>
  <tr>
    <td>
      <ul>
        <li><a href="#overview">Overview</a></li>
        <li><a href="#features">Features</a></li>
        <li><a href="#spladerunner">SPLADERunner</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#usage">Usage</a>
          <ul>
            <li><a href="#running-the-server">Running the Server</a></li>
            <li><a href="#health-checks">Health Checks</a></li>
          </ul>
        </li>
        <li><a href="#docker">Docker</a>
          <ul>
            <li><a href="#building-and-running">Building and Running</a></li>
            <li><a href="#pulling-from-docker-hub">Pulling from Docker Hub</a></li>
          </ul>
        </li>
        <li><a href="#golang-client">Golang Client</a></li>
        <li><a href="#licenses">Licenses</a></li>
        <li><a href="#acknowledgements">Acknowledgements</a></li>
      </ul>
    </td>
    <td>
      <img src="https://github.com/user-attachments/assets/82866dff-079a-4a0d-b53c-54779361e3dc" alt="image" width="300"/>
    </td>
  </tr>
</table>

## Overview

This repository contains a gRPC server that utilizes **SPLADERunner** to generate sparse representations for input texts using the **SPLADE++** model. The SPLADE++ model provides advanced sparse representation techniques that enhance lexical matching and retrieval efficiency.

This server is built using:

- **gRPC** for efficient communication.
- **Python** for scripting and deployment.
- **SPLADERunner**, a lightweight and efficient wrapper for handling SPLADE++ models without requiring heavy dependencies like PyTorch.

The server exposes two main gRPC endpoints:

- `GetEmbedding`: Generates a sparse representation in index-value pairs.
- `GetEmbeddingStrs`: Generates a sparse representation in token-value pairs, making it easy to use in human-readable form.

## Features

- **Sparse Embedding Generation**: Supports generation of sparse vector representations.
- **Lightweight Deployment**: Uses SPLADERunner to run efficiently on CPU without heavy frameworks like PyTorch.
- **gRPC Health Checks**: Implements gRPC-based health checks suitable for Kubernetes deployments.

## SPLADERunner

[**SPLADERunner**](https://github.com/PrithivirajDamodaran/SPLADERunner) is an ultra-light and fast wrapper for SPLADE++ models. It is designed to provide efficient query and passage expansion without requiring heavyweight frameworks like PyTorch.

SPLADERunner supports the following key features:

- **Lightweight**: No need for large frameworks; runs efficiently on CPUs.
- **FLOPS & Retrieval Efficiency**: Optimized for fast inference with limited hardware requirements.

### License for SPLADERunner and SPLADE++

- **SPLADE++** model is licensed under **Apache License 2.0**, allowing for commercial use and modifications.
- **SPLADERunner** itself follows the **Apache License 2.0**, providing flexibility to integrate it into commercial projects.

## Installation

1. **Clone the Repository**:

   ```sh
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**:

   - Make sure you have Python 3.9 installed.
   - Install the dependencies using `pipenv`:

   ```sh
   pipenv install
   ```

3. **Download the Model**:
   - Run the provided script to download the SPLADE++ model before starting the server:
   ```sh
   python download_model.py
   ```

## Usage

### Running the Server

1. **Run the gRPC Server**:

   ```sh
   python server.py
   ```

   The server will start listening on `0.0.0.0:50051`.

2. **gRPC Health Checks**:

   - Health checks can be accessed via gRPC to determine the liveness and readiness of the service.
   - Use a tool like `grpcurl` to check the health status:
     ```sh
     grpcurl -plaintext localhost:50051 grpc.health.v1.Health/Check
     ```

   The response should indicate the health status (`SERVING` if the server is running correctly).

### Health Checks

This server uses gRPC-based health checks, which makes it suitable for Kubernetes deployments:

- **Liveness Probe**: Checks if the server process is running.
- **Readiness Probe**: Checks if the model is loaded and the server is ready to handle requests.

## Docker

### Building and Running

The project includes a Dockerfile for containerization. To build and run the container:

1. **Build the Docker Image**:

   ```sh
   docker build -t splade-server .
   ```

2. **Run the Docker Container**:
   ```sh
   docker run -p 50051:50051 splade-server
   ```

The Docker image includes the pre-downloaded SPLADE++ model to reduce startup time and avoid model downloads at runtime.

### Pulling from Docker Hub

You can pull the Docker image directly from Docker Hub using the following command:

```sh
docker pull lordtatty/splade-grpc-server:latest
```

This allows you to run the server without needing to build the image manually.

## Golang Client

A Golang package is available that provides a simple client to interact with this server. This package can be used to send requests to the gRPC server and receive sparse embeddings in return.

You can find the Golang client here: [lordtatty/splade-server-goclient](https://github.com/lordtatty/splade-server-goclient).

To use it in your Go project, import the package and use it to communicate with the SPLADE++ gRPC server. It offers a straightforward way to integrate the sparse embedding capabilities into your Go-based applications.

## Licenses

### SPLADE++

- The **SPLADE++** model is released under the **Apache License 2.0**. This license allows for commercial use, modification, and distribution.

### SPLADERunner

- **SPLADERunner** is also licensed under the **Apache License 2.0**, making it permissible for both personal and commercial projects.

### Project Code

- The code in this repository follows the **Apache License 2.0** unless otherwise specified. This allows you to modify, distribute, and use the code in both open-source and commercial applications.

## Acknowledgements

- **SPLADE++**: The SPLADE++ model used in this project is based on research by Naver and Google on making sparse neural information retrieval more effective.
- **SPLADERunner**: Thanks to the developers of SPLADERunner for providing a lightweight and efficient way to use SPLADE++ in production environments.

For more information about the SPLADE++ model, see the [SPLADE++ model page on Hugging Face](https://huggingface.co/prithivida/Splade_PP_en_v1).
