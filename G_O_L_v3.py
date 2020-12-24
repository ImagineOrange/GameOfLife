#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 21:54:53 2020

@author: ethancrouse
"""

#conways game of life 
import matplotlib.pyplot as plt
import time
import random
import copy
# import os  #only works on osx, linux
from termcolor import colored

alive = colored('#','cyan')
HEIGHT = 15
WIDTH = 30
deadFlag = False
dead_count = 0

prev_cells = []
Cells = []
generations_x = []
generations = 0
death_points = []
breakloop = 0

#function for generating new configuration 
def generate(WIDTH, HEIGHT):
    for x in range (WIDTH):
            column=[]
            for y in range (HEIGHT):
                if random.randint(0,1)==0:
                    column.append(alive) #Appends a living cell
                else:
                    column.append(' ') #Appends a dead cell 
            Cells.append(column)
            
def reset():
    Cells.clear()
    currentCells.clear()
    generate(WIDTH,HEIGHT)
            
generate(WIDTH, HEIGHT)
    
while breakloop != 500: #main loop
    currentCells = copy.deepcopy(Cells)
    dead_count = 0
    for x in range (WIDTH):
        for y in range (HEIGHT):
            #GET NEIGHBORING COORDS
            leftcoord = (x-1) % WIDTH       #WIDTH IS WRAPPING
            rightcoord = (x+1) % WIDTH
            abovecoord = (y-1) % HEIGHT
            belowcoord = (y+1) % HEIGHT

            #COUNT NEIGHBORS!
            neighbors = 0                                    
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
                Cells[x][y] = ' '
            
            if Cells[x][y] == ' ':
                dead_count += 1
                
    #Tests for static generations
    if Cells == prev_cells:
        reset()
        generations_x.append(generations)
        generations = 1
        breakloop += 1
        
    #Establishes generational data to be compared to during the next generation to test
    #For staticness
    prev_cells = copy.deepcopy(Cells)
    
    #Tests for dead generations
    if dead_count == WIDTH*HEIGHT:
        reset()
        generations_x.append(generations)
        generations = 1
        breakloop += 1
    
    #Test for looping configurations
    if generations >= 800:
        reset()
        generations = 1
    
    generations+=1
    #time.sleep(.02)
print("Done")
plt.hist(generations_x, color = 'blue', edgecolor = 'black',
         bins = int(200))
