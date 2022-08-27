import math
from queue import Empty
from re import I
from tokenize import Imagnumber
from PIL import  ImageDraw
from copy import deepcopy
import random
from flower import Flower
import utils

IMAGE_ZONES= [
        ((0,0),(644,381))   ,((645,0),(1280,381)),((1281,0),(1919,381)),
        ((0,382),(644,759)),((1281,382),(1919,759)),
        ((0,760),(644,1079)),((645,760),(1280,1079)),((1281,760),(1919,1079))]   

BORDER_WIDTH = 50

IMAGE_NUMBER=0

ANIMATION_STEP=2

FPS=30

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

def random_flower(area,other_flowers, n_flowers):
    
    min_max_dimension=(40,100)
    
    size = random.randint(min_max_dimension[0],min_max_dimension[1]) *2
    
    coordinates=random_cordinates(area,size,other_flowers)

    if coordinates:
        return Flower(coordinates,size)
            
def random_cordinates(area,size,other_flowers):
    
    half_size=size//2 +1
    
    n_loop = 0
    
    minX, maxX = area[0][0]+half_size,area[1][0]-half_size
    minY, maxY = area[0][1]+half_size,area[1][1]-half_size
    
    overlap = True
    while overlap :
        coordinates = (random.randint(minX,maxX),random.randint(minY,maxY))

        overlap = check_overlap(coordinates,size,other_flowers)
        
        if n_loop == 500: return None
        
        n_loop += 1
        
    return coordinates

def check_overlap(coordinates,size,other_flowers):
    other_half_size = size / 2
    other_center = (coordinates[0] + other_half_size, coordinates[1] + other_half_size)
    other_half_diagonal = 0.75 * size
    
    for flower in other_flowers:
        if flower.overlap(other_center, other_half_diagonal):
            return True
    
    return False

def add_image(flowers):
    for flower in flowers:
        flower.chose_image()
        
def drow_flowers(background,flower_list):
    background= deepcopy(background)
    for area in flower_list:
        for flower in area:
            utils.paste_image(flower.image,background,flower.position)
    
    return background

def drow_flower(background,flower):
    background= deepcopy(background)
    utils.paste_image(flower.image,background,flower.position)
    return background

def generate_animation(background,flower_list,duration):
    global IMAGE_NUMBER
    
    grow_flower_area,drop_flower_area = -1,-1
    
    while grow_flower_area == drop_flower_area:
        grow_flower_area = random.randint(0,len(flower_list)-1)
        drop_flower_area = random.randint(0,len(flower_list)-1)
    
    
    grow_flower = flower_list[grow_flower_area].pop(0)
    drop_flower = flower_list[drop_flower_area].pop(0)
    
    new_bg = drow_flowers(background,flower_list)
    
    empty_frame = compute_empty_frame(grow_flower.size,drop_flower.size,duration)

    grow_flower_size = grow_flower.size
    grow_flower.size=0
    
    frame = drow_flower(new_bg,drop_flower)
    frame.save(f"images/{IMAGE_NUMBER}.png")
    IMAGE_NUMBER+=1


    while grow_flower.size < grow_flower_size or drop_flower.size > 0:
        print(f"Image {IMAGE_NUMBER}")

        for _ in range(empty_frame):
            frame.save(f"images/{IMAGE_NUMBER}.png")
            IMAGE_NUMBER+=1
        
        if grow_flower.size + ANIMATION_STEP < grow_flower_size: 
            frame = flower_animation(new_bg,grow_flower,ANIMATION_STEP)
        else:
            grow_flower.set_size(grow_flower_size)
        
        if drop_flower.size -ANIMATION_STEP > 0:
            frame = flower_animation(frame,drop_flower,-ANIMATION_STEP)
            
        else:
            drop_flower.size = 0
        
  
        frame.save(f"images/{IMAGE_NUMBER}.png")
        IMAGE_NUMBER+=1
        

def flower_animation(background,flower,step):
    flower.change(step)
    new_bg= drow_flower(background,flower)
    return new_bg

def compute_empty_frame(size1,size2,duration):
    max_size= max(size1,size2)

    animation_frame = max_size // ANIMATION_STEP

    duration_frame =  duration * FPS

    duration_diff= duration_frame - animation_frame 

    empty_frame = duration_diff // animation_frame
    return empty_frame
    
    
    