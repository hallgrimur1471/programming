FROM ubuntu:18.04

WORKDIR /usr/local/install_python

RUN apt-get update && apt-get upgrade -y

# Copy everything from this Dockerfile's root-dir to WORKDIR
COPY . .

# Installs many Python versions
ENV DEBIAN_FRONTEND=noninteractive
RUN ./install_python_ubuntu_18.sh

# Tests if Python installed correctly
CMD ./tests/python_installation_tests/test_python_setup_linux.sh
