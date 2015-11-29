import pygame,math,sys

#SETTINGS:
startFace=0
numberOfFaces=20
haarNumber=2


def mean(array):
	return sum(array)/len(array)

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
    
    return abs(int((mean(white)-mean(black))/3))
#open haar
haar=pygame.image.load("haars/"+str(haarNumber)+".png")
Hwidth=haar.get_rect()[2]
Hheight=haar.get_rect()[3]
pygame.init()
for i in range(numberOfFaces):
    im=i+startFace
    print(im)
    image=pygame.image.load("faces/"+str(im)+".jpg")
    width=image.get_rect()[2]
    height=image.get_rect()[3]

    #detect face
    highest=0
    highX=[]
    highY=[]
    for x in range(width-Hwidth):
        for y in range(height-Hheight):
            dif = haardifference(image,haar,x,y)

            if dif==highest:
                highX.append(x)
                highY.append(y)
            elif dif>highest:
                highX=[x]
                highY=[y]
                highest=dif
        
        if int(x*10/(width-Hwidth))==(10*x/(width-Hwidth)):
            print(x/(width-Hwidth))
    print("done im.",im)
    
    for i in range(len(highX)):
        cropped = pygame.Surface((Hwidth, Hheight))
        cropped.blit(image, (0, 0), (highX[i], highY[i], Hwidth, Hheight))
        if i==0:
            pygame.image.save(cropped,"results\\"+str(im)+".png")
        else:
            pygame.image.save(cropped,"results\\"+str(im)+"."+str(i)+".png")
