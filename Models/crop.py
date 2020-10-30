import os
import cv2
import matplotlib.pyplot as plt
import shutil

l = os.listdir('../plantvillage-dataset/color/folder_name')

#create output folder(data):
os.mkdir('../data')              #provide full path

for i in l[0:]:
    path = os.path.join('../plantvillage-dataset/color/folder_name',i)   #pls provide the full path
    img = cv2.imread(path)
    s=0
    g = []
    for k in range(0,img.shape[0],64):   
        for j in range(0,img.shape[1],64):
            crop = img[k:k+64,j:j+64]                           #cropped image
            s=s+1                                               #counter variable
            #saving the cropped image in data folder--
            cv2.imwrite(os.path.join('../data','NO.'+str(s)+'_'+i),crop)    #pls provide the full path

