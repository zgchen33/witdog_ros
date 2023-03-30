import sensor
import image
import lcd
import time

clock = time.clock()
lcd.init(type=1, freq=15000000, color=lcd.BLACK, invert = 0, lcd_type = 0)
lcd.rotation(3)
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.set_hmirror(1) #设置摄像头镜像
sensor.set_vflip(1)   #设置摄像头翻转
sensor.run(1)
sensor.skip_frames(30)

while True:
    clock.tick() #记录时刻，用于计算帧率
    img = sensor.snapshot()
    res = img.find_qrcodes()
    if len(res) > 0:
        img.draw_string(2,2, res[0].payload(), color=(0,128,0), scale=2)
        print(res[0].payload())
    lcd.display(img)
