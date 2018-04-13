import os
import sys
import time
import pygame
from pygame.locals import *
from collections import deque

pygame.init()

def make(f, canvas):
	size = canvas.size
	width = canvas.width
	height = canvas.height
	pixels = []
	for i in range(int(height / size)):
		pixels += list(map(
			lambda d: Paint((d[0]*size, i*size, size, size), d[1]),
			
			zip(
				list(range(int(width / size))),
				[f(int(x + i*(width / size))) for x in list(range(int(width / size)))]
			)
		))
	return pixels

class Paint(pygame.Surface):
	def __init__(self, rect, color):
		self.rect = pygame.Rect(rect)
		self.color = color
		super().__init__((self.rect.w, self.rect.h))
		self.fill(pygame.Color(self.color))

	def __str__(self):
		return "Pixel at x={} y={}".format(self.rect.left, self.rect.top)

class Canvas:
	def __init__(self, dimensions, size):
		self.display = pygame.display.set_mode(dimensions, pygame.DOUBLEBUF | pygame.HWSURFACE)
		self.display.fill((150, 150, 255))
		self.width = dimensions[0]
		self.height = dimensions[1]
		self.size = size
		self.pixels = []

	def paint(self, pixel):
		self.pixels.append(pixel)

	def refresh(self):
		list(map(lambda pixel: self.display.blit(pixel, pixel.rect), self.pixels))
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit(0)

	def save(self, name):
		self.refresh()
		pygame.image.save(self.display, os.path.relpath(name))