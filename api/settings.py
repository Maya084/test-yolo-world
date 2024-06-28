from .utils import load_env


MODEL_PATH = load_env("MODEL_PATH") or "model/custom_yoloworld.pt"
MODEL_THRESHOLD = load_env("MODEL_THRESHOLD") or 0.1
IOU_THRESHOLD = load_env("IOU_THRESHOLD") or 0.5
