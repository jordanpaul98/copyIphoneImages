
from PIL import Image
from PIL.ExifTags import TAGS

import os
import shutil

#Directory that contains the images
dir_from = input("Downloaded Photo Directory: ")

#Directory to copy images to
dir_to = input("Folder location to save to: ")

if dir_to == dir_from:
    print("Folder location cant be the same!")
    exit()


def getCameraModel(image_path):
    img = Image.open(image_path)

    exif_data = img._getexif()

    for tag_id, value in exif_data.items():
        tag = TAGS.get(tag_id, tag_id)
        if tag == "Model":
            return value

    return None


iphone_model = ''

try:
    while True:

        if input("Manually enter iPhone Model? [Y/N] ") in ['Y', 'y']:
            iphone_model = input("Enter Iphone Model ('na' for no model): ")

            if iphone_model in ['na', "NA", 'Na']:
                iphone_model = None
            break
        else:
            image_name = input("Enter Image name to extract meta data: ")
            iphone_model = getCameraModel(image_name)

            if iphone_model is None:
                cont = input("No iPhone Model found in Image: Continue with no model? [Y/N]")
                if cont in ['Y', "y"]:
                    break
            else:
                print(f"Model: {iphone_model} found!")
                break

    for filename in os.listdir(dir_from):
        if "." in filename and filename.split(".")[-1] == "JPG":

            photo_path = os.path.join(dir_from, filename)

            model = getCameraModel(photo_path)

            if model == iphone_model:

                photo_to = os.path.join(dir_to, filename)

                shutil.copy2(photo_path, photo_to)

                print(f"Copied {filename} from {dir_from} to {dir_to}")

except Exception as e:
    print(f"Error Occurred! {e}")
    exit()

print("All done :) bye.")
