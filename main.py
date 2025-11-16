import sys

import cv2 as cv

import numpy as np

HEIGHT = 427
WIDTH = 640


def rid_sludge(pixel: list[int]) -> list[int]:
  """Find out of range numbers"""
  return (pixel[0] < HEIGHT) and (pixel[1] < WIDTH) and (pixel[0] >= 0) and (pixel[1] >= 0)

# 0 imports the image in grayscale
image = cv.imread("car.jpg")
cv.imwrite("original.jpg", image)
blurred_image = image.copy()
# Now perform a blur on the image
# A box blur uses an average of the kernel size for the given pixel
# Height = len(image)
# Width = len(image[x]), where x is any index in the range of 0 to height-1
height = len(image)
for height_index, pixel_array in enumerate(image):
  width = len(pixel_array)
  for width_index, pixel_value in enumerate(pixel_array):
    box_blur_values = [#[height_index-2, width_index-1], [height_index-2, width_index], [height_index-2, width_index+1],
                       [height_index-1, width_index-1], [height_index-1, width_index], [height_index-1, width_index+1],
                       [height_index, width_index-1], [height_index, width_index], [height_index, width_index+1],
                       [height_index+1, width_index-1], [height_index+1, width_index], [height_index+1, width_index+1],
                      #  [height_index+2, width_index-1], [height_index+2, width_index], [height_index+2, width_index+1]
                       ]
    filtered_values = list(filter(rid_sludge, box_blur_values))
    box_pixels = [blurred_image[pixel[0]][pixel[1]] for pixel in filtered_values]
    if len(filtered_values) != 0:
      # Use this for grayscale
      # calculated_blur = (sum(box_pixels) / len(filtered_values))
      # blurred_image[height_index][width_index] = calculated_blur

      # Now, with color, each value is a 3 elt array, in BGR format
      # Red value
      red_values, green_values, blue_values = [], [], []
      division_value = np.int64(len(filtered_values))
      for pixel in box_pixels:
        red_values.append(pixel[2])
        green_values.append(pixel[1])
        blue_values.append(pixel[0])
        # Fixed the largest issue! Instead of using the built-in python sum function
        # Use the Numpy sum function. This resolved the Runtime Warning for Overflow
      calculated_blur_red = (np.sum(red_values) / division_value)
      # Green
      calculated_blur_green = (np.sum(green_values) / division_value)
      # Blue
      calculated_blur_blue = (np.sum(blue_values) / division_value)
      # Set image
      blurred_image[height_index][width_index] = [calculated_blur_blue, calculated_blur_green, calculated_blur_red]





print(cv.imwrite("blurred.jpg", blurred_image))
print(cv.imwrite("original.png", image))

