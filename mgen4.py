import matplotlib.pyplot as plt
import time
import random
import os

def create_pattern_and_save(ncircles, filename):

    save_directory = "mondrians"
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    colors = ['r', 'lawngreen', 'blue', 'yellow']
    
    fig, ax = plt.subplots(figsize=(5,5))
    ax.axis('off')

    for c in range(ncircles):
        xpos = random.randrange(0, 100)/100
        ypos = random.randrange(0, 100)/100
        c_size = random.randrange(5, 20)/100
        #print(xpos, ypos)

        circle = plt.Circle((xpos, ypos), c_size, color=random.choice(colors))

        ax.add_patch(circle)

    savepath = os.path.join(save_directory, f'{filename}.png')
    fig.savefig(savepath, bbox_inches='tight', pad_inches = 0)


def batch_create_patterns(tgt_patterns, circles_x_pattern):
    for i in range(tgt_patterns):
        filename = "mpattern_"+str(i+1)
        create_pattern_and_save(circles_x_pattern, filename)
        print("created", i+1, "out of", tgt_patterns)

if __name__ == "__main__":

    #get user input
    tgt_patterns = int(input("How many patterns? "))
    circles_x_pattern = int(input("Number of circles per pattern? (suggested 1500) "))
    
    batch_create_patterns(tgt_patterns, circles_x_pattern)