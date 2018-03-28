import numpy as np
import cv2
from visual import Visualizer 
from ops import conv, dilated_conv

def compare(h1,h2):
           size = h1.shape[0]
           res = np.zeros([size,size]).astype(np.uint8)
           for i in range(size):
                      for j in range(size):
                                 if not h1[j][i] == h2[j][i]:
                                            res[j][i] = 255
           cv2.imwrite('cmp.jpg',res)
           return res

if __name__=='__main__':
           v1 = Visualizer(20)
           h0 = np.array([[1]])
           h1 = dilated_conv(h0, rate=2)
           h2 = dilated_conv(h1, rate=4)
           h3 = conv(h2,kernel_size=3)
           h41 = conv(h3,kernel_size=3)
           v1.visual(h41)
           v1.save('conv.jpg')

           v2 = Visualizer(20)
           h1 = conv(h0,kernel_size=3)
           h2 = dilated_conv(h1, rate=2)
           h3 = conv(h2,kernel_size=3)
           h42 = dilated_conv(h3, rate=4)
           v2.visual(h42)
           v2.save('dilate_conv.jpg')

           v3 = Visualizer(20)
           res = compare(h41,h42)
           v3.visual(res)
           v3.save('cmpr.jpg')

