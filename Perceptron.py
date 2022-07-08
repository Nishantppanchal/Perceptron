from JMSSGraphics import *
from fperceptron import *
import pickle

# loads the list from the data file
with open ('weights_data', 'rb') as fp:
    weights = pickle.load(fp)

jmss = Graphics(width = 350, height = 350, title = "Xs or Os", fps = 60)

n = 8
side_length = 32
margin = 8
border = 16

pixels = [0] * n * n

displayPrediction = False
prediction = None


@jmss.mainloop
def Game():
    global pixels, displayPrediction, prediction
    jmss.clear()

    if jmss.isKeyDown(KEY_BACKSPACE):
        pixels = [0] * n * n
        displayPrediction = False
        prediction = None

    mouse_pos = jmss.getMousePos()
    x = (mouse_pos[0] - border) // (side_length + margin)
    y = (mouse_pos[1] - border) // (side_length + margin)

    if jmss.isMousePressed(MOUSE_BUTTON_LEFT) and not displayPrediction:
        if not(x < 0 or x >= n or y < 0 or y >= n):
            pixels[y * n + x] = 1

    if jmss.isKeyDown(KEY_ENTER):
        prediction = perceptron(pixels, weights)
        displayPrediction = True
    
    if displayPrediction: 
        if prediction == 1:
            jmss.drawText("It a X!",0,0)
        if prediction == 0:
            jmss.drawText("It is a O!",0,0)
    else: 
        jmss.drawText("Press enter to show prediction and press backspace to clear pixels",0,0)
        
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
