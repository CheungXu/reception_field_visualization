import numpy as np

def conv(image, kernel = 3, stride = 1):
           if kernel % 2 == 0:
                      print('Wrong Kernel Size!')
                      return []
           padding = (kernel - 1)/2
           input_ = image['data']
           pre_stride = image['stride']
           input_size = input_.shape[0]
           new_size = input_size + (kernel - 1) * pre_stride
           kernel_mat = np.ones([kernel,kernel])
           res = np.zeros([new_size,new_size])
           for i in range(kernel):
                      for j in range(kernel):
                                 conv_rect = kernel_mat[j][i] * input_
                                 res[j*pre_stride:j*pre_stride+input_size, i*pre_stride:i*pre_stride+input_size] += conv_rect
           img = {}
           img['data'] = res
           img['stride'] = stride
           return img

def deconv(image, kernel=3, stride=1):
           return conv(image,kernel,stride)

def dilated_conv(image, rate = 1):
           if rate < 1:
                      print('Wrong Dilated Rate!')
                      return []
           input_ = image['data']
           input_size = input_.shape[0]
           kernel = 4 * rate - 1
           padding = (kernel - 1)/2
           new_size = input_size + padding * 2
           kernel_mat = np.zeros([kernel,kernel])
           res = np.zeros([new_size,new_size])
           for i in range(3):
                      for j in range(3):
                                 kernel_mat[(j+1)*rate-1][(i+1)*rate-1] = 1
           for i in range(kernel):
                      for j in range(kernel):
                                 if kernel_mat[j][i] > 0:
                                            conv_rect = kernel_mat[j][i] * input_
                                            res[j:j+input_size, i:i+input_size] += conv_rect
           img = {}
           img['data'] = res
           img['stride'] = 1
           return img
