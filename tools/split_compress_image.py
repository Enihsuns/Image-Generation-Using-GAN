# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 15:09:27 2019

@author: Eni
"""

import os
from PIL import Image

def split_compress(img_name, in_path, out_path, box_w, box_h, resize_w, resize_h):
    '''
    box_w: Expected image width. 
    box_h: Expected image height.
    resize_w: Resized image width.
    resize_h: Resized image height.
    '''
    img = Image.open(os.path.join(in_path, img_name))
    w, h = img.size
    
    img_name = img_name.split('.')[:-1]
    
    row_num, col_num = int(w/box_w), int(h/box_h)
    
    cnt = 1
    for i in range(row_num):
        for j in range(col_num):
            cropped_img_name = ''.join(img_name) + '_' + str(box_w) + '_' + str(cnt) + '.jpg'
            
            # Crop image
            cropped_img = img.crop(box=(i*box_w, j*box_h, (i + 1)*box_w, (j + 1)*box_h))
            
            # Compress image
            cropped_img = cropped_img.resize((resize_w, resize_h))
            
            # Save image
            cropped_img.save(os.path.join(out_path, cropped_img_name))
            
            cnt = cnt + 1

in_path = '.\\薛亮\\'
out_path = '.\\data\\generated\\'

for item in os.listdir(in_path):
    if(item.split('.')[-1] == 'jpg'):
        split_compress(item, in_path, out_path, 500, 500, 224, 224)
        split_compress(item, in_path, out_path, 1000, 1000, 224, 224)
    
    
    
    