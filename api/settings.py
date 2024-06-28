from utils import load_env


MODEL_PATH = load_env("MODEL_PATH") or "model/yolov8s-worldv2-custom.pt"
MODEL_THRESHOLD = load_env("MODEL_THRESHOLD") or 0.25
IOU_THRESHOLD = load_env("IOU_THRESHOLD") or 0.5
