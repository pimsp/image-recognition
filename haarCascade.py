#face recognision using haar-cascade
import pygame,math,sys
#import pandas as pd
import numpy as np
#import matplotlib as mp

def haardifference(image,haar,x,y):
    white=[]
    black=[]
    width=haar.get_rect()[2]
    height=haar.get_rect()[3]
    for xh in range(width):
        for yh in range(height):
            if haar.get_at((xh,yh))==(255,255,255,255):
                (r,g,b,a)=image.get_at((xh+x,yh+y))
                white.append(r+g+b)
            if haar.get_at((xh,yh))==(0,0,0,255):
                (r,g,b,a)=image.get_at((xh+x,yh+y))
                black.append(r+g+b)
    
    return abs(int((np.mean(white)-np.mean(black))/3))
            
            
            
#open image
pygame.init()
image=pygame.image.load("3175.jpg")
width=image.get_rect()[2]
height=image.get_rect()[3]

#detect face
haar0=pygame.image.load("haars/7.png")
width0=haar0.get_rect()[2]
height0=haar0.get_rect()[3]

haar1=pygame.image.load("haars/0.png")
width1=haar1.get_rect()[2]
height1=haar1.get_rect()[3]
screen = pygame.display.set_mode((width-width0,height-height0))
highest=0
highX=[]
highY=[]
for x in range(width-width0):
    for y in range(height-height0):
        dif = haardifference(image,haar0,x,y)

        if dif==highest:
            highX.append(x)
            highY.append(y)
        elif dif>highest:
            highX=[x]
            highY=[y]
            highest=dif
        try:
            
            screen.set_at((x,y),(dif*2,dif*2,dif*2,255))
            if dif>50:
                screen.set_at((x,y),(0,dif*2,0,255))
        except:
            screen.set_at((x,y),(255,255,255,255))
    
    pygame.display.flip()

print((round(np.mean(highX)),round(np.mean(highY)))," heeft waarde:" ,highest)
print(haardifference(image,haar0,round(np.mean(highX)),round(np.mean(highY))))

screen.set_at((int(round(np.mean(highX))),int(round(np.mean(highY)))),(255,0,0))
screen.set_at((int(round(np.mean(highX)))+1,int(round(np.mean(highY)))-1),(255,0,0))
screen.set_at((int(round(np.mean(highX)))+1,int(round(np.mean(highY)))+1),(255,0,0))
screen.set_at((int(round(np.mean(highX)))-1,int(round(np.mean(highY)))+1),(255,0,0))
screen.set_at((int(round(np.mean(highX)))-1,int(round(np.mean(highY)))-1),(255,0,0))
#print(haardifference(image,haar0,21,41))
#print(haardifference(image,haar0,36,41))


pygame.display.flip()
