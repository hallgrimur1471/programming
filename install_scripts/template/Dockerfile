FROM ubuntu:18.04

WORKDIR /usr/local/workdir

# Update software
RUN apt-get update && apt-get upgrade -y

# Install some essentials
RUN apt-get install -y curl

# Install Python
RUN curl -o install_python.sh \
    https://raw.githubusercontent.com/hallgrimur1471/programming/master/install_scripts/python/ubuntu_18/install.sh && \
    sudo chmod +x install_python.sh && \
    ./install_python.sh

# Copy everything from this Dockerfile's root-dir to WORKDIR
COPY . .
