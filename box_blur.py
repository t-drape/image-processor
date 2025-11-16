import numpy as np

import shared


def sum_color_values(c_values: dict) -> list[int, int, int]:
    """Sum the color values in the input dictionary"""
    for key, value in c_values.items():
      c_values[key] = np.sum(value)
    return c_values

def calculate_blur_values(pixels: list[list[int]], is_color=True) -> list[int,int,int]:
    """Return calculated blur value(s)"""
    num_used_values = np.int64(len(pixels))
    if is_color:
      # red_values, green_values, blue_values = [], [], []
      # for pixel in pixels:
      #     red_values.append(pixel[2])
      #     green_values.append(pixel[1])
      #     blue_values.append(pixel[0])
      c_values = sum_color_values(shared.color_values(pixels))
      # Fixed the largest issue! Instead of using the built-in python sum function
      # Use the Numpy sum function. This resolved the Runtime Warning for Overflow
      calculated_blur_red = (c_values["red"] / num_used_values)
      # Green
      calculated_blur_green = (c_values["green"] / num_used_values)
      # Blue
      calculated_blur_blue = (c_values["blue"] / num_used_values)
      return [calculated_blur_blue, calculated_blur_green, calculated_blur_red]
    else:
      #Use this for grayscale
      return (np.sum(pixels) / num_used_values)

def blur(kernel_size, blurred_image, image):
  height = len(image)
  for height_index, pixel_array in enumerate(image):
        width = len(pixel_array)
        for width_index, pixel_value in enumerate(pixel_array):
          bbv = shared.get_indices(kernel_size, height_index, width_index)
          bp = shared.filter_pixels(height, width, bbv, blurred_image)
          if len(bp) != 0:
            # Set image
            blurred_image[height_index][width_index] = calculate_blur_values(bp)

  return blurred_image