
from PIL import Image
from PIL.ExifTags import TAGS

import os
import shutil

# ////////////////////////////////////
#Directory that contains the images
# ////////////////////////////////////
dir_from = ''

# ////////////////////////////////////
#Directory to copy images to
# ////////////////////////////////////
dir_to = ''

if dir_from == '' or dir_to == '':
    print("Please add the to and from directories")

# iPhone Model to move
iphone_model = ""

def getCameraModel(image_path):
    img = Image.open(image_path)

    exif_data = img._getexif()

    for tag_id, value in exif_data.items():
        tag = TAGS.get(tag_id, tag_id)
        if tag == "Model":
            return value

    return None

# //////////////////////////////////////////////////
# Local image to test and find what iPhone model is
# //////////////////////////////////////////////////
local_image_to_test_name = ""

if local_image_to_test_name == "":
    print("Please add local image to test")
    exit(0)

print(f"Moving File linked to camera Model: {getCameraModel(local_image_to_test_name)
    if local_image_to_test_name else "NA"}")


if iphone_model == "None": exit(0)


for filename in os.listdir(dir_from):
    if "." in filename and filename.split(".")[-1] == "JPG":

        photo_path = os.path.join(dir_from, filename)

        model = getCameraModel(photo_path)

        if model == iphone_model:

            photo_to = os.path.join(dir_to, filename)

            shutil.copy2(photo_path, photo_to)

            print(f"Copied {filename} from {dir_from} to {dir_to}")
            
 
print("All done :)") # jordan
