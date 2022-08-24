import utils
from PIL import Image
import ffmpeg

def main():
    background = Image.open("assets/BG2.png")
    red_flower = Image.open("assets/Flower Red.png")

    (
        ffmpeg
            .input('outputs/*.png', pattern_type='glob', framerate=30)
            .output('flowers.mp4')
            .run()
    )

if __name__ == "__main__":
    main()