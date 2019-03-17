#!/usr/bin/python3
import cv2
import numpy as np
import os
import pandas as pd
from PIL import Image
from sklearn.model_selection import train_test_split
vid_cam = cv2.VideoCapture(0)
while(True):

    # Capture video frame
	_, image_frame = vid_cam.read()

    # Convert frame to grayscale
	gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)
	cv2.imshow('frame', image_frame)
	if cv2.waitKey(100) & 0xFF == ord('c'):
		
		cv2.imwrite("images.jpg",image_frame)
		break
vid_cam.release()
cv2.destroyAllWindows()
pic = Image.open("images.jpg")
pix = np.array(pic.getdata()).reshape(pic.size[0], pic.size[1], 3)
flat_arr = pix.ravel()
list1 = flat_arr.tolist()
list1 = list1[0:4]
#print(list1)
tested = np.array(list)
dataset = pd.read_csv("/home/shubham/data/Dataset/user_10/user_10_loc.csv")
x = dataset['image']
y = dataset.iloc[:,1:-1]
decode = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',10:'j',11:'k',12:'l',13:'m',14:'n',15:'o',16:'p',17:'q',18:'r',19:'s',20:'t',21:'u',22:'v',23:'w',24:'x',25:'y',26:'z'}
from sklearn import preprocessing
#le = preprocessing.LabelEncoder()
#le.fit(x[:,0])
#x[:,0] = le.transform(x[:,0])
#onehotencoder = OneHotEncoder(categorical_features = [0])
#x = onehotencoder.fit_transform(x).toarray()


x_train , x_test , y_train, y_test = train_test_split( x , y , test_size = 0.1)
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier()
classifier.fit(y_train,x_train)
x_pred = classifier.predict (tested)
print (x_pred)
#print (x_test)
#print (x_pred)
#print (dataset)
#from sklearn.metrics import accuracy_score
#score = accuracy_score(x_test,x_pred)
#print (score)


