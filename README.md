# image-recognition
I am trying to create image recognition software using Python (hopefully the end product will not even require any external libraries), and will be using a 'haar cascade'  to do so. It is not yet working.

The way it will work is called haar cascade. To my knowlege, this means that a numbers of haars will be generated to check if a certain part of an image is, for example, an eye. 
A haar is a black and white image that is smaller than the original image. For all possile positions in the image, it will compare the colors under the white parts of the haar and under the black parts (I am experimenting with also adding gray areas, that will be ignored).
The cascade part means that all positions that succeed in the first test, will undergo another to be more certain it is an eye. If it succeds, yet another haar will be overlaid, untill we are almost certain that the position is one of an eye.

NOTE: all pictures included are of myself. In real-life testing I will use more images of different people, but I can't put them on-line. 
