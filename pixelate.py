from math import floor
import numpy as np

import shared
from box_blur import calculate_blur_values


def pixelated(pixelated_image, image, is_color=True):
  """Perform box blur on given image without changing original image"""
  height = len(image)
  width = len(image[0])
  kernel = list(map(lambda x: 3+x, shared.calculate_kernel_size(height, width)))
  for height_index in range(floor(kernel[0] / 2), height, kernel[0]):
      for width_index in range(floor(kernel[1] / 2), width, kernel[1]):
          pixelated_values = shared.get_indices(kernel, height_index, width_index)
          final_pixels = shared.filter_pixels_return_indices(height, width, pixelated_values, pixelated_image)
          value = calculate_blur_values([image[x][y] for x,y in final_pixels], is_color)
          for x, y in final_pixels:
              pixelated_image[x][y] = value

          # shared_value = np.sum(pixels) / len(pixels)
  return pixelated_image