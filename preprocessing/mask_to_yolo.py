# this script converts the ulcer masks to YOLO format annotations.
# which are in locations/cordinates form 
# like 0 0.131696 0.223214 0.165179 0.232143

import cv2
import os

IMAGE_DIR = "data/images"
MASK_DIR = "data/labels"

OUTPUT_DIR = "data/yolo_labels"

os.makedirs(OUTPUT_DIR, exist_ok=True)


for filename in os.listdir(IMAGE_DIR):

    if not filename.lower().endswith(".png"):
        continue

    image_path = os.path.join(IMAGE_DIR, filename)

    mask_path = os.path.join(
        MASK_DIR,
        filename
    )

    if not os.path.exists(mask_path):
        print("Mask missing:", filename)
        continue

    mask = cv2.imread(
        mask_path,
        cv2.IMREAD_GRAYSCALE
    )

    if mask is None:
        print("Could not read:", mask_path)
        continue

    height, width = mask.shape

    # Convert mask to binary
    binary_mask = (mask > 0).astype("uint8") * 255

    # Find connected ulcer regions
    contours, _ = cv2.findContours(
        binary_mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    annotations = []

    for contour in contours:

        x, y, w, h = cv2.boundingRect(contour)

        # Ignore extremely tiny regions
        if w < 2 or h < 2:
            continue

        # Convert bounding box to YOLO format
        x_center = (x + w / 2) / width
        y_center = (y + h / 2) / height

        box_width = w / width
        box_height = h / height

        # Class 0 = ulcer
        annotations.append(
            f"0 {x_center:.6f} "
            f"{y_center:.6f} "
            f"{box_width:.6f} "
            f"{box_height:.6f}"
        )

    output_name = os.path.splitext(filename)[0] + ".txt"

    output_path = os.path.join(
        OUTPUT_DIR,
        output_name
    )

    with open(output_path, "w") as f:
        f.write("\n".join(annotations))

print("\nMask → YOLO conversion completed.")