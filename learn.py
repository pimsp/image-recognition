#learning
import pygame,math,sys
import random as rnd

numberOfTruePicturs=33
numberOfFalsePicturs=11
atempts=1000

def mean(array):
	out=0
	for waarde in array:
		out+=waarde
	return out/len(array)
def haardifference(image,haar):
    ret=[]
    width=len(haar[0])
    height=len(haar)
    black=[]
    for x in range(width):
        for y in range(height):
            (r,g,b,a)=image.get_at((x,y))
            ret.append((r+b+g)*haar[y][x])
    return abs(int(mean(ret)))

def test(haar):

    true=[]
    false=[]
    for i in range(numberOfTruePicturs):
        image=pygame.image.load("examplesTRUE\\"+str(i)+".png")
        true.append(haardifference(image,haar))
    for i in range(numberOfFalsePicturs):
        image=pygame.image.load("examplesFALSE\\"+str(i)+".png")
        false.append(haardifference(image,haar))
    return(mean(true)*mean(true)/(mean(false)+1))
        
        
        


pygame.init()
for j in range(0,2):
    haar=[[0 for i in range(40)] for i in range(20)]
    lasthaar=[[0 for i in range(40)] for i in range(20)]
    maxhaar=[[0 for i in range(40)] for i in range(20)]
    score=0
    maxScore=0
    for i in range(atempts):
        n=20*i/atempts
        if n==int(n):
            print(str(int(5*n))+"%")
            print(" ",maxScore)
        lasthaar=haar
        
        x=rnd.randint(0,39)
        y=rnd.randint(0,19)
        haar[y][x]+=1
        
        x=rnd.randint(0,39)
        y=rnd.randint(0,19)
        haar[y][x]-=1
        
        score=test(haar)
        if score<=0.8*maxScore:
            haar=lasthaar
        elif not score<=maxScore:
            maxScore=score
            maxhaar=haar
    print("100%")
    print(j,":",test(maxhaar))
    print()
    
    file = open("haars\\"+str(j)+".txt", "w")
    file.write(str(maxhaar))
    file.close()

##    falseMax=0
##    for i in range(numberOfTruePicturs):
##        image=pygame.image.load("examplesTRUE\\"+str(i)+".png")
##        print("True #",i,":",haardifference(image,haar))
##    for i in range(numberOfFalsePicturs):
##        image=pygame.image.load("examplesFALSE\\"+str(i)+".png")
##        false=haardifference(image,haar)
##        if false>falseMax:
##            falseMax=false
##    print("false max:",falseMax)

    
