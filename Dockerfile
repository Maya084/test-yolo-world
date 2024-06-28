# Build from CUDA docker image
FROM ultralytics/ultralytics:8.1.35-python

WORKDIR /yoloworld

# install requirements
RUN pip install --upgrade pip && \
    pip install fastapi uvicorn python-multipart git+https://github.com/openai/CLIP.git

# copy the rest of the files
COPY . /yoloworld/

EXPOSE 8080

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8080"]