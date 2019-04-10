# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 19:54:01 2019

@author: Administrator
"""

from PIL import Image
import numpy as np

def pca(X):
    '''主成分分析
        输入：矩阵X,其中该矩阵中存储训练数据，每一行为一条训练数据
        返回：投影矩阵（按照维度的重要性排序）、方差和均值'''
    #获取维度
    num_data , dim = X.shape
    #数据中心化
    mean_X = X.mean(axis = 0)
    X = X - mean_X
    
    if dim > num_data:
        #PCA_使用紧致技巧
        M = np.dot(X,X.T)#协方差矩阵
        e,EV = np.linalg.eigh(M)#特征值和特征向量
        tmp = np.dot(X.T,EV).T#这就是紧致技巧
        V = tmp[::-1]#由于最后特征向量是我们所需要的，所以逆转
        S = np.sqrt(e)[::-1]#由于特征值是按照递增顺序排列的，所以逆转
        for i in range(V.shape[1]):
            V[:,i] /= S
    else:
        #PCA-使用SVD方法
        U,S,V = np.linalg.svd(X)
        V = V[:num_data]#仅返回前num_data维数据才合理
        
    #返回投影矩阵、方差和均值
    return V,S,mean_X