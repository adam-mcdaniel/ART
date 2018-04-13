import os, sys, time
from array import *
from PIL import Image
def path(s): return os.path.join(os.path.dirname(sys.argv[0]), s)

def rgb2hsv(r, g, b):
    r, g, b = r/255.0, g/255.0, b/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx-mn
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g-b)/df) + 360) % 360
    elif mx == g:
        h = (60 * ((b-r)/df) + 120) % 360
    elif mx == b:
        h = (60 * ((r-g)/df) + 240) % 360
    if mx == 0:
        s = 0
    else:
        s = df/mx
    v = mx
    return h, s, v

def load_image(name, color_range=10):
	image = Image.open(path(name)).convert("L")
	pixels = image.load()
	arr = []
	for y in range(image.height):
		for x in range(image.width):
			# try:
			# 	arr.append(int(rgb2hsv(*pixels[x, y][3:])[0]/(360/color_range)))
			# except:
			arr.append(int(pixels[x, y]/(255/color_range)))

	return arr, image.width, image.height