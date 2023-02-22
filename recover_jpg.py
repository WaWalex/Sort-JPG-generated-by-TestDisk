import math
import os
import exifread
from shutil import copyfile
import datetime

SRC_PATH = 'D:/recovery'
OUT_PATH = 'E:/recovery2/jpg'
TAGS = ['Canon IXUS 210', 'SM-G925F', 'MI 9', 'DSC-W210', 'GT-I9195', 'Canon EOS 2000D', 'Canon EOS 6D', 'GT-S6500']

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
                if (str(tags['Image Model']) in TAGS):
                    examine_copy(file_path, tags)
                else:
                    print(f"SKIP MODEL '{str(tags['Image Model'])}'?")
                    # input()
            else:
                print(f"No TAGS for '{file_path}'")
        except Exception as e:
            print(e, file_path)
            # input()
