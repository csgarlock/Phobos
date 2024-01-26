from piece import Piece
from constants.specialmoves import SpecialMoves

class Move:

	def __init__(self, piece, source, des, des_piece = None, special_move = SpecialMoves.NONE.value, special_piece = None):
		self.piece = piece
		self.source = source
		self.des = des
		self.des_piece = des_piece
		self.special_move = special_move
		self.special_piece = special_piece

	def __str__(self):
		if (self.special_move == SpecialMoves.SHORT_CASTLE.value):
			return (str(self.piece) + " castles short")
		elif(self.special_move == SpecialMoves.LONG_CASTLE.value):
			return (str(self.piece) + " castles long")
		elif(self.special_move == SpecialMoves.EN_PASSANT.value):
			return (str(self.piece) + " from " + str(self.source) + " to " + str(self.des) + " en passants " + str(self.special_piece))
		elif (self.des_piece is not None):
			return (str(self.piece) + " from " + str(self.source) + " to " + str(self.des) + " takes " + str(self.des_piece))
		else:
			return (str(self.piece) + " from " + str(self.source) + " to " + str(self.des))

	def __eq__(self, other):
		if not (self.piece == other.piece):
			return False
		if not (self.des_piece == other.des_piece):
			return False
		if (self.source[0] != other.source[0]) or (self.source[1] != other.source[1]):
			return False
		if (self.des[0] != other.des[0]) or (self.des[1] != other.des[1]):
			return False
		return True

	def get_piece(self):
		return self.piece

	def get_source(self):
		return self.source

	def get_des(self):
		return self.des

	def get_des_piece(self):
		return self.des_piece

	def get_special_move(self):
		return self.special_move

	def get_special_piece(self):
		return self.special_piece



