from PIL import Image
import numpy as np



def ConvImgArray(imgdir, conv='RGB'):
		im1 = np.asarray(Image.open(imgdir).convert(conv))
		return im1
		
		
def ImgSave(imgarray, dirsave, conv='RGB'):
	   	im2 = Image.fromarray(imgarray, conv)
	   	im2.save(dirsave)


def ConvPilArray(imgpil, conv='RGB'):
		im3 = np.asarray(imgpil.convert(conv))
		return im3


def ConvImgPil(imgarray, conv='RGB'):
		im4 = Image.fromarray(imgarray, conv)
		return im4
		
		
#testing
#
#a1 = ConvImgArray('image1.jpg')
#print(a1)
#
#ImgSave(a1, 'res.jpg')
#
#a2 = ConvImgPil(a1)
#print(a2)
#
#a3 = ConvPilArray(a2)
#print(a3)