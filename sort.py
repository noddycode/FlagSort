from collections import namedtuple

import pygame
from PIL import Image

ColorBand = namedtuple('ColorBand', ('color', 'y', 'height'))

if __name__ == '__main__':
  flag = Image.open('Flag.png')
  width, height = flag.size
  color_bands = []
