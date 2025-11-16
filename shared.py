import os
import tkinter as tk
from tkinter import filedialog

from math import floor


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

def filter_pixels(height, width, box_blur_values: list[list[int]], image: list[list[int]]) -> list[list[int]]:
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