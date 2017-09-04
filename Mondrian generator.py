#--------------Mondrian generator--------------#
#-------Copyright Suran & van Dooren 2017------#

#the program creates Mondrian pattern images of size 400x400 pixels

#import libraries
from psychopy import os, visual, core, event
import random
from PIL import ImageGrab

#parameters
number_of_images = 5
round_shape = 1
shape_size = 1

#create Images folder
if not os.path.exists("Images"):
    os.makedirs("Images")

#create window
win = visual.Window(fullscr = 0, units="pix", size = (750,750))

#create function
def draw_Mondrians(win, sq):
    red = [1, -1, -1]
    green = [-1, 1, -1]
    blue = [-1, -1, 1]
    yellow = [1, 1, -1]
    black = [-1, -1, -1]
    violet = [1,-0.3,0.7]
    azure = [-0.6, 0.9, 1]
    colors = [red, green, blue, yellow, black, violet, azure]
    color = colors[random.randint(0,len(colors)-1)]
    sq.fillColor = color
    sq.lineColor = color
    #sq.color = color
    sq.setPos([random.randint(-500,450), random.randint(-550, 450)])
    sq.setSize(random.randrange(30*shape_size, 100*shape_size,5))
    sq.draw()

shapes = []
if round_shape:
    for i in range(5000):
        shapes.append(visual.Circle(win))
else:
    for i in range(5000):
        shapes.append(visual.Rect(win))

event.Mouse(visible = True)
for i in range(number_of_images):
    for shape in shapes:
        draw_Mondrians(win, shape)
    win.flip()
    y = ImageGrab.grab([550, 250, 1100, 800])
    y.save("Images\Mondrian%d.jpg" % i)
    core.wait(0.01)

core.quit()