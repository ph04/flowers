import copy
from PIL import Image
import random
from utils import *


IMAGE_NAME={"Blue","Orange","Pink","Purple","Red"}
IMAGE_DICT={color : Image.open("assets/Flower "+ color +".png") for color in IMAGE_NAME}


class Flower:
    def __init__(self, position, size):
        self.original_image = None
        self.image = None
        self.image_name = None
        self.position = position
        self.size = size
        self_half_size = self.size / 2
        self.center = (self.position[0] + self_half_size / 2, self.position[1] + self_half_size / 2)
        self.half_diagonal = 0.75 * self.size
        # self.diagonal = 1.41421356237 * self.size
        # self.half_diagonal = 0,707106781185 * self.size
        
    def overlap(self, other_center, other_half_diagonal):
        distance = compute_distance(self.center, other_center)

        # print(distance,self.half_diagonal + other_half_diagonal)
        return distance <= self.half_diagonal + other_half_diagonal 
    
    def chose_image(self,color_set):

        name= random.choice(list(IMAGE_NAME-color_set))
            
        self.original_image= IMAGE_DICT[name]
        self.image_name= name
        self.resize_image()
        return self.image_name
    
    def set_size(self,size):
        self.size=size
        self.resize_image()
    
    def resize_image(self):
        self.image = resize_new_image(self.original_image,self.size,self.size)
        
    def change(self,step):
        self.set_size(self.size+step)
        self.change_position(-step//2)
        
    def change_position(self,step):
        self.position=(self.position[0]+step,self.position[1]+step)
    
    def __repr__(self) -> str:
        return f"{self.image_name}"