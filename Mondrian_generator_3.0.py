#----------------------------------------------#
#------------Mondrian generator v3.0-----------#
#-------Suran, T., & van Dooren, R., 2017------#
#----------------------------------------------#

'''The program creates Mondrian pattern images of size 600x600 pixels
and saves them in the "Images" folder.
It is possible to choose between circles and squares, and between coloured
or grayscale images. The 'Shape size proportion' parameter allows to set
the size range of the shapes. Version 3.0 works both on PC and Mac.'''

#import libraries
from psychopy import os, visual, core, event, gui
import random
from PIL import ImageGrab, Image
import wx

#get screen resolution
app = wx.App(False)
width, height = wx.GetDisplaySize()


#parameters
def parameters():
    global number_of_images, round_shape, shape_size, grayscale
    myDlg = gui.Dlg(title="Set parameters")
    myDlg.addField('Number of images:', 5)
    myDlg.addField('Shape type:', choices=["Circles", "Squares"])
    myDlg.addField('Shape size proportions:', 1.0)
    myDlg.addField('Grayscale:', choices=["No", "Yes"])
    myDlg.show()  # show dialog and wait for OK or Cancel
    if myDlg.OK:  # or if ok_data is not None
        try:
            number_of_images = int(str(myDlg.data[0]))
            if str(myDlg.data[1]) == "Circles":
                round_shape = 1
            else:
                round_shape = 0
            shape_size = float(myDlg.data[2])
            if str(myDlg.data[3]) == "No":
                grayscale = 0
            else:
                grayscale = 1
            return
        except ValueError:
            parameters()
    else:
        print('user cancelled')
parameters()

#create Images folder
if not os.path.exists("Images"):
    os.makedirs("Images")

#create window
win = visual.Window(fullscr = 0, units="pix", size = [600,600], pos = [(width/2)-300, (height/2)-300])

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
    sq.setPos([random.randint(-300,300), random.randint(-300, 300)])
    sq.setSize(random.randrange(int(round(30*shape_size)), int(round(100*shape_size)),5))
    sq.draw()

shapes = []
if round_shape:
    for i in range(4000):
        shapes.append(visual.Circle(win))
else:
    for i in range(4000):
        shapes.append(visual.Rect(win))

event.Mouse(visible = False)

for i in range(number_of_images):
    for shape in shapes:
        draw_Mondrians(win, shape)
    win.flip()
    y = ImageGrab.grab([(width/2)-300, (height/2)-300, (width/2)+300, (height/2)+300])
    if grayscale:
        y = y.convert('L')
    y.save(os.path.join("Images", "Mondrian") + "%d.jpg" % (i+1))
    core.wait(0.01)

core.quit()