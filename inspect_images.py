from PIL import Image
import os

folder = "data/images"

files = [
    f for f in os.listdir(folder)
    if f.lower().endswith(".png")
]

print("Total images:", len(files))
print()

for filename in files[:10]:
    path = os.path.join(folder, filename)

    try:
        image = Image.open(path)

        print(
            filename,
            "->",
            image.size,
            "->",
            image.mode
        )

    except Exception as e:
        print(filename, "ERROR:", e)