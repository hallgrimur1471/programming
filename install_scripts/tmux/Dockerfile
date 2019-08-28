FROM ubuntu:18.04

WORKDIR /usr/local/workdir

# Update software
RUN apt-get update && apt-get upgrade -y

# Install some essentials
RUN apt-get install -y \
    curl \
    sudo

# Install python
RUN curl -o install_python.sh \
    https://raw.githubusercontent.com/hallgrimur1471/programming/master/install_scripts/python/ubuntu_18/install.sh && \
    chmod +x install_python.sh && \
    ./install_python.sh

# Install pytest
RUN python3.7 -m pip install --user pytest

# Copy install script & configs
COPY install.py .
COPY configs configs

# Install tmux
RUN ./install.py

# Also copy the tests now
COPY . .

# Validate install
CMD ./tests/validate_install.py
