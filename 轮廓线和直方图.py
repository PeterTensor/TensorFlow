# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 10:33:31 2019

@author: Administrator
"""

import numpy as np
import matplotlib as pt
from PIL import Image
import os
import pylab as pl

'''for infile in filelist:
    outfile = os.math.splitext(infile)[0] + '.jpg'
    if infile != outfile:
        try:
            Image.open(infile).save(outfile)
        except:
            print('cannot convert',infile)'''
pil_im = Image.open(r'C:\Users\Administrator\Desktop\微信图片_20190326095645.jpg').convert('L')
#读取图像到数组中
im = np.array(pil_im)
#绘制图像
pl.imshow(im)
#新建一个图像
pl.figure()
#不使用颜色
pl.gray()
#在原点的左上角显示轮廓图像
pl.contour(im,origin = 'image')
pl.axis('equal')
pl.axis('off')
pl.figure()
pl.hist(im.flatten(),128)
pl.show()
#对图像进行反相处理
im2 = 255 - im
pl.imshow(im2)
#将图像像素值表换到100-200区间
im3 = (100.0/255)*im + 100
pl.imshow(im3)
#对图像像素值求平方后得到的图像
im4 = 255.0*(im/255.0)**2
#pl.imshow(im4)
print(int(im.min()),int(im.max()))
#pl.subplot(im2,im3,im4)
#一些点
'''
x = [100,100,400,400]
y = [200,500,200,500]
#使用红色星状标记绘制点
plot(x,y,'y-')
#绘制连接前两个点的线
plot(x[:2],y[:2],'y-')
#添加标题，显示绘制的图像
title('Plotting:"image.jpg"')
show()
#axis('off')'''