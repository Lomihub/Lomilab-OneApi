# NVIDIA Image Ubuntu 22.04
FROM nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu22.04

# Working directory
WORKDIR /app

# Update and install all dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    wget \
    curl \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python and Pip
RUN apt-get install -y python3 python3-pip && \
    ln -s /usr/bin/python3 /usr/bin/python && \
    ln -s /usr/bin/pip3 /usr/bin/pip

# Install libraries
RUN pip install --no-cache-dir \
    numpy \
    pandas \
    scikit-learn \
    matplotlib \
    seaborn \
    jupyterlab \
    notebook \
    opencv-python-headless \
    pillow \
    flask \
    fastapi \
    uvicorn \
    requests \
    torch==2.0.1+cu118 torchvision==0.15.2+cu118 torchaudio==2.0.2+cu118 -f https://download.pytorch.org/whl/torch_stable.html \
    tensorflow==2.13.0

# Update pip
RUN pip install --upgrade pip

# Copy all files to the container
COPY . .

# Expose port Flask/FastAPI
EXPOSE 8888

# Run API Default
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8888"]