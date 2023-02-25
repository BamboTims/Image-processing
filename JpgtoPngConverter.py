import sys
import os

from PIL import Image

#Grab arguments
folderName = sys.argv[1]
outputFolderName = sys.argv[2]

#create outputfolder if it doesnt exist
if not os.path.exists(outputFolderName):
    os.makedirs(outputFolderName)

#converting images in the *folderName folder
for filename in os.listdir(folderName):
    img = Image.open(f"{folderName}{filename}")
    cleanName,_ = os.path.splitext(filename)
    img.save(f"{outputFolderName}{cleanName}.png", "png")
    print(f"{cleanName} converted to png")