from PIL import Image, ImageDraw, ImageFont, ImageFilter

import random

# 随机字母数字:

def rndChar():
    STR = random.choice([chr(i) for i in range(65, 91)])  # 随机选取A-Z
    str = random.choice([chr(i) for i in range(97, 123)])  # a-z
    number = random.choice([chr(i) for i in range(48, 58)])  # 0-9
    return random.choice([STR,str,number])


# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

# 240 x 60:
width = 45 * 6
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象:
font = ImageFont.truetype('Andale Mono.ttf', 36)
#font = ImageFont.truetype('Arial Narrow.ttf', 36)
# 创建Draw对象:
draw = ImageDraw.Draw(image)
# 填充每个像素:
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())


#定义验证码保存字符型变量'code'
code=''
# 输出文字:
for t in range(6):
    codechar=rndChar()
    draw.text((40 * t + 10, 10), codechar, font=font, fill=rndColor2())
    code=str(code)+str(codechar)

print(code)


# 模糊:(按自己需要选择注释或启用模糊滤镜效果)
image = image.filter(ImageFilter.BLUR)


image.save('code.jpg', 'jpeg')
