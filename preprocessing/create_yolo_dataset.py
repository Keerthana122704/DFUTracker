import os
import shutil
import random

IMAGE_DIR = "data/images"
LABEL_DIR = "data/yolo_labels"

OUTPUT_DIR = "data/yolo_detection"

random.seed(42)

images = [
    f for f in os.listdir(IMAGE_DIR)
    if f.lower().endswith(".png")
]

random.shuffle(images)

total = len(images)

train_end = int(total * 0.70)
val_end = int(total * 0.85)

train_files = images[:train_end]
val_files = images[train_end:val_end]
test_files = images[val_end:]

splits = {
    "train": train_files,
    "val": val_files,
    "test": test_files
}


for split, files in splits.items():

    image_output = os.path.join(
        OUTPUT_DIR,
        split,
        "images"
    )

    label_output = os.path.join(
        OUTPUT_DIR,
        split,
        "labels"
    )

    os.makedirs(image_output, exist_ok=True)
    os.makedirs(label_output, exist_ok=True)

    for filename in files:

        image_source = os.path.join(
            IMAGE_DIR,
            filename
        )

        label_name = os.path.splitext(filename)[0] + ".txt"

        label_source = os.path.join(
            LABEL_DIR,
            label_name
        )

        shutil.copy2(
            image_source,
            image_output
        )

        if os.path.exists(label_source):

            shutil.copy2(
                label_source,
                label_output
            )

print("Dataset split completed.")

print("Train:", len(train_files))
print("Validation:", len(val_files))
print("Test:", len(test_files))
