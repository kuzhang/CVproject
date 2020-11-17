
import os,glob,pdb
import numpy as np
import pandas as pd
import shutil


# SIXray Dataset. Remove the comment to activate the code for this part

root= '/home/dlp/dataset/SIXray'
split_file_train = os.path.join(root,'ImageSet/10/train.csv')
split_file_test = os.path.join(root,'ImageSet/10/test.csv')
train_data = pd.read_csv(split_file_train, sep=',')
test_data = pd.read_csv(split_file_test, sep=',')

train_file_name = train_data['name'][:]
test_file_name = test_data['name'][:]

for name in train_file_name:
    if name[0] in ['P']:
        file = os.path.join(root,'positive',name+'.jpg')
        target = os.path.join('/home/dlp/github/ganomaly/data/SIXray/train/1.abnormal', name+'.jpg')
    else:
        file = os.path.join(root, 'negative', name+'.jpg')
        target = os.path.join('/home/dlp/github/ganomaly/data/SIXray/train/0.normal', name+'.jpg')

    if os.path.exists(file):
        shutil.copy(file,target)
    #pdb.set_trace()

for name in test_file_name:
    if name[0] in ['P']:
        file = os.path.join(root, 'positive', name + '.jpg')
        target = os.path.join('/home/dlp/github/ganomaly/data/SIXray/test/1.abnormal', name + '.jpg')
    else:
        file = os.path.join(root, 'negative', name + '.jpg')
        target = os.path.join('/home/dlp/github/ganomaly/data/SIXray/test/0.normal', name + '.jpg')

    if os.path.exists(file):
        shutil.copy(file, target)




