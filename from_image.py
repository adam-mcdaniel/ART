import random
from easy_art import *
from easy_art.tools import *
from easy_art.image import *
from easy_art.array import *

def row(x, canvas):
	return int(x / (canvas.width / canvas.size))

def column(x, canvas):
	return int(x % (canvas.width / canvas.size))

def pos(x, canvas): return (row(x, canvas), column(x, canvas))

def resize(f, w, h, z, s=1): return zoom(make_2d(list(f((w/z) * (h/z)))[:int((w/z) * (h/z)*s*s)], w/z/s), s)

def resize_random(f, width, height, size, scale=1, lowrange=-1, highrange=1): return sum(random_range(list(resize(lambda n: list(map(f, list(range(0, int(n))))), width, height, size, scale)), lowrange, highrange))

def corrode_image(name, c, lr=-1, hr=1, color_range=10):
	array, width, height = load_image(name, color_range=color_range)

	size = int(round(gcd(width, height) / c))

	print((c, size))

	array = sum(random_range(compress(make_2d(array, width), c), lr, hr))
	width = int(width * size/c)
	height = int(height * size/c)
	return array, width, height, size


array, width, height, size = corrode_image('/Users/kiwi/Desktop/Ruby/ruby2.png', 8, 0, 0, 10)

c = pixel.Canvas((width, height), size)

# colors = generate(100, 13, 20)
# colors = generate(20, 13, 10)
# colors = generate(250, 13, 9, saturation=0.8, value=1.0)
colors = generate(0, 13, 36, saturation=0.8, value=0.8)
# colors = generate(156, 17, 7, saturation=0.6, value=0.8)
# colors = generate(300, 17, -17, saturation=0.6, value=0.8)
# colors = generate(170, 17, -17, saturation=0.6, value=0.8)
# colors = generate(260, 13, -10, saturation=0.8)
# colors = generate(250, 22, -6, saturation=0.8)
# colors = generate(255, 300, -1, saturation=0.6, value=0.8)
# colors = generate(0, 180, 2, saturation=0.6, value=0.8)
# colors = generate(0, 150, 15, saturation=0.6, value=0.8)
# colors = generate(10, 13, 30)


list(map(
	c.paint,
	pixel.make(lambda x: colors[array[x]], c)
))

c.save("ruby.png")


#ur cute and i believe in u
