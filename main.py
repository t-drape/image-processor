
import os
import tkinter as tk
from tkinter import filedialog

from math import floor


import cv2 as cv
import numpy as np





def rid_sludge(pixel: list[int], height, width) -> list[int]:
  """Find out of range numbers"""
  return (pixel[0] < height) and (pixel[1] < width) and (pixel[0] >= 0) and (pixel[1] >= 0)

def read_image(image_path: str) -> list[list[int]]:
  """Read image into program"""
  return cv.imread(image_path)

def box_blur(image: list[list[int]]) -> list[list[int]]:
  """Blur the input image using box blur"""

def get_indices(kernel: tuple[int], height_index: int, width_index: int) -> list[list[int]]:
    """Find all neighboring pixels within the kernel size"""
    box_blur_values = []
    # Define the starting point, the middle of the range
    starting_spot_height_middle = floor(kernel[0] / 2)
    starting_spot_width_middle = floor(kernel[1] / 2)

    for height in range (kernel[0]):
        for width in range(kernel[1]):
            box_blur_values.append([height_index-(starting_spot_height_middle-height), width_index-(starting_spot_width_middle-width)])
    return box_blur_values

def filter_pixels(filter_func, height, width, box_blur_values: list[list[int]], image: list[list[int]]) -> list[list[int]]:
   """Filter out indexes not in image, Grab pixels from image"""
   filtered_values = list(filter(lambda pixel: (pixel[0] < height) and (pixel[1] < width) and (pixel[0] >= 0) and (pixel[1] >= 0), box_blur_values))
   return [image[pixel[0]][pixel[1]] for pixel in filtered_values]

def color_values(pixels: list[list[int]]) -> dict:
    """Sum the Blue, Green, and Red values in the box blur pixels"""
    c_values = {"red": [], "blue": [], "green": []}
    for pixel in pixels:
        c_values["red"].append(pixel[2])
        c_values["green"].append(pixel[1])
        c_values["blue"].append(pixel[0])
    return c_values

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
      c_values = sum_color_values(color_values(pixels))
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
# 0 imports the image in grayscale

def find_image() -> str:
  """Allow the user to pick the image to edit"""
  root = tk.Tk()
  root.withdraw()
  desktop = os.path.expanduser("~/Desktop")
  file_path = filedialog.askopenfilename(
    initialdir=desktop,
    title="Select a photo file to edit",
    filetypes=(("JPEG files", "*.jpg"), ("PNG files", "*.png"))
  )
  return file_path


def main():
    """A photo editing program written in Python, automatically box blurs the given image"""
    file_path = find_image()
    if file_path:
      print(f"Selected File: {file_path}")
      image = cv.imread(file_path)
      blurred_image = image.copy()
      height = len(image)
      kernel_size = (5, 3)
      for height_index, pixel_array in enumerate(image):
        width = len(pixel_array)
        for width_index, pixel_value in enumerate(pixel_array):
          bbv = get_indices(kernel_size, height_index, width_index)
          bp = filter_pixels(rid_sludge, height, width, bbv, blurred_image)
          if len(bp) != 0:
            # Set image
            blurred_image[height_index][width_index] = calculate_blur_values(bp)
      new_file_path = file_path[:-4] + "_blurred" + file_path[-4:]
      print(f"Your Image: {new_file_path}")
      print(cv.imwrite(f"{file_path + "_blurred"}.jpg", blurred_image))
    else:
      print("No Image Selected, please try again.")
# Now perform a blur on the image
# A box blur uses an average of the kernel size for the given pixel
# Height = len(image)
# Width = len(image[x]), where x is any index in the range of 0 to height-1
if __name__ == "__main__":
   main()

# file_path = find_image()
# if file_path:
#   print(f"Selected File: {file_path}")
#   image = cv.imread(file_path)
#   blurred_image = image.copy()
#   HEIGHT = len(image)
#   kernel_size = (5, 3)
#   for height_index, pixel_array in enumerate(image):
#     WIDTH = len(pixel_array)
#     for width_index, pixel_value in enumerate(pixel_array):
#       bbv = get_indices(kernel_size, height_index, width_index)
#       bp = filter_pixels(rid_sludge, bbv, blurred_image)
#       if len(bp) != 0:
#         # Set image
#         blurred_image[height_index][width_index] = calculate_blur_values(bp)
# new_file_path = file_path[:-4] + "_blurred" + file_path[-4:]
# print(f"Your Image: {new_file_path}")
# print(cv.imwrite(new_file_path, blurred_image))