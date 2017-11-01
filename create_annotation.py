import os
import argparse
from PIL import Image

'''
Creates annotation files based on submitted arguments.
Requires the name of the file and bounding box dimensions.
'''

#Constants
JPEG_FOLDER = 'JPEGImages'
TEMPLATE = 'template.xml'

def check_box(box):
    x1, y1, x2, y2 = box[0], box[1], box[2], box[3]
    if x1 >= x2:
        raise ValueError("xmin must be less than xmax")
    if y1 >= y2:
        raise ValueError("ymin must be less than ymax")
    if x1 < 0 or y1 < 0 or x2 < 0 or y2 < 0:
        raise ValueError("Negative coordinates detected")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', help='The image file name, assumes it is in JPEG_FOLDER')
    parser.add_argument('-b', '--bounding_box', nargs=4, type=int, help='Four integers that indicate bounding box of the object of interest')
    args = parser.parse_args()

    #Get image file and image data
    image_name = args.file
    box = args.bounding_box
    check_box(box)

    image_path = os.path.abspath('{}/{}'.format(JPEG_FOLDER, image_name))
    w, h = Image.open(image_path).size
    image_name = image_name.split(".")[0] #get rid of file extension

    #Open template file and read entire file as string
    #Create new file and insert formatted string
    with open(TEMPLATE, 'r') as f:
        fmt_string = f.read().format(image_name, image_path, w, h, box[0], box[1], box[2], box[3])
        with open("Annotations/{}.xml".format(image_name), "w+") as out:
            out.write(fmt_string)

