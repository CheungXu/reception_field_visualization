import numpy as np
import cv2

class Visualizer(object):
           def __init__(self, rect_size):
                      self.rect_size = rect_size
                      self.line_width = 2
           def draw_rect(self, i, j, fill_color):
                      cv2.rectangle(self.img, (i*self.rect_size+self.line_width,j*self.rect_size+self.line_width), \
                                    ((i+1)*self.rect_size-self.line_width,(j+1)*self.rect_size-self.line_width), fill_color, -1)
                      
           def visual(self,input_):
                      img_size = input_.shape[0]
                      size = img_size * self.rect_size 
                      self.img = np.zeros([size,size,3]).astype(np.uint8)
                      colors  = {}
                      for i in range(img_size):
                                 for j in range(img_size):
                                            colors[input_[i][j]] = 1
                      color_num = len(colors.keys())
                      color_step = int(255/(color_num+1))
                      colors = sorted(colors.items(), key=lambda item:item[0])
                      color_dict = {}
                      num = 1
                      for color in colors:
                                 color_dict[color[0]] = num * color_step
                                 num += 1
                      for i in range(img_size):
                                 for j in range(img_size):
                                            self.draw_rect(i,j,fill_color=[0,color_dict[input_[i][j]],0])
                      cv2.imshow('visual',self.img)
                      cv2.waitKey(0)
                      cv2.destroyAllWindows()
                      
           def show(self):
                      cv2.imshow('visual',self.img)
                      cv2.waitKey(0)
                      cv2.destroyAllWindows()
                      
           def save(self, path):
                      cv2.imwrite(path,self.img)
