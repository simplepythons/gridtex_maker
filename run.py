import sys, math
from PIL import Image, ImageDraw, ImageFont

args = []
size_level = 6
input_dir = ""
output_path = "hoge.png"

MAX_IMAGE_SIZE = 1024 * 4
RECT_SIZE = 29
BACK_COLOR = (255, 255, 255)

def rectTest():
    img = Image.new('RGB', (MAX_IMAGE_SIZE, MAX_IMAGE_SIZE), color=BACK_COLOR)
    img.putalpha(255)

    rect_height = RECT_SIZE * int(math.pow(2.0, size_level - 1))
    print(rect_height)
    rect_width = int( (3 + math.sqrt(2)) * rect_height )
    print(rect_width)

    fnt = ImageFont.truetype('YuGothM.ttc', int(rect_height * 0.7))
    draw = ImageDraw.Draw(img)

    rn = int(math.pow(2.0, 6.0 - size_level))
    xn = int(MAX_IMAGE_SIZE / rn)
    yn = int(math.floor(MAX_IMAGE_SIZE / rect_height))

    for y in range(yn):
        for x in range(xn):
            for r in range(3):
                draw.rectangle((x * rect_width + rect_height * r, y * rect_height, (x + 1) * rect_width + rect_height * r, (y + 1) * rect_height), fill=BACK_COLOR, outline=(0, 0, 0))
                draw.text((x * rect_width + rect_height * r + int(rect_height * 0.1), y * rect_height + int(rect_height * 0.1)), str(y + x * yn), font=fnt, fill=(0, 0, 0))
            draw.rectangle((x * rect_width + rect_height * 3, y * rect_height, (x + 1) * rect_width + rect_height, (y + 1) * rect_height), fill=BACK_COLOR, outline=(0, 0, 0))
    img.save(output_path)
    print("saved path = " + output_path)

def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()

if __name__ == '__main__':
    args = sys.argv
    if 4 <= len(args):
        if(is_integer(args[1])):
            size_level = int(args[1])
            input_dir = args[2]
            output_path = args[3]
            rectTest()
        else:
            print('invalid args format : $1 is not integer.')
    else:
        print('invalid args format : arguments are too short')