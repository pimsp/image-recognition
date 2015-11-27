#face recognision using haar-cascade
import pygame,math,sys


def mean(array):
	out=0
	for waarde in array:
		out+=waarde
	return out/len(array)

def haardifference(image,haar,X,Y):
    ret=[]
    width=len(haar[0])
    height=len(haar)
    black=[]
    for x in range(width):
        for y in range(height):
            (r,g,b,a)=image.get_at((x+X,y+Y))
            ret.append((r+b+g)*haar[y][x])
    return abs(int(mean(ret)))
            
            
            
#open image
pygame.init()
image=pygame.image.load("faces\\0.jpg")


#open haar
ar=open("haars\\"+str(0)+".txt", "r").read()[2:-2].split('], [')
haar=[[int(i) for i in st.split(',')] for st in ar]

width=image.get_rect()[2]-len(haar[0])
height=image.get_rect()[3]-len(haar)

screen = pygame.display.set_mode((width,height))
highest=0
highX=[]
highY=[]
def mean(array):
	out=0
	for waarde in array:
		out+=waarde
	return out/len(array)

for x in range(width):
    for y in range(height):
        dif = haardifference(image,haar,x,y)

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

print((round(mean(highX)),round(mean(highY)))," heeft waarde:" ,highest)
print(haardifference(image,haar,round(mean(highX)),round(mean(highY))))

screen.set_at((int(round(mean(highX))),int(round(mean(highY)))),(255,0,0))
screen.set_at((int(round(mean(highX)))+1,int(round(mean(highY)))-1),(255,0,0))
screen.set_at((int(round(mean(highX)))+1,int(round(mean(highY)))+1),(255,0,0))
screen.set_at((int(round(mean(highX)))-1,int(round(mean(highY)))+1),(255,0,0))
screen.set_at((int(round(mean(highX)))-1,int(round(mean(highY)))-1),(255,0,0))
#print(haardifference(image,haar0,21,41))
#print(haardifference(image,haar0,36,41))


pygame.display.flip()
