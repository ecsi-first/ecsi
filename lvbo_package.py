import cv2
import time
import numpy as np
import matplotlib.pyplot as plt
from multipolyfit import multipolyfit
from lvbo_package import lvbo_v

start=time.perf_counter()

picture=4
sub_mse,sub_rgb=0.1,15
file_path="D:/test/test1/{}.jpg".format(picture)
save_path="D:/test/test1/save{}_v.jpg".format(picture)

img=cv2.imread(file_path,1)

height,width,c=img.shape

img1 = np.zeros(img.shape,dtype="uint8")


print("正在计算")
for w in range(0,width):

	key_point=lvbo_v(height,w,img,sub_mse,sub_rgb)
	print(key_point)

	for column in key_point:
		img1[column][w][0]=255
		img1[column][w][1]=255
		img1[column][w][2]=255
	key_point.clear()
	
	print("*"*int(50*w/width),"           ","{0:.2f}%".format(100*(w+1)/width),end='\r')

cv2.imwrite(save_path,img1)

end=time.perf_counter()
print("计算结束,耗时{}s".format(end-start))
