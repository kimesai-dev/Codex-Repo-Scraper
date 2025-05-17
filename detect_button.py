import json
import os
import sys

from ultralytics import YOLO

DEFAULT_WEIGHTS = "runs/detect/train5/weights/best.pt"


def detect(image_path: str, model_path: str):
    """Run YOLO detection on the image and return detection dicts."""
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file '{model_path}' not found")

    model = YOLO(model_path)
    results = model(image_path)

    detections = []
    for r in results:
        for b in r.boxes:
            detections.append({
                "class": int(b.cls.item()),
                "confidence": float(b.conf.item()),
                "xyxy": [float(x) for x in b.xyxy[0].tolist()],
            })
    return detections


def main(argv):
    if len(argv) < 2:
        print("Usage: python3 detect_button.py <image_path> [weight_path]", file=sys.stderr)
        return 1

    image_path = argv[1]
    weight_path = argv[2] if len(argv) > 2 else os.environ.get("YOLO_WEIGHTS", DEFAULT_WEIGHTS)

    if not os.path.exists(image_path):
        print(f"Error: image '{image_path}' not found", file=sys.stderr)
        return 1

    if not os.path.exists(weight_path):
        print(f"Error: model file '{weight_path}' not found", file=sys.stderr)
        return 1

    detections = detect(image_path, weight_path)
    print(json.dumps({"image": image_path, "detections": detections}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
