from random import random
from PIL import Image
import utils
import flower



def main():
    utils.remove_directory_file("images")
    
    generate_images()
    
    # utils.generate_video('images/*.png','output/flowers.mp4',30)


def generate_images():
    background = Image.open("assets/BG2.png")
    
    flower_list = create_starting_flower()

    drow_flowers(background,flower_list)
    
    background.show()
    
    # background = utils.drowable_areas_new_image(background)
    
    # background.save("images/BG_test.png")

def create_starting_flower():
    drowable_areas = utils.compute_drowable_areas()
    n_flower = 2
    flower_list=[]
    
    for area in drowable_areas:
        new_flowers = []

        utils.generate_flowers(area, n_flower, new_flowers)
        print(True)
        flower_list.append(new_flowers)
        
    return flower_list

def drow_flowers(background,flower_list):
    for area in flower_list:
        for flower in area:
            utils.paste_image(flower.image,background,flower.position)
        
        



if __name__ == "__main__":
    main()