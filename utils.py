from PIL import Image, ImageDraw
from copy import deepcopy
from os import remove
from glob import glob
import random
import ffmpeg
import math

from flower import Flower

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
            .input(images_path, pattern_type='glob', framerate=framerate)
            .output(output_path)
            .run()
    )

def remove_directory_file(folder):
    files = glob(folder+"/*")
    for file in files:
        remove(file)
        



IMAGE_ZONES= [
        ((0,0),(644,381))   ,((645,0),(1280,381)),((1281,0),(1919,381)),
        ((0,382),(644,759)),((1281,382),(1919,759)),
        ((0,760),(644,1079)),((645,760),(1280,1079)),((1281,760),(1919,1079))]   

BORDER_WIDTH = 40

IMAGE_LIST=[Image.open("assets/Flower "+ color +".png") for color in ["Blue","Orange","Pink","Purple","Red"]]

def drowable_areas_new_image(image):

    color = [0,1,0,1,1,0,1,0]

    new_image = deepcopy(image)
    draw = ImageDraw.Draw(new_image)
                                                        
    for i,zone in enumerate(IMAGE_ZONES):
        draw.rectangle(zone,outline="red" if color[i] else "blue")
    
    for area in compute_drowable_areas():
        draw.rectangle(area,outline="green")
        
    return new_image

def compute_drowable_areas():
    return [((zone[0][0]+BORDER_WIDTH,zone[0][1]+BORDER_WIDTH),(zone[1][0]-BORDER_WIDTH,zone[1][1]-BORDER_WIDTH)) for zone in IMAGE_ZONES]


    
def generate_flowers(area,n_flowers,new_flowers):
    if n_flowers == len(new_flowers):
        return

    new_flower = random_flower(area, new_flowers, n_flowers)

    if new_flower == None:
        new_flowers.pop()
    else:
        new_flowers.append(new_flower)

    generate_flowers(area, n_flowers, new_flowers)

def random_flower(area,other_flowers, n_flowers) -> Flower:
    
    min_max_dimension=(80,230)
    
    size = random.randint(min_max_dimension[0],min_max_dimension[1]) 
    
    coordinates=random_cordinates(area,size,other_flowers)

    if coordinates:
        # for 
        image = random.choice(IMAGE_LIST)
        
        n = 0

        while True:
            if all(map(lambda flower: flower != image, other_flowers)):
                break
            else:
                image = random.choice(IMAGE_LIST)
            
            if n == n_flowers:
                return None
            
            n += 1

        resize_image(image,size,size)
        
        return Flower(image,coordinates, size)

def random_cordinates(area,size,other_flowers):
    
    half_size=size//2 +1
    
    n_loop = 0
    overlap = True
    
    while overlap :
        coordinates = (random.randint(area[0][0]+half_size,area[1][0]-half_size),
                    random.randint(area[0][1]+half_size,area[1][1]-half_size))

        overlap = check_overlap(coordinates,size,other_flowers)
        
        # print(overlap)

        if n_loop == 1000:
            # print(False)
            return None
        n_loop += 1
        
    return coordinates

def compute_distance(point1, point2):
    return math.dist(point1,point2)

def check_overlap(coordinates,size,other_flowers):
    other_half_size = size / 2
    other_center = (coordinates[0] + other_half_size, coordinates[1] + other_half_size)
    other_half_diagonal = 0.75 * size
    
    for flower in other_flowers:
        if flower.overlap(other_center, other_half_diagonal):
            return True
    
    return False