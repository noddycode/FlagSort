import colorsys
import math
from collections import namedtuple

import pygame
from PIL import Image, ImageDraw

ColorBand = namedtuple('ColorBand', ('color', 'y', 'height'))

# Key functions sourced from https://www.alanzucconi.com/2015/09/30/colour-sorting/

def naive_key(band):
  return band.color

def hsv_key(band):
  return colorsys.rgb_to_hsv(*band.color)

def luminosity_key(band):
  r, g, b = band.color
  return math.sqrt(.241 * r + .691 * g + .068 * b)

def step_key(band):
  repetitions = 2

  r, g, b = band.color
  lum = math.sqrt(.241 * r + .691 * g + .068 * b)

  h, s, v = colorsys.rgb_to_hsv(r, g, b)

  h2 = int(h * repetitions)
  lum2 = int(lum * repetitions)
  v2 = int(v * repetitions)

  return h2, lum, v2


if __name__ == '__main__':
  flag = Image.open('Flag.png')
  width, height = flag.size
  color_bands = []
  last_color = flag.getpixel((500, 0))  # Take from x=500 so we avoid the European Flag part
  last_y = 0
  for y in range(height):
    color = flag.getpixel((500, y))
    if color != last_color:
      color_bands.append(ColorBand(last_color, last_y, y-last_y-1))
      last_color = color
      last_y = y

  # Grab the last color band
  color_bands.append(ColorBand(last_color, last_y, y-last_y))

  color_bands = sorted(color_bands, key=hsv_key)

  print('\n'.join(str(band) for band in color_bands))

  test_img = Image.new(flag.mode, (width, height), color=(255, 0, 0))
  draw = ImageDraw.Draw(test_img)
  curr_y = 0
  for band in color_bands:
    draw.rectangle(((0, curr_y), (width, curr_y+band.height)), fill=band.color)
    curr_y += band.height+1

  test_img.save('TestImage.png', 'PNG')

