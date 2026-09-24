from ultralytics import YOLO

model = YOLO(
    "runs/detect/results/detection/dfu_yolov8/weights/best.pt"
)

results = model.predict(
    source="data/yolo_detection/test/images",
    imgsz=224,
    conf=0.25,
    save=True,
    project="results/detection",
    name="test_predictions"
)

print("Test prediction completed.")