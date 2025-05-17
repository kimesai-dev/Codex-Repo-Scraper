diff --git a//dev/null b/README.md
index 0000000..d11a7a2 100644
--- a//dev/null
+++ b/README.md
@@ -0,0 +1,96 @@
+# Codex Repo Scraper
+
+This repository contains resources for detecting message buttons with a YOLO model.
+
+## Detecting buttons
+
+Use `detect_button.py` to run the detector on a single image. The script
+requires the image path and accepts an optional path to the model weights
+as a second command‑line argument. If no weight path is provided, the script
+uses the value of the `YOLO_WEIGHTS` environment variable or defaults to
`runs/detect/train/weights/best.pt`.
+
+```bash
+python3 detect_button.py <image_path> [weight_path]
+```
+
+### Example
+
+To run detection on one of the test images:
+
+```bash
+python3 detect_button.py model/test_images/<file>.png /path/to/best.pt
+```
+
+Replace `<file>` with the specific image name and `/path/to/best.pt` with the
+path to your trained model weights.
+
+The output is printed as JSON in the following format:
+
+```json
+{
+  "image": "<image_path>",
+  "detections": [
+    {
+      "class": 0,
+      "confidence": 0.99,
+      "xyxy": [x1, y1, x2, y2]
+    }
+  ]
+}
+```
+
+Each detection entry contains the class index, confidence score and bounding
+box coordinates in the `[x1, y1, x2, y2]` format.
+
+## Building a custom model
+
+1. **Label screenshots**
+   - Collect 20–30 Messenger screenshots that show the *Message Again* button.
+   - Use a tool such as **labelImg** or the browser-based **Roboflow** annotator
+     to draw a bounding box around the button in each image.
+   - Export the labels in YOLO format with a single class named `message_button`.
+
+2. **Create the dataset directory structure**
+
+   Place your images and corresponding `.txt` label files under `model/train` in
+   the following layout:
+
+   ```
+   model/train/images/  # JPEG or PNG files
+   model/train/labels/  # matching .txt files in YOLO format
+   model/data.yaml      # dataset config
+   ```
+
+   The provided `model/data.yaml` already defines the dataset with one class and
+   expects the `train/images` folder for both training and validation.
+
+3. **Train YOLOv8 locally**

   Install the Ultralytics package in your Python environment:

   ```bash
   pip install ultralytics
   ```

   Run the provided helper script to start training. It uses the lightweight
   `yolov8n.yaml` model for 100 epochs with early stopping enabled:

   ```bash
   python3 train_model.py
   ```

   Training outputs the best weights to `runs/detect/train/weights/best.pt`.
+
+4. **Run detection with the trained model**
+
+   Call `detect_button.py` with the path to the `best.pt` file or place the file
+   at the default location (`runs/detect/train/weights/best.pt`). The script
+   will print detection results in the JSON format shown above.

5. **(Optional) Visualize detections**

   Use `draw_boxes.py` to save a copy of the image with bounding boxes drawn:

   ```bash
   python3 draw_boxes.py <image_path> [weight_path] [output_path]
   ```
