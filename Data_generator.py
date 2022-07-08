from JMSSGraphics import *
import pickle
import os

jmss = Graphics(width = 350, height = 350, title = "O", fps = 60)

n = 8
side_length = 32
margin = 8
border = 16

pressed = False

pixels = [0] * n * n
data_list = []

delete = input("Do want to make a new data set (1) or add to the existing one(if there is one)(2): ")
if delete == "1" and os.path.exists("training_data"):
    os.remove("training_data")
else: 
    with open ('training_data', 'rb') as fp:
        data_list = pickle.load(fp)

@jmss.mainloop
def Game():
    global pixels, pressed, data_list
    jmss.clear()

    mouse_pos = jmss.getMousePos()
    x = (mouse_pos[0] - border) // (side_length + margin)
    y = (mouse_pos[1] - border) // (side_length + margin)

    if jmss.isMousePressed(MOUSE_BUTTON_LEFT) and not pressed:
        if not(x < 0 or x >= n or y < 0 or y >= n):
            pixels[y * n + x] = 1

    if jmss.isKeyDown(KEY_SPACE):
        pressed = True

    if pressed:
        jmss.drawText("Press X if it a X or O if it is a O",0,0)
        xPressed = jmss.isKeyDown(KEY_X)
        yPressed = jmss.isKeyDown(KEY_O)
        if xPressed or yPressed:
            end = [1] if xPressed else [0]
            print("new data point: " + str(pixels))
            data_list.append(pixels + end)
            with open('training_data', 'wb') as fp:
                pickle.dump(data_list, fp)
            pixels = [0] * n * n
            pressed = False

    for x in range(n):
        for y in range(n):
            jmss.drawRect(border + x * (side_length + margin), \
                          border + y * (side_length + margin), \
                          border + x * (side_length + margin) + side_length, \
                          border + y * (side_length + margin) + side_length, \
                          r = pixels[y * n + x], \
                          b = 1 - pixels[y * n + x], \
                          g = 0)
                            

jmss.run()
