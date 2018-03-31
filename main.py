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

def convs(num):
           h0 = np.array([[1]])
           for i in range(num):
                      tmp = conv(h0)
                      h0 = tmp
                      v = Visualizer(20)
                      v.visual(tmp)
                      v.save('.\\conv\\'+str(i)+'.jpg')
                      print 'conv: ',v.size()
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
                      print 'dconv: ', v.size()


            
if __name__=='__main__':
           #convs(10)
           dilated_convs(10)

