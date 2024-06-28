from fastapi import FastAPI, File, UploadFile
from ultralytics import YOLOWorld
from typing import List
from PIL import Image
from typing import List
import io
from settings import MODEL_PATH, MODEL_THRESHOLD, IOU_THRESHOLD

app = FastAPI()

model = YOLOWorld(MODEL_PATH)
DEFAULT_CLASSES = model.names


@app.post("/predict/")
async def predict(
    classes: List[str] = [],
    file: UploadFile = File(...),
    iou: float = IOU_THRESHOLD,
    conf: float = MODEL_THRESHOLD,
):
    image = Image.open(io.BytesIO(await file.read()))

    if len(classes) == 1:
        # Split the single string into a list of strings and strip each item
        classes = [item.strip() for item in classes[0].split(",") if item.strip()]

    # Check if classes is not empty after processing
    if classes:
        model.set_classes(tuple(classes))
    else:
        classes = DEFAULT_CLASSES

    try:
        # Execute inference with the YOLOv8s-world model on the uploaded image
        results = model.predict(image, conf=conf, iou=iou)
        # Convert the prediction results to a list of dictionaries
        predictions = []
        for res in results[0].boxes:
            obj = {
                "confidence": round(float(res.conf[0]), 2),
                "coordinates": {
                    "x_min": round(float(res.xyxy[0][0]), 2),
                    "y_min": round(float(res.xyxy[0][1]), 2),
                    "x_max": round(float(res.xyxy[0][2]), 2),
                    "y_max": round(float(res.xyxy[0][3]), 2),
                },
                "class": classes[int(res.cls[0])],
            }
            predictions.append(obj)
        return predictions
    finally:
        image.close()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=7000)
