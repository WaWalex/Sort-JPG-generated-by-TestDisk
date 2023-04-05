# Sort-JPG-generated-by-TESTDISK
> Simple and lightweight util to sort all the generated folders and unnamed JPG from TESTDISK https://www.cgsecurity.org/wiki/TestDisk.


## General Information
- Provide general information about your project here.
- What problem does it (intend to) solve?
- What is the purpose of your project?
- Why did you undertake it?
<!-- You don't have to answer all the questions - just the ones relevant to your project. -->


## Technologies Used
- TESTDISK by PhotoRec
- Python 3+
- exifread (pip install exifread)


## Screenshots
![immagine](https://user-images.githubusercontent.com/52601911/230055736-8d793653-d0fe-4ce8-b2da-15e83110c305.png)



## Setup
In order to use this simple project you have to install exifread dependency https://pypi.org/project/ExifRead/.

`pip install exifread`


## Usage
1. First you have to recover your files using TestDisk, I'm not going to teach you how to do that, there are a lot of tutorials.
2. If you recovered your files correctly you'll and up with a folder containing a lot of folders labeled 'recup_dir.N', this main folder will be your `SRC_PATH`.
3. Now you have to decide where you want your files to be sorted and copied, this will be your `OUT_PATH`.
4. You can now edit 'recover_jpg.py' and change those two variables at line 7 and 8, make sure to have `TAGS` set to empy: `TAGS = []`
Now you can run the application:

`python ./recover_jpg.py`

You'll soon notice that the program will pause anytime it will encounter a new DEVICE, if you want to keep all the photos made by that device, enter `Y`:

![immagine](https://user-images.githubusercontent.com/52601911/230056614-de1c9b06-e5d9-4d8c-8242-5e740af26ea4.png)

You can now continue this procedure, as soon as the program will end:

![immagine](https://user-images.githubusercontent.com/52601911/230057018-4dd6b2c8-73ad-4d96-bbe5-ca2ebffd319a.png)
![immagine](https://user-images.githubusercontent.com/52601911/230057243-f37014d2-0ba9-478e-b06c-51badfaf2fe7.png)

## Considerations
As you can see from the screenshots, the program will create a folder for the year, inside that a folder for the device and than it will copy all the photos renaming them '%Y:%m:%d %H:%M:%S.jpg'.

I tested it with more than 353GB of data, and more than 350000 files. It worked perfectly! 

## Project Status
Project is: _complete_ 


## Contact
Created by [@WaWalex](mailto:wawalex1122@gmail.com) - feel free to contact me!