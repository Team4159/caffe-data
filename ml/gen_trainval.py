import os

"""
Locates the Annotations folder, finds all files 
and prints the annotation file name with the corresponding image file name.
The output may be copied and pasted to test.txt and trainval.txt
"""

USERNAME = 'edmond'
base = '/home/' + USERNAME + '/Desktop/caffe/data/VOCdevkit_STEAMWORKS/ml'
for fname in os.listdir(base + '/Annotations'):
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

    first = 'ml/JPEGImages/' + folder + img_name
    second = 'ml/Annotations/' + fname
    print(first + ' ' + second)
