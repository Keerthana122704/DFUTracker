from ultralytics import YOLO

model = YOLO(
    "runs/detect/results/detection/dfu_yolov8/weights/best.pt"
)

metrics = model.val(
    data="dfu_detection.yaml",
    imgsz=224,
    split="val"
)

print("\nValidation Results")
print("------------------")

print("Precision :", metrics.box.mp)
print("Recall    :", metrics.box.mr)
print("mAP50     :", metrics.box.map50)
print("mAP50-95  :", metrics.box.map)