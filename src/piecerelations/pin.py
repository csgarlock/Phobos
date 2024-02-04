class Pin:
	def __init__(self, threat, pinned, attacked, direction):
		self.threat = threat
		self.pinned = pinned
		self.attacked = attacked
		self.direction = direction

	def get_threat(self):
		return self.threat

	def get_pinned(self):
		return self.pinned

	def get_attacked(self):
		return self.attacked

	def get_direction(self):
		return self.direction