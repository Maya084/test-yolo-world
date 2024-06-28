# import requests
# from PIL import Image, ImageDraw
# from io import BytesIO
# import argparse
import time
import requests
from io import BytesIO
from PIL import Image, ImageDraw

image_url = ""
url = "https://yolo-world-ald5dh6gtq-uc.a.run.app/predict/"

# Download the image
response = requests.get(image_url)
image = Image.open(BytesIO(response.content))

# # Prepare data for the API request
# files = {"file": ("image.jpg", response.content, "image/jpeg")}
# data = {
#     "iou": args.iou,
#     "conf": args.conf
# }

payload = {'iou': '0.3'}
files=[
  ('file',('image.png',open('test_img.jpg','rb'),'image/jpg'))
]
headers = {}

start = time.perf_counter()
response = requests.request("POST", url, headers=headers, data=payload, files=files)
print("Request took: ", time.perf_counter() - start, " seconds.")

# print(response.text)
predictions = response.json()
print("Predictions: ", predictions)

# # Plot bounding boxes on the image
# draw = ImageDraw.Draw(image)
# for prediction in predictions:
#     confidence = prediction["confidence"]
#     coordinates = prediction["coordinates"]
#     class_name = prediction["class"]
#     x_min, y_min, x_max, y_max = (
#         coordinates["x_min"],
#         coordinates["y_min"],
#         coordinates["x_max"],
#         coordinates["y_max"],
#     )
#     draw.rectangle([x_min, y_min, x_max, y_max], outline="red")
#     draw.text((x_min, y_min), f"{class_name} ({confidence})", fill="red")

# # Save the image with bounding boxes
# image.save("result_image.jpg")





