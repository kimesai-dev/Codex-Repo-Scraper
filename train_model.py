"""Train a custom YOLOv8 model on the Message Again button dataset."""
from ultralytics import YOLO


DATA_FILE = "model/data.yaml"
DEFAULT_MODEL = "yolov8n.yaml"


def main():
    """Train the model using the dataset configuration."""
    model = YOLO(DEFAULT_MODEL)
    model.train(
        data=DATA_FILE,
        epochs=100,
        imgsz=640,
        patience=10,
        project="runs/detect",
        name="train",
        exist_ok=True,
    )


if __name__ == "__main__":
    main()
