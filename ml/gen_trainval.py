import os

"""
Locates the Annotations folder, finds all files 
and prints the annotation file name with the corresponding image file name
into trainval.txt and test.txt.
"""

HOME = '/home/edmond'
DATASET = 'ml'
base = HOME + '/data/caffe-data/'
TEST_FILE = 'test.txt'
TRAIN_FILE = 'trainval.txt'
TEST_SIZE = 12

#Get all image names and place onto list
filenames = []
for fname in os.listdir(base + DATASET + '/Annotations'):
    if "_out" in fname:
        try:
            idx = fname.index("_out")
        except Exception as e:
            continue
        folder = fname[:idx] + '/'
        img_name = fname[idx+1:].replace('.xml', '.jpg')
    else:
        folder = ''
        img_name = fname.replace(".xml", ".jpg")

    first = DATASET + '/JPEGImages/' + folder + img_name
    second = DATASET + '/Annotations/' + fname
    print(first + ' ' + second)
    filenames.append(str(first + ' ' + second))

#Split list, add names to files
trainfiles = filenames[ : len(filenames) - TEST_SIZE - 1]
testfiles = filenames[len(filenames) - TEST_SIZE : ]
with open(TRAIN_FILE, "a") as trainfile:
    for txt in trainfiles:
        trainfile.write(txt + '\n')

with open(TEST_FILE, "a") as testfile:
    for txt in testfiles:
        testfile.write(txt + '\n')

#Create test data image size file
os.system("{0} {1} {2} {3}".format(os.getenv('CAFFE_ROOT') + '/build/tools/get_image_size', base, TEST_FILE, "test_name_size.txt"))

