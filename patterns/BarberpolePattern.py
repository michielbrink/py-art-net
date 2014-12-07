# Barberpole pattern was originally made in C by Duality
class BarberpolePattern:
	# Rotating stripes of certain colors, default red/white
	def __init__(self, backwards=False, color1=(255, 0, 0), color2=(255, 255, 255)):
		self.backwards = backwards
		self.color1 = color1
		self.color2 = color2
		self.pos = 0
		
		self.width = 10
		self.height = 17
		self.size = self.width*self.height
	def generate(self):
		data = []
		if self.backwards:
			leds = xrange(self.size, 0, 1)
		else:
			leds = xrange(0, self.size, 1)
		for i in leds:
			place = (i % self.width) + self.pos
			if (place >= self.width):
				place -= self.width
			if (place < self.width/2):
				data.append(self.color1)
			else:
				data.append(self.color2)
		self.pos += 1
		if (self.pos >= self.width):
			self.pos = 0
		return data
