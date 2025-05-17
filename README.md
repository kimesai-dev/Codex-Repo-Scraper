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
