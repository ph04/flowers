import copy
from PIL import Image
import random
import utils


IMAGE_LIST=[(Image.open("assets/Flower "+ color +".png"),color) for color in ["Blue","Orange","Pink","Purple","Red"]]
background = Image.open("assets/BG2.png")

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
        distance = utils.compute_distance(self.center, other_center)

        # print(distance,self.half_diagonal + other_half_diagonal)
        return distance <= self.half_diagonal + other_half_diagonal 
    
    def chose_image(self):
        img = random.choice(IMAGE_LIST)
        self.original_image=img[0]
        self.image_name=[1]
        self.resize_image()
            
    def set_size(self,size):
        self.size=size
        self.resize_image()
        
    def resize_image(self):
        self.image = utils.resize_new_image(self.original_image,self.size,self.size)
        
    def change(self,step):
        self.set_size(self.size+step)
        self.change_position(-step//2)
        
    def change_position(self,step):
        self.position=(self.position[0]+step,self.position[1]+step)
    
    def __repr__(self) -> str:
        return f"{self.image_name}"