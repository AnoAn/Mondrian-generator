import matplotlib.pyplot as plt
import time
import random
import os
from PIL import Image


def create_pattern_and_save(nshapes, shape, filename, dpi, grayscale):

    save_directory = "mondrians"
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    if grayscale:
        colors = [(intensity/255,)*3 for intensity in [50, 100, 130, 180, 220]]
    else:
        colors = ['r', 'lawngreen', 'blue', 'yellow']
    
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.axis('off')

    for c in range(nshapes):
        xpos = random.randrange(0, 100)/100
        ypos = random.randrange(0, 100)/100
        s_size = random.randrange(5, 20)/100
        #print(xpos, ypos)

        if shape == 'c':
            curr_shape = plt.Circle((xpos, ypos), s_size, color= random.choice(colors))
        else:
            curr_shape = plt.Rectangle((xpos, ypos), s_size, s_size, color= random.choice(colors))

        ax.add_patch(curr_shape)

    savepath = os.path.join(save_directory, f'{filename}.png')
    fig.savefig(savepath, bbox_inches='tight', pad_inches = 0, dpi = dpi)
    
    #convert to grayscale - add if
    #img = Image.open(savepath).convert('L')
    #img.save(savepath)



def ask_user_input():
    while True:
        shape = input("Do you want circles (default) or squares? [type c or s]: ")
        if shape == '':
            shape = 'c'
            break
        elif shape not in ['c', 's']:
            print("Enter the lowercase 'c' for circels or 's' for squares")
            continue  
        else:
            break

    while True:
        grayscale = input("Want colors (default; otherwise grayscale)? [y/n] ")
        if grayscale == '':
            grayscale = False
            break
        elif grayscale not in ['y', 'n']:
            print("Enter the lowercase 'c' for colors or 'g' for grayscale")
            continue  
        else:
            grayscale = True
            break
        

    tgt_patterns = input("How many patterns (default 3): ")
    shapes_per_pattern = input("Number of circles per pattern (default 1500): ")
    dpi = input("Figure DPI (default 96; determines size): ")
    

    if tgt_patterns == "": tgt_patterns = 3
    else: tgt_patterns = int(tgt_patterns)

    if shapes_per_pattern == "": shapes_per_pattern = 1500
    else: shapes_per_pattern = int(shapes_per_pattern)

    if dpi == "": dpi = 96.0
    else: dpi = float(dpi)

    return tgt_patterns, shape, shapes_per_pattern, dpi, grayscale



if __name__ == "__main__":

    #get user input
    tgt_patterns, shape, shapes_per_pattern, dpi, grayscale = ask_user_input()
    
    for i in range(tgt_patterns):
        filename= "mpattern_"+str(i+1)
        create_pattern_and_save(shapes_per_pattern, shape, filename, dpi, grayscale)
        print("created", i+1, "out of", tgt_patterns)