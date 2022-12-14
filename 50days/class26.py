#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2022/12/14 17:07
# @Author: Ylei
# @File  : class26.py
# @Topic ：用python处理图像

from PIL import Image
from PIL import ImageFilter

image = Image.open('img.png')
print(image.format)
print(image.size)
print(image.mode)
# image.show()
# image.crop((80, 20, 210, 260)).show()
# image.thumbnail((128, 128))
# image.show()

he_image = Image.open('img_1.png')
image_part = image.crop((80, 20, 210, 210))
width, height = image_part.size
he_image.paste(image_part.resize((int(width / 1.5), int(height / 1.5))), (172, 40))
# he_image.show()

# image.rotate(45).show()
#DeprecationWarning: FLIP_LEFT_RIGHT is deprecated and will be removed in Pillow 10 (2023-07-01). Use Transpose.FLIP_LEFT_RIGHT instead.
# image.transpose(Image.FLIP_LEFT_RIGHT).show()
# image.transpose(Image.FLIP_TOP_BOTTOM).show()

# for x in range(20, 100):
#     for y in range(20, 100):
#         image.putpixel((x, y), (0, 160, 160))
# # image.show()

image.filter(ImageFilter.CONTOUR).show()
