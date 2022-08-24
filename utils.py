from PIL import Image
from copy import deepcopy

def resize_image(image, new_width, new_height):
    image.thumbnail((new_width, new_height), Image.ANTIALIAS)

def resize_new_image(image, new_width, new_height):
    new_image = deepcopy(image)
    new_image.thumbnail((new_width, new_height), Image.ANTIALIAS)
    return new_image

def paste_image(upper_image, lower_image, w, h):
    lower_image.paste(upper_image, (w, h))

def paste_new_image(upper_image, lower_image, w, h):
    new_lower_image = deepcopy(lower_image)
    new_lower_image.paste(upper_image, (w, h), upper_image)
    return new_lower_image

def rotate_new_image(image, degree):
    return image.rotate(degree)