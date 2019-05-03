from collections import namedtuple

import pygame
from PIL import Image, ImageDraw

ColorBand = namedtuple('ColorBand', ('color', 'y', 'height'))

if __name__ == '__main__':
  flag = Image.open('Flag.png')
  width, height = flag.size
  color_bands = []
  last_color = flag.getpixel((500, 0))  # Take from x=500 so we avoid the European Flag part
  last_y = 0
  for y in range(height):
    color = flag.getpixel((500, y))
    if color != last_color:
      color_bands.append(ColorBand(last_color, last_y, y-last_y))
      last_color = color
      last_y = y

  print('\n'.join(str(band) for band in color_bands))

  test_img = Image.new(flag.mode, (width, height), color=(255,255,255))
  draw = ImageDraw.Draw(test_img)
  for i, band in enumerate(color_bands):
    draw_height = band.height
    if i == len(color_bands)-1:
      draw_height -= 1

    draw.rectangle(((0, band.y), (width, band.y+draw_height)), fill=band.color)

  test_img.save('TestImage.png', 'PNG')

