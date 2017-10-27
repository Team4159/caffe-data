# Caffe Data

This repository contains training and test data for team 4159's machine learning project.

## Setup

The data is intended to be used with our reflective tape detector. Clone this repository in ~/caffe-data/ml (create if it doesn't exist or clone to ml from caffe-data), then move the ml folder that is inside the repo to $CAFFE\_ROOT/data which contains scripts to prepare building the detection model.

## Creating a custom dataset
Follow the instructions from the [SSD Caffe Wiki](https://github.com/weiliu89/caffe/wiki/Train-SSD-on-custom-dataset):

* From $CAFFE\_ROOT/data/ml, python gen_trainval.py to create text files for training and testing.
* Go to $CAFFE\_ROOT then run ./data/ml/create_data.sh to create the LMDB file
* Now the data is ready to be trained, read the training instructions in our caffe repo to learn more.
