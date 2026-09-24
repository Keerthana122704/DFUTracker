from ultralytics import YOLO

# Load pretrained YOLOv8 Nano model
model = YOLO("yolov8n.pt")

# Train
results = model.train(
    data="dfu_detection.yaml",
    epochs=50,
    imgsz=224,
    batch=8,
    project="results/detection",
    name="dfu_yolov8",
    patience=10,
    workers=0
)

print("Training completed.")