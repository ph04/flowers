from random import random
from PIL import Image
import utils




def main():
    utils.remove_directory_file("images")
    
    generate_images()
    
    # utils.generate_video('images/*.png','output/flowers.mp4',30)


def generate_images():
    background = Image.open("assets/BG_test.png")
    
    flower_list = create_starting_flower()

    drow_flowers(background,flower_list)
    
    background.show()
    
    # background = utils.drowable_areas_new_image(background)
    
    # background.save("images/BG_test.png")

def create_starting_flower():
    drowable_areas = utils.compute_drowable_areas()
    n_flawer = 4
    flower_list=[]
    
    for area in drowable_areas:
        area_flower_list=[]    
        for _ in range(n_flawer):
            area_flower_list.append(utils.random_flower(area,area_flower_list))
        flower_list.extend(area_flower_list)
        
    return flower_list

def drow_flowers(background,flower_list):
    for flower in flower_list:
        utils.paste_image(flower.image,background,flower.position)
        



if __name__ == "__main__":
    main()