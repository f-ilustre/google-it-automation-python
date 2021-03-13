#!/usr/bin/env python3

import os
from PIL import Image

directory = '/supplier-data/images/'

for filename in os.listdir(directory):
    if 'tiff' in filename:
        im = Image.open(directory + filename)
        f, e = os.path.splitext(filename)
        directory1 = '/supplier-data/images/'
        outfile = f + '.jpeg'
        im.resize((600, 400)).convert('RGB').save(directory1 + outfile)