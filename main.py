from __future__ import print_function

import numpy as np
import cv2
from visual import Visualizer 
from ops import conv, dilated_conv, deconv

def compare(h1,h2):
           size = h1.shape[0]
           res = np.zeros([size,size]).astype(np.uint8)
           for i in range(size):
                      for j in range(size):
                                 if not h1[j][i] == h2[j][i]:
                                            res[j][i] = 255
           cv2.imwrite('cmp.jpg',res)
           return res

def convs(num):
           h0 = {}
           h0['data'] = np.array([[1]])
           h0['stride'] = 1
           for i in range(num):
                      tmp = conv(h0,stride=1)
                      h0 = tmp
                      v = Visualizer(20)
                      v.visual(tmp)
                      v.save('.\\conv\\'+str(i)+'.jpg')
                      print('conv: ',v.size())
                      
def dilated_convs(num):
           #r = [1,1,2,2,4,4,2,2,1,1]
           r = [1,2,4,8,16,32,64,128,256]
           h0 = np.array([[1]])
           for i in range(num):
                      #n = i%3
                      tmp = dilated_conv(h0,rate=r[i])
                      h0 = tmp
                      v = Visualizer(20)
                      v.visual(tmp)
                      v.save('.\\dilated_conv\\z_'+str(i+1)+'.jpg')
                      print('dconv: ', v.size())

def my_net():
           net = []
           h0 = {}
           h0['data'] = np.array([[1]])
           h0['stride'] = 1
           h1 = conv(h0,kernel=5)
           net.append(h1)
           
           h2 = conv(h1,stride=2)
           net.append(h2)
           h3 = conv(h2)
           net.append(h3)
           
           h4 = conv(h3,stride=2)
           net.append(h4)
           h5 = conv(h4)
           net.append(h5)
           
           h6 = conv(h5,stride=2)
           net.append(h6)
           h7 = dilated_conv(h6,rate=2)
           net.append(h7)
           h8 = dilated_conv(h6,rate=5)
           net.append(h8)
           
           h9 = conv(h8)
           net.append(h9)
           
           h10 = deconv(h9)
           net.append(h10)
           h11 = conv(h10)
           net.append(h11)
           
           h12 = deconv(h11)
           net.append(h12)
           h13 = conv(h12)
           net.append(h13)
           
           h14 = deconv(h13)
           net.append(h14)
           h15 = conv(h14)
           net.append(h15)

           h16 = conv(h15)
           net.append(h16)
           h17 = conv(h16)
           net.append(h17)

           for i in range(len(net)):
                      v = Visualizer(1)
                      v.visual_pixel(net[i])
                      v.save('.\\net2\\'+str(i+1)+'.jpg')
                      print('con: '+str(i), v.size())

if __name__=='__main__':
           #convs(10)
           #convs(10)
           my_net()

