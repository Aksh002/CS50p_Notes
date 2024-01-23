#         IMAGES AND PIL LIBRARY

#Binary file-Its just 0s and 1s that can be layed out in any pattern you want,particularly when you want to store not textual info but graphical,audio, video info
#               PIL/Pillow lib
#source-pillow.readthedocs.io

#              GIF production of 2 costumes
#gif is created by toggling 2 or more images one after another

#Since program expects 2 command line arguments,the names of the files,the individual images that we wanna animate back n forth
import sys
from PIL import Image
images=[]
for arg in sys.argv[1:]:    #we use use slice fxn([1:]) with sys.argv as we know that sys.argv() return file name at [0] position in the list
    image=Image.open(arg)
    images.append(image)
images[0].save(
    "costumes.gif",save_all=True,append_images=[image[1]],duration=200,loop=0     #loop=0 signifies looping infinite times
)                  #we dont hv to do opening and closing in csv, but we dont hv to do it here, save fxn do it for us here

#Basically, first we import sys library to recieve 2 command line inputs/arguments,the names of the image files.sys.argv fxn is used to return command line inputs in the form of list, we use use slice fxn([1:]) with sys.argv as we know that sys.argv() return file name at [0] position in the list
#Then we import Image fxn frm PIL library to make changes in the image. Then we take a empty list named students. and run the loop on the sys.argv to open the image and store it in variable named image and append the images in students list
#Then we will save the first image using save fxn but i am asking this library to append this other image to it as well(could be multuiple also).This save_all is used to save all the images together under name provided(here costumes.gif).Duration is used to get the pause of 200ms in between each frame. loop=0 loops this appending fxn  infinitely times.
#Then pass these fxns in command line
           '''
           python z_costumes.py zz_costumes1.gif zz_costumes2.gif
           code costumes.gif                                       '''# opening final image
 