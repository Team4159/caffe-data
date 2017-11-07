# Caffe Data

This repository contains training and test data for team 4159's machine learning project.

## Setup

The data is intended to be used with our reflective tape detector. The instructions assume you are using Ubuntu 17.04 or 17.10 and you have set the CAFFE_ROOT environment variable as well as the other three needed to build and run SSD CAFFE. 

Clone this repository in ~/caffe-data/ml (create if it doesn't exist or clone to ml from caffe-data), then move the ml folder that is inside the repo to $CAFFE\_ROOT/data which contains scripts to prepare building the detection model.

## Adding new data
You may add new data in an OS other than Ubuntu and you don't have to setup anything. To add new data, add the image to JPEGImages, then use [LabelImg](https://github.com/tzutalin/labelImg) to create the annotation files. You may install LabelImg directly in Windows, OS X, or Ubuntu. 

When you open LabelImg, you need to open the image directory, then annotation files will be saved in the correct place and annotations that exist for a image will be displayed. Press w to use the bounding box tool then create one over the reflective tape objects (see other images for examples of how to do this). Check the difficult box if something such as the center pipe is obstructing a tape object. Press Ctrl-S to save the annotation  - if you go to another image without doing this then you have to start over for the previous image again!

Currently the image path for all annotation refer to a static directory, this is not needed for creating the custom dataset, if it is, it will be changed to Team4159.

## Creating a custom dataset
Follow the instructions from the [SSD Caffe Wiki](https://github.com/weiliu89/caffe/wiki/Train-SSD-on-custom-dataset):

* From $CAFFE\_ROOT/data/ml, python gen_trainval.py to create text files for training and testing.
* Go to $CAFFE\_ROOT then run ./data/ml/create_data.sh to create the LMDB file
* Now the data is ready to be trained, read the training instructions in our caffe repo to learn more.
