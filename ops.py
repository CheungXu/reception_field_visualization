import numpy as np
from common import *

class feature_map(object):
    def __init__(self, data, pre_stride):
        self.data = data
        self.pre_stride = pre_stride

class kernel_conv(object):
    def __init__(self, kernel = np.ones([3,3]), stride = 1):
        #kernel格式判断
        self.kernel = None
        check_res = self.check_kernel(kernel)
        if isinstance(check_res, ReturnErrCode):
            print(check_res.print_info)
            kernel = np.ones([3,3])
        else:
            self.kernel = kernel
        
        #strid格式判断
        if isinstance(stride, int):
            self.stride = stride
        else:
            print('Wrong Stride Type (must be int) !')
            self.stride = 1

    #判断kernel格式是否合法
    def check_kernel(self, kernel):
        if not kernel.ndim == 2:
            return ReturnErrCode('Wrong Kernel Dims (must be 2) !')
        if kernel.shape[0] != kernel.shape[1]:
            return ReturnErrCode('Wrong Kernel Shape (must equal) !')
        if kernel.shape[0] % 2 == 0:
            return ReturnErrCode('Wrong Kernel Size!')
        else:
            return True

    #卷积核权重归一化
    def kernel_normalize(self):
        kernel_sum = np.sum(self.kernel)

        return self.kernel/kernel_sum

    #计算卷积感受野权重矩阵
    def conv(self, feat_map):
        input_ = feat_map.data
        input_size = input_.shape[0]
        pre_stride = feat_map.pre_stride
        kernel_size = self.kernel.shape[0]

        new_size = input_size + (kernel_size - 1) * pre_stride
        kernel_mat = self.kernel_normalize()
        res = np.zeros([int(new_size), int(new_size)])
        for i in range(kernel_size):
            for j in range(kernel_size):
                conv_rect = kernel_mat[j][i] * input_
                res[j*pre_stride:j*pre_stride+input_size, i*pre_stride:i*pre_stride+input_size] += conv_rect
        res = feature_map(res, self.stride)
        return res

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
           kernel = 2 * rate + 1
           padding = (kernel - 1)/2
           new_size = input_size + padding * 2
           kernel_mat = np.zeros([kernel,kernel])
           res = np.zeros([int(new_size),int(new_size)])
           for i in range(3):
                      for j in range(3):
                                 kernel_mat[j*rate][i*rate] = 1
           for i in range(kernel):
                      for j in range(kernel):
                                 if kernel_mat[j][i] > 0:
                                            conv_rect = kernel_mat[j][i] * input_
                                            res[j:j+input_size, i:i+input_size] += conv_rect
           img = {}
           img['data'] = res
           img['stride'] = 1
           return img
