#!/usr/bin/env python  
# -*- coding: utf-8  -*-
#time:'2018/4/27 下午 9:18'
#author:'jiayiming'

import tesserocr
from PIL import Image
image = Image.open('image.png')
print(tesserocr.image_to_text(image))

