import copy
from PIL import Image
import random
import utils


IMAGE_LIST=[Image.open("assets/Flower "+ color +".png") for color in ["Blue","Orange","Pink","Purple","Red"]]
background = Image.open("assets/BG2.png")

class Flower:
    def __init__(self, image, position, size):
        self.image = image
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
        image = random.choice(IMAGE_LIST)
        self.image=image
        self.resize_image()
            
    
    def resize_image(self):
        utils.resize_image(self.image,self.size,self.size)
        

    def __repr__(self) -> str:
        return f"Flower"