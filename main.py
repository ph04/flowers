from PIL import Image
import utils
import image_utils

def main():
    utils.remove_directory_file("images")
    
    generate_images()
    
    utils.generate_video(utils.get_path()+'/images/%d.png','output/flowers.mp4',30)

def generate_images():
    background = Image.open("assets/BG2.png")
    
    flower_list = create_starting_flower()

    start_image = image_utils.drow_flowers(background,flower_list)
    # start_image.save("images/BG_test.png")
    
    image_utils.generate_animation(background,flower_list,1)
    
    # background.show()

def create_starting_flower():
    drowable_areas = image_utils.compute_drowable_areas()
    n_flower = 2
    flower_list=[]
    
    for i,area in enumerate(drowable_areas):
        new_flowers = []    
        image_utils.generate_flowers(area, n_flower, new_flowers)
        image_utils.add_image(new_flowers)
        flower_list.append(new_flowers)
        
        # print(f"Area {i+1} completa")

    return flower_list


        
if __name__ == "__main__":
    import timeit

    start = timeit.default_timer()

    main()

    stop = timeit.default_timer()

    print('Time: ', stop - start)  

