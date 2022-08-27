import ffmpeg
import math
from PIL import Image
from copy import deepcopy
from os import remove
from glob import glob


def resize_image(image, new_width, new_height):
    image.thumbnail((new_width, new_height), Image.ANTIALIAS)

def resize_new_image(image, new_width, new_height):
    new_image = deepcopy(image)
    new_image.thumbnail((new_width, new_height), Image.ANTIALIAS)
    return new_image

def paste_image(upper_image, lower_image, position):
    lower_image.paste(upper_image, position,  upper_image)

def paste_new_image(upper_image, lower_image, position):
    new_lower_image = deepcopy(lower_image)
    new_lower_image.paste(upper_image, position, upper_image)
    return new_lower_image

def rotate_new_image(image, degree):
    return image.rotate(degree)

def generate_video(images_path,output_path,framerate=30):
    (
        ffmpeg
            .input(images_path, framerate=framerate )
            .output(output_path, level ="3.0",
                    **{'profile:v': "baseline"},
                    preset="slow" ,
                    **{"c:v" :"libx264"},
                    **{"c:a" :"aac"},
                    pix_fmt = "yuv420p")
            .run(overwrite_output=True)
    )

def get_path():
    import os
    dirname, filename = os.path.split(os.path.abspath(__file__))
    print(dirname)
    return dirname

def remove_directory_file(folder):
    files = glob(folder+"/*")
    for file in files:
        remove(file)

def compute_distance(point1, point2):
    return math.dist(point1,point2)