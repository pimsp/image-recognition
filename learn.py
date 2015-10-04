#learning
import pygame,math,sys
import random as rnd
import numpy as np
def haardifference(image,haar):
    white=[]
    black=[]
    width=haar.get_rect()[2]
    height=haar.get_rect()[3]
    for x in range(width):
        for y in range(height):

            if haar.get_at((x,y))==(255,255,255,255):
                (r,g,b,a)=image.get_at((x,y))
                white.append(r+g+b)
            if haar.get_at((x,y))==(0,0,0,255):
                (r,g,b,a)=image.get_at((x,y))
                black.append(r+g+b)

    
    return abs(int((np.mean(white)-np.mean(black))/3))
def test(haar):
    numberOfTruePicturs=6
    numberOfFalsePicturs=11
    true=[]
    false=[]
    for i in range(numberOfTruePicturs):
        image=pygame.image.load("examplesTRUE\\"+str(i)+".png")
        true.append(haardifference(image,haar))
    for i in range(numberOfFalsePicturs):
        image=pygame.image.load("examplesFALSE\\"+str(i)+".png")
        false.append(haardifference(image,haar))
    return(np.mean(true)*np.mean(true)/(np.mean(false)+1))
        
        
        


pygame.init()
for j in range(10,15):
    haar=pygame.image.load("haars\\blanck.png")
    lasthaar=pygame.image.load("haars\\blanck.png")
    score=0
    maxScore=0
    atempts=10000
    for i in range(atempts):
        n=10*i/atempts
        if n==int(n):
            print(str(int(10*n))+"%")
            print(" ",maxScore)
        lasthaar=pygame.Surface.copy(haar)
        x=rnd.randint(0,39)
        y=rnd.randint(0,19)
        if haar.get_at((x,y))==(0,0,0):
            haar.set_at((x,y),(255,255,255))
        else:
            haar.set_at((x,y),(0,0,0))
        score=test(haar)
        if score<=0.8*maxScore:
            haar=pygame.Surface.copy(lasthaar)
        elif not score<=maxScore:
            maxScore=score
    print("100%")
    print(j,":",test(haar))
    print()
    pygame.image.save(haar,"haars\\"+str(j)+".png")


    
