from PIL import Image

def imagetoascii(image, sizefactor=10, width=None, height=None, invert=False, color=False, allats=False):
	"""
	image: The only required field. What image do you want to be changed into ascii? Must be a path/filename (string)
	sizefactor: How many times smaller do you want your ascii image to be? Is overridden by width or height settings. (int)
	width: How many chars long do you want the asciiart to be? (int)
	height: How tall do you want your asciiart to be? (int)
	invert: Do you want the dark parts to be bright and vice versa? (bool)
	color: Do you want your image to be in color? (Uses Truecolor) (bool)
	allats: Reccomended for color. Do you want the entire image to be @s so it looks more like a photo? (bool)
	"""
	b = []
	sizefactor = round(sizefactor)
	try:
		import replit # Testing if it is on repl.it
		if invert:
			invert = False
		else:
			invert = True
	except:
		pass
	GRAYSCALE = " .:-=+*#%@"[::-1]
	if allats:
		GRAYSCALE = "@@@@@@@@@@@@@"
	if invert:
		GRAYSCALE = GRAYSCALE[::-1]
	img = Image.open(image)
	width_, height_ = img.size
	if width == None and height == None:
		img.thumbnail((width_ / sizefactor, height_ / sizefactor)) # Making the image smaller
	elif width != None:
		img.thumbnail((width, height_))
	elif height != None:
		img.thumbnail((width_, height))
	width_ = img.size[0]
	pixvals = list(img.getdata()) # RGB values for all the images

	ab = 0
	for x in pixvals:
		if type(x) == int:
			pixvals[ab] = (x, x, x) # Turns into tuple if needed
		ab += 1
	ab = 0
	for x in pixvals:
		a = x[0] + x[1] + x[2] # Averaging the tuples
		a /= 3
		a /= (255 / 9)
		a = round(a)
		b.append(GRAYSCALE[a] * 2) # Assigning them to their greyscales
		if ab % width_ == width_ - 1:
			b.append("\n")
		ab += 1
	if color:
		test = 0
		ab = 0
		for x in b:
			if x != "\n":
				temp = pixvals[ab]
				b[test] = "\x1b[38;2;" + str(temp[0]) + ";" + str(temp[1]) + ";" + str(temp[2]) + "m" + x
				ab += 1
			test += 1
	b = "".join(b)
	return b

f = open("out.txt", "w")
a = imagetoascii("test card.png", 10, invert=False)

f.write(a)
print("Done")
print(len(a), "chars long")
f.close()

# Image to color
print(imagetoascii("ice cream.jpeg", 1, invert = False, color = True, allats = True))