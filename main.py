import cv2 as cv

import shared
import box_blur
import pixelate
# 0 imports the image in grayscale

def main():
    """A photo editing program written in Python, automatically box blurs the given image"""
    file_path = shared.find_image()
    if file_path:
      print(f"Selected File: {file_path}")
      image = cv.imread(file_path)
      blurred_image = image.copy()
      pixelated_image = image.copy()
      blurred_image = box_blur.blur(blurred_image, image)
      pixelated_image = pixelate.pixelated(pixelated_image, image)
      new_file_path_blurred = file_path[:-4] + "_blurred" + file_path[-4:]
      new_file_path_pixelated = file_path[:-4] + "_pixelated" + file_path[-4:]
      print(f"Your Blurred Image: {new_file_path_blurred}")
      print(f"Your Pixelated Image: {new_file_path_pixelated}")
      print(cv.imwrite(new_file_path_blurred, blurred_image))
      print(cv.imwrite(new_file_path_pixelated, pixelated_image))
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