from PIL import Image, ImageDraw,ImageFont
from io import BytesIO
from django.shortcuts import HttpResponse,render
import random
import os
def get_valid_img(request):

    # 生成随机颜色
    def get_random_color():
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    image = Image.new("RGB", (200, 35), get_random_color())

    # 生成随机字符
    draw = ImageDraw.Draw(image)
    #font = ImageFont.truetype("./static/font/kumo.ttf", size=25)
    #print(font,"font")
    temp = []
    for i in range(5):
        random_num = str(random.randint(0, 9))
        random_low = chr(random.randint(97, 122))
        random_upper_alpha = chr(random.randint(65, 90))
        random_char = random.choice([random_num, random_low, random_upper_alpha])
        draw.text((30 + i * 30, 3), random_char, get_random_color())

        temp.append(random_char)


        # 噪点噪线
        width=100
        height=40
        for i in range(1):
            x1=random.randint(0,width)
            x2=random.randint(0,width)
            y1=random.randint(0,height)
            y2=random.randint(0,height)
            draw.line((x1,y1,x2,y2),fill=get_random_color())

        for i in range(1):
            draw.point([random.randint(0, width), random.randint(0, height)], fill=get_random_color())
            x = random.randint(0, width)
            y = random.randint(0, height)
            draw.arc((x, y, x + 4, y + 4), 0, 90, fill=get_random_color())

    # 在内存中生成图片
    path = os.path.dirname(os.path.abspath(__file__))
    print(path)
    with open(path+"/../statics/images/valid.png","wb") as f:
        image.save(f, "png")

    temp_str = "".join(temp)
   # 存入session中方便在其他视图函数中验证 
    return temp_str
