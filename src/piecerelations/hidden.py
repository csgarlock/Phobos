class Hidden:
	def __init__(self, masked, concealer, threatened, direction):
		self.masked = masked
		self.concealer = concealer
		self.threatened = threatened
		self.direction = direction


	def __str__(self):
		return str(self.masked) + " Attacking " + str(self.threatened) + " concealed by " + str(self.concealer)

	def get_masked(self):
		return self.masked

	def get_concealer(self):
		return self.concealer

	def get_threatened(self):
		return self.threatened

	def get_direction(self):
		return self.direction


