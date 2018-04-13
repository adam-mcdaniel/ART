import colorsys
import webcolors
from functools import *

def pi_digits(n):
	"Generate n digits of Pi."
	k, a, b, a1, b1 = 2, 4, 1, 12, 4
	while n > 0:
		p, q, k = k * k, 2 * k + 1, k + 1
		a, b, a1, b1 = a1, b1, p * a + q * a1, p * b + q * b1
		d, d1 = a / b, a1 / b1
		while d == d1 and n > 0:
			yield int(d)
			n -= 1
			a, a1 = 10 * (a % b), 10 * (a1 % b1)
			d, d1 = a / b, a1 / b1

def pi(n): return list(pi_digits(n+1))[int(n)]

def fib(n):
	a,b,c = 0,1,0
	while c < n:
		yield a
		c += 1
		a, b = b, a + b

def fibonacci(n): return int(reduce(lambda a, x: a + str(x), list(fib(n+1)), "0")[int(n+1)])

def hsv2rgb(h,s,v):
	return tuple(int(i * 255) for i in colorsys.hsv_to_rgb(h,s,v))

def rgb2hex(rgb): return webcolors.rgb_to_hex(rgb)

def generate(h, n, u, saturation=0.8, value=1.0):
	return list(map(lambda a: (rgb2hex(hsv2rgb((h + u*a)/360, saturation, value))), list(range(n))))
