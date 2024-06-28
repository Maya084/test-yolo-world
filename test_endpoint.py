import time
import requests
from PIL import Image, ImageDraw

url = "/predict"

payload = {"iou": "0.3", "conf": 0.3, "classes": "dress,person"}
files = [("file", ("test_img.jpg", open("test_img.jpg", "rb"), "application/octet"))]
image = Image.open("test_img.jpg")
headers = {}

start = time.perf_counter()
response = requests.request("POST", url, headers=headers, data=payload, files=files)
print("\nRequest took: ", time.perf_counter() - start, " seconds.\n")
predictions = response.json()
print("Predictions: ", predictions, "\n")

# Plot bounding boxes on the image
draw = ImageDraw.Draw(image)
for prediction in predictions:
    confidence = prediction["confidence"]
    coordinates = prediction["coordinates"]
    class_name = prediction["class"]
    x_min, y_min, x_max, y_max = (
        coordinates["x_min"],
        coordinates["y_min"],
        coordinates["x_max"],
        coordinates["y_max"],
    )

    draw.rectangle([x_min, y_min, x_max, y_max], outline="red")
    draw.text((x_min, y_min), f"{class_name} ({confidence})", fill="red")

# Save the image with bounding boxes
image.save("result_image.jpg")
