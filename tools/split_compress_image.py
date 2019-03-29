# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 15:09:27 2019

@author: Eni
"""

import os
from PIL import Image

def split_compress(img_name, in_path, out_path, box_factor, resize_w, resize_h):
    '''
    box_factor: The factor of cropping box corresponding to the original image.
    resize_w: Resized image width.
    resize_h: Resized image height.
    '''
    img = Image.open(os.path.join(in_path, img_name))
    w, h = img.size
    
    img_name = img_name.split('.')[:-1]
    
    box_w = box_h = min(w, h)*box_factor
    
    row_num, col_num = 2*int(w/box_w), 2*int(h/box_h)
    
    cnt = 1
    for i in range(row_num):
        for j in range(col_num):
            cropped_img_name = ''.join(img_name) + '_' + '{:.0f}'.format(box_w) + '_' + str(cnt) + '.jpg'
            
            # Crop image
            left, top, right, bottom = i*box_w/2, j*box_h/2, (i/2 + 1)*box_w, (j/2 + 1)*box_h
            if(right > w):
                left = left - (right - w)
                right = w
            if(bottom > h):
                top = top - (bottom - h)
                bottom = h
            
            cropped_img = img.crop(box=(left, top, right, bottom))
            
            # Compress image
            cropped_img = cropped_img.resize((resize_w, resize_h))
            
            # Save image
            cropped_img.save(os.path.join(out_path, cropped_img_name))
            
            cnt = cnt + 1

base_path = 'E:\\Work\\ImageGeneration\\'
in_path = os.path.join(base_path, '白雪石\\') 
out_path = os.path.join(base_path, 'data\\generated\\')

for item in os.listdir(in_path):
    if(item.split('.')[-1] == 'jpg'):
        split_compress(item, in_path, out_path, 0.3, 500, 500)
        split_compress(item, in_path, out_path, 1, 500, 500)
    
    
    
    