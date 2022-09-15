from PIL import Image
from flower import Flower
from utils import *
import image_utils



START_FLOWER=[[((256, 91), 96), ((107, 119), 72)], [((722, 128), 82), ((536, 110), 110)], [((984, 125), 64), ((1179, 98), 100)], [((112, 352), 136), ((288, 374), 70)], [((964, 357), 120), ((1106, 337), 72)], [((190, 610), 92), ((325, 609), 112)], [((621, 623), 66), ((717, 578), 60)], [((947, 573), 78), ((1090, 613), 100)]]

@timer()
def main():
    remove_directory_file("images")
    
    generate_images()
    
    generate_video(get_path()+'/images/%d.png','output/flowers.mp4',30)

def generate_images():
    background = Image.open("assets/background.png")
    # image_utils.drawable_areas_new_image(background).save("assets/background_test.png")

    flower_list = create_starting_flower()
    #flower_list = create_flower_from_list(START_FLOWER)

    image_utils.generate_animations(background,flower_list,15)
    

def create_starting_flower():
    drawable_areas = image_utils.compute_drawable_areas()
    n_flower = 2
    flower_list=[]
    
    for area in drawable_areas:
        new_flowers = []    
        image_utils.generate_flowers(area, n_flower, new_flowers)
        image_utils.add_image(new_flowers)
        flower_list.append(new_flowers)
    return flower_list


def create_flower_from_list(position_list):
    flower_list = []
    for area in position_list:
        area_flower=[]
        for flower in area:
            area_flower.append(Flower(flower[0],flower[1]))
        image_utils.add_image(area_flower)
        flower_list.append(area_flower)
    
    return flower_list

def create_list_from_flower(flower_list):
    position_list= []
    for area in flower_list:
        position_area=[]
        for flower in area:
            position_area.append((flower.position,flower.size))
        position_list.append(position_area)

    return position_list





if __name__ == "__main__":
    main()

