
from PIL import Image, ImageFilter, ImageDraw, ImageFont

firPic = Image.open("1.jpg")
firPic.show()
print(firPic.size, firPic.mode)

resizedPic = firPic.reduce(3)
resizedPic.save("resizedPic.jpg")
mirPic = firPic.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
mirPic2 = firPic.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
mirPic.save("mirPic.jpg")
mirPic2.save("mirPic2.jpg")

MassOfPics = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg']
for files in MassOfPics: 
    pic = Image.open(files)
    pic = pic.filter(ImageFilter.FIND_EDGES)
    nameforPICS = "done" + str(files) 
    pic.save(f"{nameforPICS}")
    
waterMark = ImageDraw.Draw(firPic)
waterMark.text((100,100),"WATER_MARK", 100, font=ImageFont.load_default(), size=50)
firPic.save("WaterMark.jpg")