#this is used for checking the imagesing are having their 
# corresponding annotation masks or not in labels folder.
# if it is fine start with yolo detection in preprocessing folder


import os

IMAGE_DIR = "data/images"
LABEL_DIR = "data/labels"

image_files = {
    os.path.splitext(f)[0]
    for f in os.listdir(IMAGE_DIR)
    if f.lower().endswith(".png")
}

label_files = {
    os.path.splitext(f)[0]
    for f in os.listdir(LABEL_DIR)
    if f.lower().endswith(".png")
}

print("Number of images:", len(image_files))
print("Number of masks :", len(label_files))

images_without_masks = image_files - label_files
masks_without_images = label_files - image_files

print("\nImages without masks:", len(images_without_masks))
print("Masks without images:", len(masks_without_images))

if images_without_masks:
    print("\nExamples of images without masks:")
    for name in list(images_without_masks)[:10]:
        print(name)

if masks_without_images:
    print("\nExamples of masks without images:")
    for name in list(masks_without_images)[:10]:
        print(name)

if not images_without_masks and not masks_without_images:
    print("\nSUCCESS: Every image has a corresponding mask.")