import datetime
import os
from shutil import copyfile

import exifread

SRC_PATH = 'D:/recovery'
OUT_PATH = 'E:/recovery2/jpg'
MODELS = []

file_copied = 1
jpg_files = []
    
def examine_copy(src, tags):
    global file_copied
    
    # extract date
    image_datetime_str: str = str(tags['Image DateTime'])
    image_dt = datetime.datetime.strptime(image_datetime_str, '%Y:%m:%d %H:%M:%S')

    # create folder
    dst_folder = os.path.join(OUT_PATH, str(image_dt.year), str(tags['Image Model']))
    os.makedirs(dst_folder, exist_ok=True)

    # generate filename
    dst = str(image_dt.year) + '-' + str(image_dt.month).zfill(2) + '-' + str(image_dt.day).zfill(2) + ' ' + str(image_dt.hour).zfill(2) + '.' + str(image_dt.minute).zfill(2) + '.' + str(image_dt.second).zfill(2) + ".jpg"
    dst = os.path.join(dst_folder, dst)

    # copy file
    perc = round((file_copied/len(jpg_files)*100), 2)
    if not os.path.exists(dst): 
        copyfile(src, dst)
        print(f"{perc}% '{src}' copied to '{dst}'!")
    else:
        print(f"{perc}% '{src}' SKIPPED!")
    file_copied += 1


if __name__ == "__main__":
    # find all JPG files
    for root, dirs, files in os.walk(SRC_PATH):
        for file in files:
            if file.endswith(".jpg"): 
                jpg_files.append(os.path.join(root,file))

    # search for TAGS matching in photo's metadata 
    for file_path in jpg_files:
        try:
            f = open(file_path, 'rb')
            tags = exifread.process_file(f)
            if tags != {} and 'Image Model' in tags:
                if (str(tags['Image Model']) in MODELS):
                    examine_copy(file_path, tags)
                else:
                    image_model = str(tags['Image Model'])
                    res = input(f"ARE YOU INTERESTED IN THIS DEVICE '{image_model}'? [y/n]")
                    if (str.lower(res) == 'y'):
                        MODELS.append(image_model)
            else:
                print(f"No TAGS for '{file_path}'")
        except Exception as e:
            print(e, file_path)
            input("Press ENTER to continue...")
