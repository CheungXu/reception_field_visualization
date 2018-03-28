import numpy as np

def conv(input_, kernel_size = 3):
           if kernel_size % 2 == 0:
                      print('Wrong Kernel Size!')
                      return []
           padding = (kernel_size - 1)/2
           input_size = input_.shape[0]
           new_size = input_size + padding * 2
           kernel = np.ones([kernel_size,kernel_size])
           res = np.zeros([new_size,new_size])
           for i in range(kernel_size):
                      for j in range(kernel_size):
                                 conv_rect = kernel[j][i] * input_
                                 res[j:j+input_size, i:i+input_size] += conv_rect
           return res

def dilated_conv(input_, rate = 1):
           if rate < 1:
                      print('Wrong Dilated Rate!')
                      return []
           input_size = input_.shape[0]
           kernel_size = 4 * rate - 1
           padding = (kernel_size - 1)/2
           new_size = input_size + padding * 2
           kernel = np.zeros([kernel_size,kernel_size])
           res = np.zeros([new_size,new_size])
           for i in range(3):
                      for j in range(3):
                                 kernel[(j+1)*rate-1][(i+1)*rate-1] = 1
           for i in range(kernel_size):
                      for j in range(kernel_size):
                                 conv_rect = kernel[j][i] * input_
                                 res[j:j+input_size, i:i+input_size] += conv_rect
           return res
