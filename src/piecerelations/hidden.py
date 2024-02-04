class Hidden:
	def __init__(self, masked, concealer, threatened, direction):
		self.masked = masked
		self.concealer = concealer
		self.threatened = threatened
		self.direction = direction

	def get_masked(self):
		return self.masked

	def get_concealer(self):
		return self.concealer

	def get_threatened(self):
		return self.threatened

	def get_direction(self):
		return self.direction


