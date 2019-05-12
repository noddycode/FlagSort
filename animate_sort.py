import colorsys
import time
from functools import total_ordering

import pygame
from PIL import Image

# Modified version of quickSortIterative by Mohit Kumra
# From https://www.geeksforgeeks.org/iterative-quick-sort/
# Changed to use more stack-like operations, more verbose variable names, and more compact code
# Also changed to generator to enable stepped sorting
def quick_sort_generator(arr, start_idx, end_idx):
  stack = []
  # push initial values of start_idx and end_idx to stack
  stack.append(start_idx)
  stack.append(end_idx)

  # Keep popping from stack while is not empty
  while stack:

    # Pop end_idx and start_idx
    end_idx = stack.pop()
    start_idx = stack.pop()

    # Set pivot element at its correct position in
    # sorted array
    i = (start_idx - 1)

    pivot = arr[end_idx]

    pivot.highlight = (0, 255, 0)

    for j in range(start_idx, end_idx):
      arr[j].highlight = (0, 0, 255)
      yield
      if arr[j] < pivot:
        # increment index of smaller element
        arr[j].highlight = (255, 0, 0)
        yield
        arr[j].highlight = None
        i = i + 1
        color_bands[i], color_bands[j] = color_bands[j], color_bands[i]
        yield

      arr[j].highlight = None

    color_bands[i + 1], color_bands[end_idx] = color_bands[end_idx], color_bands[i + 1]
    yield

    pivot.highlight = None
    pivot_idx = i+1

    # If there are elements on right side of pivot,
    # then push right side to stack
    if pivot_idx+1 < end_idx:
      stack.append(pivot_idx+1)
      stack.append(end_idx)

    # If there are elements on left side of pivot,
    # then push left side to stack
    if pivot_idx-1 > start_idx:
      stack.append(start_idx)
      stack.append(pivot_idx - 1)


@total_ordering
class ColorBand(object):

  def __init__(self, color, height):
    self.color = color
    self.height = height
    self.highlight = None
    
  def draw_rect(self, y, width, draw_surface):
    # draw a highlight color
    if self.highlight:
      draw_surface.fill(self.highlight, pygame.Rect(0, y, width+50, self.height))

    draw_surface.fill(self.color, pygame.Rect(0, y, width, self.height))

  # Sort functions from https://www.alanzucconi.com/2015/09/30/colour-sorting/
  def __eq__(self, other):
    return colorsys.rgb_to_hsv(*self.color) == colorsys.rgb_to_hsv(*other.color)

  def __ne__(self, other):
    return colorsys.rgb_to_hsv(*self.color) != colorsys.rgb_to_hsv(*other.color)

  def __lt__(self, other):
    return colorsys.rgb_to_hsv(*self.color) < colorsys.rgb_to_hsv(*other.color)


if __name__ == '__main__':
  flag = Image.open('Flag.png')
  width, height = flag.size
  color_bands = []
  last_color = flag.getpixel((500, 0))  # Take from x=500 so we avoid the European Flag part
  last_y = 0
  for y in range(height):
    color = flag.getpixel((500, y))
    if color != last_color:
      color_bands.append(ColorBand(last_color, y-last_y))
      last_color = color
      last_y = y

  flag.close()

  flag_img = pygame.image.load('Flag.png')

  # Grab the last color band
  color_bands.append(ColorBand(last_color, y-last_y+1))

  pygame.init()
  size = win_width, win_height = width + 200, height
  screen = pygame.display.set_mode(size)

  sort_gen = quick_sort_generator(color_bands, 0, len(color_bands)-1)

  done = False
  while not done:

    # PyGame quit code from https://stackoverflow.com/questions/15214727/exiting-pygame-window-on-click
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          done = True
          break
      elif event.type == pygame.QUIT:
        done = True
        break
    if done:
      break  # to break out of the while loop

    screen.fill((0, 0, 0))

    try:
      next(sort_gen)
    except StopIteration:
      pass

    y = 0
    for band in color_bands:
      band.draw_rect(y, width, screen)
      y += band.height

    # Draw European Flag
    screen.blit(flag_img, (0, 0), area=pygame.Rect(0, 0, 322, 228))

    pygame.display.flip()

    time.sleep(0.03)
