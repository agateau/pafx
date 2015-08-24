#!/usr/bin/env python3
import sys

from PIL import Image

from pafx import add_outline, add_depth


src_filename = sys.argv[1]
dst_filename = sys.argv[2]

img = Image.open(src_filename)

img = add_depth(img, color='#595652')
img = add_depth(img, color='#595652')
img = add_outline(img, color='black')

img.save(dst_filename)
