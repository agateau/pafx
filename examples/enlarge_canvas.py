#!/usr/bin/env python3
import os
import sys

from PIL import Image

from pafx import clone_format, paste, BOTTOM_RIGHT


src_filename = sys.argv[1]
dst_dirname = sys.argv[2]

img = Image.open(src_filename)

for size in 48, 64, 128:
    dst = clone_format(img, (size, size))
    paste(dst, img)
    paste(dst, img, dst_anchor=BOTTOM_RIGHT, src_anchor=BOTTOM_RIGHT)
    filepath = os.path.join(dst_dirname, 'enlarged-{}.png'.format(size))
    dst.save(filepath)
