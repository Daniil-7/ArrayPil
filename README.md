# ArrayPil
---
The library that translates the Pillow image into a Numpy array and on the contrary. It also allows you to save images from the Numpy array.
The library is designed to facilitate and understand the code.
I also apologize for my crooked English translation.
Author's website:
https://tatem.pythonanywhere.com/
---
# Example of using the library:
## importing ArrayPil
```python
from ArrayPil import *
```
## importing numpy and pillow
```python
from PIL import Image
import numpy as np
```
## we will get a array numpy the image that we took from our folder (your folder)
```python
# the first parameter is the location of the image 
# the second parameter is the default RGB color model
num_array = ConvImgArray('image1.jpg')
print(num_array)
```
## convert the a array numpy into a picture
```python
# the first parameter is a array numpy
# the second parameter is the location where the image is saved
# the third parameter is the default RGB color model
ImgSave(num_array, 'res.jpg')
```
## convert the numpy array to a pillow image
```python
# the first parameter is a array numpy
# the second parameter is the default RGB color model
pil_img = ConvImgPil(num_array)
print(pil_img)
```
## convert pillow images to numpy array
```python
# the first parameter is the pillow image
# the second parameter is the default RGB color model
num_array2 = ConvPilArray(pil_img)
print(num_array2)
```
