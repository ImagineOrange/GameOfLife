#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 02:27:11 2020

@author: ethancrouse
"""

#This program pixelates images and has multiple paths: single image pixelation




from PIL import Image
import time
import sys
import os

def main():
    first = True
    print("\n\n     ***NOTE: program only accepts .jpg, .jpeg file formats.")
    print("\nThis program pixelates images!")
    while first:
        route = str(input("\nType 'single' to pixelate a single image.\nType 'multi' to pixelate a whole folder of images at once.\nType 'exit' to exit program. "))
        if route == 'single':
            os.system('cls||clear')
            one_file()
            first = False
        elif route == 'multi':
            os.system('cls||clear')
            mult_file()
            first = False
        elif route == 'exit':
            sys.exit()
        else:
            print("\n\nInvalid input.")
            time.sleep(2)

 ###################################################################################

def mult_file(): #multi-file pixelation route
    
    def extractor(): #extracts files from directory and routes them to mult_pixel
        file_list=[]
        new_f=[]
        accept1 = ('.jpg')
        accept2 = ('.jpeg')
        accept3 = ('.JPG')
        basepath = str(input("Enter your desired directory: "))
        for entry in os.listdir(basepath): #appends all files from directory to file_list
            if os.path.isfile(os.path.join(basepath, entry)):
                file_list.append(entry)
        for file in range(0,(len(file_list))):
            if str(accept1) in file_list[file] or str(accept2) in file_list[file] or str(accept3) in file_list[file]:   #filters for only .jpg,.jpeg
                new_f.append(file_list[file])
        mult_pixel(new_f)
    

    def mult_pixel(imgs): #establishes pixelation level, opens images - sequentially routes to mult_pixelizer
        level = int(input("Enter Pixelation level. 1-5: "))
        LVL = 0   
        if level == 1 : 
            LVL= .05
        elif level ==2 : 
            LVL= .04
        elif level == 3 :        #establishes pixelation level
            LVL = .03
        elif level == 4 :
            LVL = .02
        elif level == 5 :
            LVL = .01
        else: 
            print("Error, invalid input. Restarting program.")
            mult_pixel()
        img_number=0 #used for savenames of pixelated files
        length = len(imgs)
        for image in range (len(imgs)):
            img_number+=1
            path = str(imgs[image])
            img = Image.open(path)
            print("\nPixelizing",img)
            time.sleep(2)
            mult_pixelizer(img,LVL,img_number,length)
        
    def mult_pixelizer(img,LVL,n,n2): #pixelizes images, sends to saver for saving
        xpixel,ypixel = img.size[0],img.size[1]
        xpixel = int(xpixel*LVL)
        ypixel = int(ypixel*LVL)
        reform = img.resize((xpixel,ypixel),resample=Image.BILINEAR) #grid to be used !!!
        pixel = reform.resize(img.size,Image.NEAREST) #image resized to original image resolution 
        mult_saver(pixel,n,n2,LVL)
    
    def mult_saver(pixel,n,n2,LVL): #names and saves pixelated images 
        filename = "pixelated"+str(n)+'_LVL_'+str(LVL)+'.jpg' #saves incoming images
        pixel.save(filename)
        print("Saved.")
        while n == n2:
            again = input("\nAll images saved to inputted directory. \nWould you like to pixelate again? (Y/N): ")
            if again == 'Y':
                main()
            else:
                sys.exit()
            
    extractor()



 ###################################################################################



def one_file(): #single-file pixelation route 
    def single(): #prompts for image file and prints stats
        try: 
            print("\nThis script pixelates a single image. Enter information in the fields below: ")
            path = str(input("Image File Path: "))
            image = Image.open(path)
            print("\nImage information: ", image.format, image.size, image.mode) #display img info 
            level = int(input("Enter Pixelation level. 1-5: "))
        except FileNotFoundError:
            er=input("Error, file not found.\nWould you like to try again? (Y/N): ")
            if er == 'Y':
                single()
            else:
                sys.exit()
        LVL = 0   
        if level == 1 : 
            LVL= .05
        elif level ==2 : 
            LVL= .04
        elif level == 3 :        #establishes pixelation level
            LVL = .03
        elif level == 4 :
            LVL = .02
        elif level == 5 :
            LVL = .01
        else: 
            print("Error, invalid input. Restarting program.")
            single()
        image = Image.open(path)
        print("\nPixelizing image...")
        time.sleep(2)
        pixelizer(image,LVL)
    
    def pixelizer(img,LVL): #resizes pixel with bilinear interpolation 
        xpixel,ypixel = img.size[0],img.size[1]
        xpixel = int(xpixel*LVL)
        ypixel = int(ypixel*LVL)
        reform = img.resize((xpixel,ypixel),resample=Image.BILINEAR) #grid to be used !!!
        reform.save('TEMP.JPG') ###?
        pixel = reform.resize(img.size,Image.NEAREST) #image resized to original image resolution 
        pixel.show()
        again = input("\nType 'Y' to pixelate again. Type 'N' to exit program. Otherwise, type 'save' to save the pixelated image. ")
        if again == 'N':
            pixel.close()
            sys.exit()
        elif again == 'Y':
            print('\n******************************\n')
            single()
        elif again == 'save':
            saver(pixel)
        else:
            print("Error, invalid input. Restarting program.")
            single()
            
    def saver(pixel): #function saves image according to inputted filename
        filename = input('Save image as: ')
        try:
            pixel.save(filename)
        except ValueError:
            print("\nError, unknown file extension. Try .PDF or .JPG ")
            time.sleep(1)
            saver(pixel)
            
        again = input("\nType 'Y' to pixelate again. Type 'N' to exit program. ")
        if again == 'N':
            pixel.close()
            sys.exit()
        elif again == 'Y':
            print('\n******************************\n')
            single()
    single()
main()

