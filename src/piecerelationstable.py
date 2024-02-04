from piece import *

class PieceRelationsTable:
	def __init__(self, board):
		self.board = board

		self.pins = {}
		self.hidden = {}
		self.attacks = {}
		self.defending = {}
		pieces = board.get_pieces()
		for piece in pieces:
			self.pins.update({piece.get_key() : [[], [], []]})
			self.hidden.update({piece.get_key() : [[], [], []]})
			self.attacks.update({piece.get_key() : [[], []]})
			self.defending.update({piece.get_key() : [[], []]})

		moves = board.get_all_moves()

		for piece in pieces:
			pass

	def update_from_move(self, move):
		self.update_pins(move)

	def update_pins(self, move)
		pass