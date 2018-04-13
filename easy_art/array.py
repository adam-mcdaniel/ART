import random
from functools import *

def zoom(a, n): return list(reduce(lambda a, x: hstack(a, copy(expand(x, n), n)), list(map(lambda x: get_column(a, x), list(range(0, len(a[0]))))), make_size(len(a)*n)))

def compress(l1, n):
	l2 = [[]]
	c = 0
	for i, y in enumerate(l1):
		if i % n != 0:
			continue

		for j, x in enumerate(y):
			if c % n == 0:
				l2[-1].append(x)
			c += 1
		l2.append([])
		c = 0
	return l2[:-1]

def get_column(l1, n): return list(map(lambda a: [l1[a][n]], list(range(0, len(l1)))))

def hstack(l1, l2): return list(map(lambda a: a[0] + a[1], zip(l1, l2)))

def vstack(l1, l2): return l1 + l2

def replace(l1, elem, coords):
	l1[coords[1]][coords[0]] = elem
	return l1

def expand(l1, factor):
	length = len(l1)
	l2 = []
	for i in range(length):
		list(map(lambda a: l2.append(l1[i]), list(range(0, factor))))
	return l2

def make_size(length): return list(map(lambda a: [], list(range(0, length))))

def sum(l1): return list(reduce(lambda a, x: a + x, l1, []))

def make_2d(l1, dim):
	a = 0
	j = 0
	l2 = [[]]
	for i in range(0, len(l1)-1):
		if a > dim-1:
			j += 1
			a = 0
			l2.append([])
		a += 1
		l2[j].append(l1[i])
	l2[len(l2)-1].append(l1[len(l1)-1])
	return l2

def copy(l1, n):
	l2 = make_size(len(l1))
	for i in range(0, n):
		l2 = hstack(l1, l2)
	return l2

def random_range(a, lr, hr):
	return make_2d(list(map(lambda n: n + random.randint(lr, hr), sum(a))), len(a[0]))

def gcd(a, b):
    if b == 0:
        return a
    if b > a:
        return gcd(b, a)
    # This means b <= a
    return gcd(b, a % b)