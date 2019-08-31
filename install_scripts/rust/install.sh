#!/usr/bin/env bash

# Install cargo, rustc and rustup
curl https://sh.rustup.rs -sSf | sh

# Add formatting tool
rustup component add rustfmt

# Add linting tool
rustup component add clippy