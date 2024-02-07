from piece import *
from piecerelations.attack import Attack
from piecerelations.defending import Defending 
from piecerelations.hidden import Hidden
from piecerelations.pin import Pin

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

		for piece in pieces:
			look_results = board.look_directions(piece, piece.get_attack_vectors(), piece.get_attack_length())
			for result in look_results:
				other_piece = result[0]
				direction = result[1]
				if (piece.on_same_team(other_piece)):
					defense = Defending(piece, other_piece, direction)
					self.defending[piece.get_key()][0].append(defense)
					self.defending[other_piece.get_key()][1].append(defense)
				else:
					attack = Attack(piece, other_piece, direction)
					self.attacks[piece.get_key()][0].append(attack)
					self.attacks[other_piece.get_key()][1].append(attack)
		for piece in pieces:
			if (piece.get_move_length() == -1):
				for defense in self.defending[piece.get_key()][0]:
					other_piece = defense.get_defended()
					direction = defense.get_direction()
					look_result = board.look_directions(other_piece, [direction], -1)
					if(len(look_result) == 1):
						threated_piece = look_result[0][0]
						if (not piece.on_same_team(threated_piece)):
							hidden = Hidden(piece, other_piece, threated_piece, direction)
							self.hidden[piece.get_key()][0].append(hidden)
							self.hidden[other_piece.get_key()][1].append(hidden)
							self.hidden[threated_piece.get_key()][2].append(hidden)
				for attack in self.attacks[piece.get_key()][0]:
					other_piece = attack.get_attacked()
					direction = attack.get_direction()
					look_result = board.look_directions(other_piece, [direction], -1)
					if(len(look_result == 1)):
						threated_piece = look_result[0][0]
						if (piece.on_same_team(threated_piece)):
							pin = Pin(piece, other_piece, threated_piece, direction)
							self.pins[piece.get_key()][0].append(pin)
							self.pins[other_piece.get_key()][1].append(pin)
							self.pins[threated_piece.get_key()][2].append(pin)

	def update_from_move(self, move):
		pass