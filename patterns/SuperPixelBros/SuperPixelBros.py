from Graphics import *
from Controllers import *
from time import time

c = BLACK
r = RED
g = GREEN
b = BLUE

level1 = [
			c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,
			c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,
			c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,
			c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,
			c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,
			g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,
			g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,
			g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,
			g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,
			g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,
		]

level = [BLUE]*matrix_size

class PixelBrosController(PygameController, XboxController):
	def __init__(self, plugged=0):
		PygameController.__init__(self, plugged)
	def getDpad(self, button):
		return PygameController.getButtons(self, button)

"""Tile class holds info on individual Tiles"""
class TilePixel(object):
	def __init__(self, pos, color, graphics):
		self.color = color
		self.graphics = graphics
		self.pos = (pos[1],pos[0])
		print self.pos
	def draw(self):
		x,y = self.pos
		self.graphics.drawPixel(self.graphics.width-x-1,y, self.color)
	def setPos(self, pos):
		self.pos = (pos[1],pos[0])
	def getPos(self):
		return (self.pos[1],self.pos[0])

"""Player class handles how to player acts."""
class Player(TilePixel):
	def __init__(self, pos, color, graphics, game):
		TilePixel.__init__(self, pos, color, graphics)
		self.controller = PixelBrosController(0)
		self.game = game
		self.dx = 0
		self.dy = 0
	def handleInput(self):
		if self.controller.getDpad(self.controller.UP_DPAD):
			self.dy = -1
		elif self.controller.getDpad(self.controller.DOWN_DPAD):
			self.dy = 1
		else:
			self.dy = 0

		if self.controller.getDpad(self.controller.LEFT_DPAD):
			self.dx = -1
		elif self.controller.getDpad(self.controller.RIGHT_DPAD):
			self.dx = 1
		else:
			self.dx = 0

	def process(self):
		x,y = self.getPos()
		print self.dx,self.dy
		y += self.dy
		x += self.dx
		pos = x,y
		self.setPos(pos)

"""
SuperPixelBros is a class that hanles function calling and processing.
makes sure the level is generated.
makes sure the player get the right data.

"""
class SuperPixelBros(object):
	def __init__(self):
		self.graphics = Graphics(matrix_width, matrix_height)

		self.players = []
		self.player = Player((9,7), BLUE, self.graphics, self)

		self.level = level1

	def handleInput(self):
		self.player.handleInput()
	def process(self):
		self.player.process()
	def draw(self):
		self.graphics.fill(BLACK)
		#draw the map.
		level_matrix = self.graphics.toMatrix(self.level, self.graphics.getSurfaceHeight())
		for y in self.graphics.heightRange:
			for x in self.graphics.widthRange:
				tile = level_matrix[x][y]
				#draw the map flipped
				self.graphics.drawPixel(self.graphics.width-x-1,y, tile)

		#draw the player.
		self.player.draw()
	def generate(self):
		self.handleInput()
		self.process()
		self.draw()
		return self.graphics.getSurface()