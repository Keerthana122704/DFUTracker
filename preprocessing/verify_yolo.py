import os

BASE_DIR = "data/yolo_detection"

for split in ["train", "val", "test"]:

    image_dir = os.path.join(
        BASE_DIR,
        split,
        "images"
    )

    label_dir = os.path.join(
        BASE_DIR,
        split,
        "labels"
    )

    images = [
        f for f in os.listdir(image_dir)
        if f.endswith(".png")
    ]

    labels = [
        f for f in os.listdir(label_dir)
        if f.endswith(".txt")
    ]

    print("\n", split.upper())
    print("Images:", len(images))
    print("Labels:", len(labels))

    missing = []

    for image in images:

        name = os.path.splitext(image)[0]

        if name + ".txt" not in labels:
            missing.append(image)

    print("Images without labels:", len(missing))