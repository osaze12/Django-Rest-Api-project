        
from PIL import Image, ImageDraw, ImageFilter



img1 = Image.open('media/uploads/8.jpg')
img2 = Image.open('media/uploads/decorative-lines-transparent-18.png')

#resize the image
new = img2.resize((450, 200))
imgone = Image.open('media/uploads/eight.png')

#make it be on top of another image
#first for left-right. second for up-down
imgone.paste(new, (430,500), new)
imgone.save('media/uploads/new.jpg', quality=95)