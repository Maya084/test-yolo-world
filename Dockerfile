# Build from CUDA docker image
FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

# Update default packages
RUN apt-get -qq update

# Install dependecies
RUN apt-get install -qq build-essential curl python3-venv git ffmpeg libsm6 libxext6  -y

# Allow statements and log messages to immediately appear in logs
ENV PYTHONUNBUFFERED True

# Create virtual environment within the container
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
# Add virtual environment's Python path (/opt/venv/bin) to the system's PATH,
# so pip does not complain about installing from root.
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Set and cd into the container's working directory
WORKDIR /yolo_world

COPY requirements.txt /yolo_world/requirements.txt

# Update pip and install dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# download ViT-B/32
RUN python -c "import clip; clip.load('ViT-B/32')"

# Add src files (Worker Template)
COPY . /yolo_world/

EXPOSE 8000

CMD ["python", "api/main.py"]



