from PIL import Image, ImageFilter

img = Image.open('./image/jevg.jpg')

# Blur image
filteredImage = img.filter(ImageFilter.BLUR)
filteredImage.save("blur.png","png")

#rotate image
crooked = filteredImage.rotate(90)
crooked.save("blur.png","png")

#Turn picture to black and white
filteredImage1 = img.convert('L')
filteredImage1.save("grey.png","png")

#resize image
resize = filteredImage.resize((300,300))

#crop image
box = (100,100,400,400)
crop = filteredImage.crop(box)

#resize an Image
img2 = Image.open("./image/jorch.jpg")
img2.thumbnail((400,400))
img2.save("thumbnail.jpg")
print(img2.size)


# To display image
# crop.show() 
