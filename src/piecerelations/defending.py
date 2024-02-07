class Defending:

	def __init__(self, guard, defended, direction):
		self.guard = guard
		self.defended = defended
		self.direction = direction

	def __str__(self):
		return str(self.guard) + " Defending " + str(self.defended)

	def get_guard(self):
		return self.guard

	def get_defended(self):
		return self.defended

	def get_direction(self):
		return self.direction		