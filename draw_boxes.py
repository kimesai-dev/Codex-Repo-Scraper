"""Draw bounding boxes returned by detect_button.py on an image."""
import os
import sys
from typing import Sequence

from PIL import Image, ImageDraw

import detect_button


COLOR = (255, 0, 0)
WIDTH = 2


def draw_bounding_boxes(image_path: str, detections: Sequence[dict], output_path: str) -> None:
    """Save a copy of the image with bounding boxes drawn."""
    img = Image.open(image_path).convert("RGB")
    draw = ImageDraw.Draw(img)
    for det in detections:
        box = det.get("xyxy")
        if box:
            draw.rectangle(box, outline=COLOR, width=WIDTH)
    img.save(output_path)


def main(argv: Sequence[str]) -> int:
    if len(argv) < 2:
        print("Usage: python3 draw_boxes.py <image_path> [weight_path] [output_path]", file=sys.stderr)
        return 1

    image_path = argv[1]
    weight_path = argv[2] if len(argv) > 2 else os.environ.get("YOLO_WEIGHTS", detect_button.DEFAULT_WEIGHTS)
    output_path = argv[3] if len(argv) > 3 else f"boxed_{os.path.basename(image_path)}"

    detections = detect_button.detect(image_path, weight_path)
    draw_bounding_boxes(image_path, detections, output_path)
    print(f"Saved boxed image to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
