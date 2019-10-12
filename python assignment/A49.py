Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from os import walk
>>> for diepath, dirnames, filenames in walk('E:\Python\Images')
SyntaxError: invalid syntax
>>> from os import walk
>>> for diepath, dirnames, filenames in walk('E:\Python\Images'):
	print(filenames)

	
['IMG_20151225_083012_HDR.jpg', 'IMG_20160117_173221_HDR.jpg']
>>> 
