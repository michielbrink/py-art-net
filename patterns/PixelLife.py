from Graphics import *
from Life.life import *
import random

class RandomLife(object):
	def __init__(self):
		self.life = Life(matrix_width, matrix_height, 1, color=BLACK)
		self.graphics = Graphics(matrix_width, matrix_height)
	def pickRandomColor(self):
		color = random.randint(0,len(COLORS)-1)
		#make sure that that color isn't black
		while(COLORS[color] == BLACK):
			color = random.randint(0, len(COLORS)-1)
		return COLORS[color]
	def drawRandomColor(self):
		life_matrix = self.graphics.toMatrix(self.life.field, self.graphics.getSurfaceWidth())
		for y in self.graphics.heightRange:
			for x in self.graphics.widthRange:
				if life_matrix[y][x]:
					color = self.pickRandomColor()
					#give every lifing cell a random color
					self.graphics.drawPixel(x,y, color)
				else:
					self.graphics.drawPixel(x,y, BLACK)
	def draw(self):
		self.drawRandomColor()
	def generate(self):
		self.life.process()
		self.draw()
		return self.graphics.getSurface()

class BlueLife(object):
	def __init__(self):
		self.life = Life(matrix_width, matrix_height, 1, color=BLUE)
		self.graphics = Graphics(matrix_width, matrix_height)
	def draw(self):
		life_matrix = self.graphics.toMatrix(self.life.field, self.graphics.getSurfaceWidth())
		for y in self.graphics.heightRange:
			for x in self.graphics.widthRange:
				if life_matrix[y][x]:
					color = BLUE
				else:
					color = BLACK
				self.graphics.drawPixel(x,y,color)
	def generate(self):
		self.life.process()
		self.draw()
		return self.graphics.getSurface()

'''
take the gray scales over every point and
add or subtract depening on if lifing or not
'''
class GrayedLife(object):
	def __init__(self):
		pass
	def generate(self):
		pass

class MixedLife(object):
	def __init__(self):
		blue = ColorRGBOps.darken(BLUE, 128)
		green = ColorRGBOps.darken(GREEN, 128)
		red = ColorRGBOps.darken(RED, 128)

		self.life1 = Life(matrix_width, matrix_height, 1, color=blue)
		self.life2 = Life(matrix_width, matrix_height, 1, color=green)
		self.life3 = Life(matrix_width, matrix_height, 1, color=red)
		
		self.graphics = Graphics(matrix_width, matrix_height)
		self.index = 0
	"""
	this draw function manipulates the graphics surface directly.
	it's either elegent in one way.
	and really really ugly in another way.
	"""
	def drawThreeAdded(self):
		pass
		# for index, cell in enumerate(self.life1.field):
		# 	color = self.graphics.surface[index]
		# 	if cell:
		# 		color = ColorRGBOps.add(color, self.life1.cellColor)
		# 	else:
		# 		color = ColorRGBOps.subtract(color, BLUE)
		# 	self.graphics.surface[index] = color

		# for index, cell in enumerate(self.life2.field):
		# 	color = self.graphics.surface[index]
		# 	if cell:
		# 		color = ColorRGBOps.add(color, self.life2.cellColor)
		# 	else:
		# 		color = ColorRGBOps.subtract(color, GREEN)
		# 	self.graphics.surface[index] = color

		# for index, cell in enumerate(self.life3.field):
		# 	color = self.graphics.surface[index]
		# 	if cell:
		# 		color = ColorRGBOps.add(color, self.life3.cellColor)
		# 	else:
		# 		color = ColorRGBOps.subtract(color, RED)
		# 	self.graphics.surface[index] = color
	def draw(self):
		self.drawThreeAdded()
	def generate(self):
		self.life1.process()
		self.life2.process()
		self.life3.process()
		self.draw()
		return self.graphics.getSurface()
