# Codex Repo Scraper

This repository contains resources for detecting message buttons with a YOLO model.

## Detecting buttons

Use `detect_button.py` to run the detector on a single image. The script
requires the image path and accepts an optional path to the model weights
as a second command‑line argument. If no weight path is provided, the script
uses the value of the `YOLO_WEIGHTS` environment variable or defaults to
`runs/detect/train5/weights/best.pt`.

```bash
python3 detect_button.py <image_path> [weight_path]
```

### Example

To run detection on one of the test images:

```bash
python3 detect_button.py model/test_images/<file>.png /path/to/best.pt
```

Replace `<file>` with the specific image name and `/path/to/best.pt` with the
path to your trained model weights.

The output is printed as JSON in the following format:

```json
{
  "image": "<image_path>",
  "detections": [
    {
      "class": 0,
      "confidence": 0.99,
      "xyxy": [x1, y1, x2, y2]
    }
  ]
}
```

Each detection entry contains the class index, confidence score and bounding
box coordinates in the `[x1, y1, x2, y2]` format.
