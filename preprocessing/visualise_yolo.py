import cv2
import os

IMAGE_DIR = "data/yolo_detection/train/images"
LABEL_DIR = "data/yolo_detection/train/labels"

OUTPUT_DIR = "results/preprocessing"

os.makedirs(OUTPUT_DIR, exist_ok=True)

files = os.listdir(IMAGE_DIR)

count = 0

for filename in files:

    if not filename.endswith(".png"):
        continue

    image_path = os.path.join(
        IMAGE_DIR,
        filename
    )

    label_path = os.path.join(
        LABEL_DIR,
        os.path.splitext(filename)[0] + ".txt"
    )

    if not os.path.exists(label_path):
        continue

    image = cv2.imread(image_path)

    height, width = image.shape[:2]

    with open(label_path, "r") as f:

        for line in f:

            values = line.strip().split()

            if len(values) != 5:
                continue

            class_id, xc, yc, w, h = map(
                float,
                values
            )

            x1 = int((xc - w / 2) * width)
            y1 = int((yc - h / 2) * height)

            x2 = int((xc + w / 2) * width)
            y2 = int((yc + h / 2) * height)

            cv2.rectangle(
                image,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                2
            )

            cv2.putText(
                image,
                "ulcer",
                (x1, max(y1 - 5, 15)),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 255, 0),
                1
            )

    output_path = os.path.join(
        OUTPUT_DIR,
        filename
    )

    cv2.imwrite(output_path, image)

    count += 1

    if count >= 10:
        break

print("Saved", count, "visualizations.")