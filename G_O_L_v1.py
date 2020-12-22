#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 21:54:53 2020

@author: ethancrouse
"""

#conways game of life 
import time
import random
import copy
# import os  #only works on osx, linux
from termcolor import colored

alive = colored('#','cyan')
HEIGHT = 15
WIDTH = 30

Cells = []
for x in range (WIDTH):
    column=[]
    for y in range (HEIGHT):
        if random.randint(0,1)==0:
            column.append(alive) #Appends a living cell
        else:
            column.append(' ') #Appends a dead cell 
    Cells.append(column)
    generations = 1
    breakloop = True #breaks loop when gen hits 150
    
while breakloop: #main loop
    print("\n\n")
    print("    *** Generation", generations,"***",)
    print('\n\n')
    currentCells = copy.deepcopy(Cells)
    print("********************************")
    for y in range (HEIGHT):
        print("*", end='')
        for x in range (WIDTH):
            print (currentCells[x][y],end='') #print the # or ' '
        print("*", end='')
        
        print() #newline printed at the end of row (HEIGHT)
    print("********************************",end='')
    
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
                

    generations+=1
    time.sleep(.2)
    if generations == 251:
        breakloop = False
  
    # os.system('clear')   #possible clearing animation, clears last frame

print("\n\n\n\n        ~~~Good-Job~!!!~~~")

#autosizing via width constant 
#see if can add ZONE DEAD
#find a way to animate
#experiment - investigate possible ranges of generations for failure - are there ranges moire likely to fail?
