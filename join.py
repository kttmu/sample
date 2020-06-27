import numpy as np
import cv2
import glob
import re
import matplotlib.pyplot as plt
from config import dir_num, datalist_
import copy

#read
datalist = []
for line in datalist_:
  datalist.append(glob.glob(line))

#sort 
sort = [["test"] * len(datalist[0]) for i in range(len(datalist))]

regex = re.compile('\d+')
for i in range(dir_num):
    for j in range(len(datalist[0])):
        ten = regex.findall(datalist[i][j])
        sort[i][int(ten[-1])-1] = datalist[i][j]

#kakuninn
for i in range(len(datalist[0])):
    print(sort[0][i] + sort[1][i] + sort[2][i])





