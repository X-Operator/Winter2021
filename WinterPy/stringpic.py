#！usr/bin/env python
# -*- coding:utf-8 -*-

from PIL import Image

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'.œ∑´®†¥¨ˆøπ ")
length = len(ascii_char)
im = Image.open('mygirl.jpeg')
im = im.resize((240, 240))    #重新调整宽高
width, height = im.size


def get_char(r, g, b, alpha=256):    #RGB转为list里的字符
    if alpha == 0:
        return ' '
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)    #RGB公式转灰度值
    return ascii_char[int(gray * length / 256)]


output = ""    #String字符串输出
for i in range(height):
    for j in range(width):
        output += get_char(*im.getpixel((j, i)))
    output += '\n'

f = open('textPicture.txt', 'w')
f.write(output)
f.close()