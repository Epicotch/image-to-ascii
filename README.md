# image-to-ascii
A python package that turns images into asciiart.

image: The only required field. What image do you want to be changed into ascii? Must be a path/filename (string)
sizefactor: How many times smaller do you want your ascii image to be? Is overridden by width or height settings. (int)
width: How many chars long do you want the asciiart to be? (int)
height: How tall do you want your asciiart to be? (int)
invert: Do you want the dark parts to be bright and vice versa? (bool)
color: Do you want your image to be in color? (Uses Truecolor) (bool)
allats: Reccomended for color. Do you want the entire image to be @s so it looks more like a photo? (bool)
