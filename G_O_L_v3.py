#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 12:33:07 2020

@author: ethancrouse
"""

# conway's game of life ~ w/ interesting stats

import time
import random
import copy
from termcolor import colored
import matplotlib as plt

ITERATIONS = int(input("Note: New configuration generated upon dead/static grid.\nDesired number of configurations: "))
GEN_CAP = int(input("Input generation cap: "))
alive = colored('#','cyan') #alive cell color
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
    

#function for generating new configuration 
def generate(WIDTH, HEIGHT):
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
   
    # ##########################################
    # print("********************************")
    # for y in range (HEIGHT):
    #     print("*", end='')
    #     for x in range (WIDTH):
    #         print (currentCells[x][y],end='') #print the # or ' '     # <---- main output block
    #     print("*", end='')
    #     print() #newline printed at the end of row (HEIGHT)
    # print("********************************",end='')
    # ##########################################
   
    dead_count = 0
    
    for x in range (WIDTH):
        for y in range (HEIGHT):
            #GET NEIGHBORING COORDS
            leftcoord = (x-1) % WIDTH       #WIDTH IS WRAPPING
            rightcoord = (x+1) % WIDTH
            abovecoord = (y-1) % HEIGHT
            belowcoord = (y+1) % HEIGHT

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
        
    #Tests for dead generations
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


