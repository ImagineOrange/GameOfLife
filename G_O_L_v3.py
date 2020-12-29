#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 12:33:07 2020

@author: ethancrouse
"""

<<<<<<< Updated upstream
# conway's game of life ~ w/ interesting stats

=======
# conways game of life
import matplotlib.pyplot as plt
import matplotlib.animation as animation
>>>>>>> Stashed changes
import time
import random
import copy
from termcolor import colored
import matplotlib as plt

<<<<<<< Updated upstream
ITERATIONS = int(input("Note: New configuration generated upon dead/static grid.\nDesired number of configurations: "))
GEN_CAP = int(input("Input generation cap: "))
alive = colored('#','cyan') #alive cell color
=======
alive = colored('#', 'cyan')
>>>>>>> Stashed changes
HEIGHT = 15
WIDTH = 30
dead_count = 0

prev_cells = [] 
Cells = []
generations_x = [] 
death_points = []
generations = 0 #counter for generations
breakloop = 0 #counter for config restarts

def stats(death_points,generations_x): #
    print('\n\n')
    print("There were", len(death_points), 'dead or static configurations. ')
    if len(generations_x)>0:
        print("\nThe generation numbers: ",generations_x)
    
    plt.hist(generations_x, color = 'blue', edgecolor = 'black',    #generate histogram of gen numbers
         bins = int(200))
    

# function for generating new configuration


def generate(WIDTH, HEIGHT):
<<<<<<< Updated upstream
    for x in range (WIDTH):
            column=[]
            for y in range (HEIGHT):
                if random.randint(0,1)==0:
                    column.append(alive) #Appends a living cell
                else:
                    column.append(' ') #Appends a dead cell 
            Cells.append(column) #appends each randomly generated column to Cells array
            
generate(WIDTH, HEIGHT) 
    
while breakloop != ITERATIONS: #main program loop --- breakloop incremented by +=1 every static/dead config
    print("\n\n")
    print("    *** Generation", generations,"***",) #Print generation #
    print('\n\n')
    currentCells = copy.deepcopy(Cells) #currentCells copies initial Cells array, undergoes testing
   
    
    ##########################################
    print("********************************")
    for y in range (HEIGHT):
        print("*", end='')
        for x in range (WIDTH):
            print (currentCells[x][y],end='') #print the # or ' '     # <---- main output block
        print("*", end='')
        print() #newline printed at the end of row (HEIGHT)
    print("********************************",end='')
    ##########################################
   
    dead_count = 0
    
    for x in range (WIDTH):
        for y in range (HEIGHT):
            #GET NEIGHBORING COORDS
            leftcoord = (x-1) % WIDTH       #WIDTH IS WRAPPING
=======
    for x in range(WIDTH):
        column = []
        for y in range(HEIGHT):
            if random.randint(0, 1) == 0:
                column.append(alive)  # Appends a living cell
            else:
                column.append(' ')  # Appends a dead cell
        Cells.append(column)


def reset():
    Cells.clear()
    currentCells.clear()
    generate(WIDTH, HEIGHT)


def animate(i):
    xar = []
    yar = []
    for x_nums in generations_x:
        xar.append(int(x_nums))

    for gen_num in generations_x:
        y_num = generations_x.count(gen_num)
        yar.append(int(y_num))

    ax1.clear()
    ax1.plot(xar, yar)


generate(WIDTH, HEIGHT)

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)

while breakloop != 50:  # main loop
    currentCells = copy.deepcopy(Cells)
    dead_count = 0
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # GET NEIGHBORING COORDS
            leftcoord = (x-1) % WIDTH  # WIDTH IS WRAPPING
>>>>>>> Stashed changes
            rightcoord = (x+1) % WIDTH
            abovecoord = (y-1) % HEIGHT
            belowcoord = (y+1) % HEIGHT

<<<<<<< Updated upstream
            #CHECK NEIGHBOR STATS
            neighbors = 0 #counter for live neighbors
            if currentCells[leftcoord][abovecoord] == alive :           #X#
                neighbors+=1#leftabove                                  #C#
            if currentCells[x][abovecoord] == alive :                 # Y##
                neighbors+=1#above
            if currentCells[rightcoord][abovecoord] == alive :
                neighbors+=1#aboveright
            if currentCells[leftcoord][y] == alive :
                neighbors+=1#left
            if currentCells[rightcoord][y] == alive :
                neighbors+=1#right
            if currentCells[leftcoord][belowcoord] == alive :
                neighbors+=1#belowleft
            if currentCells[x][belowcoord] == alive :
                neighbors+=1#middleblow
            if currentCells[rightcoord][belowcoord] == alive :
                neighbors+=1#belowright
                
            if currentCells[x][y] == alive and (neighbors == 2 or neighbors == 3):  #alive cells stay alive
                Cells[x][y] = alive 
            elif currentCells[x][y] == ' ' and neighbors == 3: #dead cells come alive
                Cells[x][y] = alive
            else: 
                Cells[x][y] = ' ' #die/dead
            
            if Cells[x][y] == ' ':
                dead_count += 1

    #Tests for static generations
=======
            # COUNT NEIGHBORS!
            neighbors = 0
            if currentCells[leftcoord][abovecoord] == alive:  # X#
                neighbors += 1  # leftabove                                  #C#
            if currentCells[x][abovecoord] == alive:                 # Y##
                neighbors += 1  # above
            if currentCells[rightcoord][abovecoord] == alive:
                neighbors += 1  # aboveright
            if currentCells[leftcoord][y] == alive:
                neighbors += 1  # left
            if currentCells[rightcoord][y] == alive:
                neighbors += 1  # right
            if currentCells[leftcoord][belowcoord] == alive:
                neighbors += 1  # belowleft
            if currentCells[x][belowcoord] == alive:
                neighbors += 1  # middleblow
            if currentCells[rightcoord][belowcoord] == alive:
                neighbors += 1  # belowright

            # alive cells stay alive
            if currentCells[x][y] == alive and (neighbors == 2 or neighbors == 3):
                Cells[x][y] = alive
            elif currentCells[x][y] == ' ' and neighbors == 3:  # dead cells come alive
                Cells[x][y] = alive
            else:
                Cells[x][y] = ' '

            if Cells[x][y] == ' ':
                dead_count += 1

    # Tests for static generations
>>>>>>> Stashed changes
    if Cells == prev_cells:
        death_points.append(generations)
        Cells.clear()
        currentCells.clear()
        print("\n\n\nSTATIC CONFIG - New Config Incoming...")
        time.sleep(1)
        generate(WIDTH,HEIGHT)
        generations_x.append(generations)
        generations = 1
        breakloop += 1
<<<<<<< Updated upstream
        
    #Tests for dead generations
=======

    # Establishes generational data to be compared to during the next generation to test
    # For staticness
    prev_cells = copy.deepcopy(Cells)

    # Tests for dead generations
>>>>>>> Stashed changes
    if dead_count == WIDTH*HEIGHT:
        death_points.append(generations)
        Cells.clear()
        currentCells.clear()
        print("\n\n\nDEAD CONFIG - New Config Incoming...")
        time.sleep(1)
        generate(WIDTH, HEIGHT)
        generations_x.append(generations)
        generations = 1
        breakloop += 1
<<<<<<< Updated upstream
        
    #new config if gencap is met, prevents infinite loops
    if generations == GEN_CAP: 
        Cells.clear()
        currentCells.clear()
        print("\n\n\nGENCAP REACHED - New Config Incoming...")
        time.sleep(1)
        generate(WIDTH, HEIGHT)
        generations = 1
        breakloop +=1
        
        
    #Establishes generational data to be compared to during the next generation to test
    #For staticness
    prev_cells = copy.deepcopy(Cells) #sets up copy of config for comparison with next generation
    
    generations+=1
    time.sleep(.2)


stats(death_points,generations_x)


=======

    # Test for looping configurations
    if generations >= 800:
        reset()
        generations = 1

    generations += 1
    time.sleep(.02)

print("Calculations completed")
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
print("Done")
>>>>>>> Stashed changes
