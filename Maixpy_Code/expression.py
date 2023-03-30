import sensor,image,lcd  # import 相关库
import time
import os

lcd.init() # 初始化lcd

#img0 = image.Image("/sd/dog/dogface_00000.jpg")
#img1 = image.Image("/sd/dog/dogface_00026.jpg")
#img2 = image.Image("/sd/dog/dogface_00027.jpg")
#img3 = image.Image("/sd/dog/dogface_00028.jpg")

while(1):
    for i in range(0, 55):
        if i == 26 or i == 30:
            img = image.Image("/sd/dog/dogface_00026.jpg")
            lcd.display(img)
        elif i == 27 or i == 29:
            img = image.Image("/sd/dog/dogface_00027.jpg")
            lcd.display(img)
        elif i == 28:
            img = image.Image("/sd/dog/dogface_00028.jpg")
            lcd.display(img)
        else:
            img = image.Image("/sd/dog/dogface_00000.jpg")
            lcd.display(img)
