from __future__ import print_function

import numpy as np
import cv2,os
from visual import Visualizer 
from ops import conv, dilated_conv, deconv

def convs(num):
           #Create Path
           if not os.path.exists(os.path.join('.','conv')):
                        os.mkdir(os.path.join('.','conv'))
           
           #Init Input
           h0 = {}
           h0['data'] = np.array([[1]])
           h0['stride'] = 1
           
                                 
           #Stack Conv Layers and visual&save
           for i in range(num):
                      tmp = conv(h0,stride=2)
                      h0 = tmp
                      v = Visualizer(20)
                      v.visual(tmp)
                      v.save(os.path.join('.','conv',str(i)+'.jpg'))
                      print('conv: ',v.size())
                      
def dilated_convs(num):
           #Create Path  
           if not os.path.exists(os.path.join('.','dconv')):
                        os.mkdir(os.path.join('.','dconv'))
           #Dilate Rate of Each Layer
           r = [1,2,5,1,2,7,1,2,9,2,1]
           
           #Init Input
           h0 = {}
           h0['data'] = np.array([[1]])
           h0['stride'] = 1
           
           #Stack Dilated Conv Layers
           for i in range(num):
                      tmp = dilated_conv(h0,rate=r[i])
                      h0 = tmp
                      v = Visualizer(20)
                      v.visual(tmp)
                      v.save(os.path.join('.','dconv',str(i+1)+'.jpg'))
                      print('dconv: ', v.size())
           

def example():
           net = []
           h0 = {}
           h0['data'] = np.array([[1]])
           h0['stride'] = 1

           h1 = conv(h0)
           h2 = conv(h1)
           h3 = dilated_conv(h3)
           h4 = dilated_conv(h4)

           rect_size = 20
           v = Visualizer(rect_size)
           v.visual(h4)
           v.save(os.path.join('.','res.jpg'))
           print('con: '+str(i), v.size())

if __name__=='__main__':
             dilated_convs(10)
             convs(10)
             example()

