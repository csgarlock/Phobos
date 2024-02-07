class Attack:
	def __init__(self, threat, attacked, direction):
		self.threat = threat
		self.attacked = attacked
		self.direction = direction

	def __str__(self):
		return str(self.threat) + " attacking " + str(self.attacked)

	def get_threat(self):
		return self.threat

	def get_attacked(self):
		return self.attacked

	def get_direction(self):
		return self.direction