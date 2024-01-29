import sys, pygame
from constants.piecetype import PieceType
from constants.directions import Directions
from constants.specialmoves import SpecialMoves
from teaminfo import TeamInfo
from piece import *
from move import Move


class Board:

	def __init__(self, starting = True, Board = None):
		self.pieces = []
		self.board_arr = [[None for i in range(8)] for j in range(8)]
		self.turn = PieceType.WHITE.value
		self.en_passant_target = None
		if (starting):

			#Fill the default starting board
			self.pieces.append(Rook(PieceType.BLACK.value, [0, 0]))
			self.pieces.append(Rook(PieceType.BLACK.value, [7, 0]))
			self.pieces.append(Rook(PieceType.WHITE.value, [0, 7]))
			self.pieces.append(Rook(PieceType.WHITE.value, [7, 7]))

			self.pieces.append(Knight(PieceType.BLACK.value, [1, 0]))
			self.pieces.append(Knight(PieceType.BLACK.value, [6, 0]))
			self.pieces.append(Knight(PieceType.WHITE.value, [1, 7]))
			self.pieces.append(Knight(PieceType.WHITE.value, [6, 7]))

			self.pieces.append(Bishop(PieceType.BLACK.value, [2, 0]))
			self.pieces.append(Bishop(PieceType.BLACK.value, [5, 0]))
			self.pieces.append(Bishop(PieceType.WHITE.value, [2, 7]))
			self.pieces.append(Bishop(PieceType.WHITE.value, [5, 7]))

			self.pieces.append(Queen(PieceType.BLACK.value, [3, 0]))
			self.pieces.append(Queen(PieceType.WHITE.value, [3, 7]))

			self.pieces.append(King(PieceType.BLACK.value, [4, 0]))
			self.pieces.append(King(PieceType.WHITE.value, [4, 7]))

			for i in range(0, 8):
				self.pieces.append(Pawn(PieceType.BLACK.value, [i, 1]))
				self.pieces.append(Pawn(PieceType.WHITE.value, [i, 6]))
		else:
			pass

		self.team_info = [TeamInfo(PieceType.WHITE.value, board), TeamInfo(PieceType.BLACK.value, board)]

		self.generated_moves = False
		self.moves = []

		for piece in self.pieces:
			position = piece.get_pos()
			self.board_arr[position[1]][position[0]] = piece

	def get_piece_at(self, pos):
		return self.board_arr[pos[1]][pos[0]]

	def get_pieces(self):
		return self.pieces

	def get_turn(self):
		return self.turn

	def try_move_piece(self, move):
		for valid_move in self.get_all_moves():
			if (move == valid_move):
				self.make_move(valid_move)
				return

	def make_move(self, move):
		print(move)
		piece = move.get_piece()
		source = move.get_source()
		special_move = move.get_special_move()
		special_piece = move.get_special_piece()
		des = move.get_des()
		if (special_move == SpecialMoves.NONE.value):
			self.board_arr[source[1]][source[0]] = None
			piece.move(des)
			if (move.get_des_piece() is not None):
				self.pieces.remove(move.get_des_piece())
			self.board_arr[des[1]][des[0]] = piece
		elif (special_move == SpecialMoves.PAWN_CAPTURE.value):
			self.board_arr[source[1]][source[0]] = None
			piece.move(des)
			if (move.get_des_piece() is not None):
				self.pieces.remove(move.get_des_piece())
			self.board_arr[des[1]][des[0]] = piece
		elif (special_move == SpecialMoves.SHORT_CASTLE.value or special_move == SpecialMoves.LONG_CASTLE.value):
			self.board_arr[source[1]][source[0]] = None
			piece.move(des)
			self.board_arr[des[1]][des[0]] = piece
			special_des = [0, 7*(1 - special_piece.get_team())]
			if (special_move == SpecialMoves.SHORT_CASTLE.value):
				special_des[0] = 5
			else:
				special_des[0] = 3
			special_piece.move(special_des)
			self.board_arr[special_des[1]][special_des[0]] = special_piece
		elif (special_move == SpecialMoves.EN_PASSANT.value):
			self.board_arr[source[1]][source[0]] = None
			piece.move(des)
			self.board_arr[des[1]][des[0]] = piece
			special_piece_pos = special_piece.get_pos()
			self.pieces.remove(special_piece)
			self.board_arr[special_piece_pos[1]][special_piece_pos[0]] = None

		if (isinstance(piece, Pawn)):
			if (abs(source[1] - des[1]) == 2):
				self.en_passant_target = piece
				print(self.en_passant_target)
			else:
				self.en_passant_target = None
		else:
			self.en_passant_target = None
		self.team_info[self.turn].update_from_move(move)
		self.moves = []
		self.generated_moves = False
		#Swithes whose turn it is
		self.turn = 1 - self.turn

	def get_all_moves(self):
		if (not self.generated_moves):
			for piece in self.pieces:
				if (piece.get_team() == self.turn):
					self.moves.extend(self.get_piece_moves(piece))
			self.generated_moves = True
		return self.moves

	def get_piece_moves(self, piece):
		piece_pos = piece.get_pos()
		moves = []
		move_vectors = piece.get_move_vectors()
		move_length = piece.get_move_length()
		if (isinstance(piece, Pawn)):
			attack_vectors = []
			if (piece.get_team() == PieceType.WHITE.value):
				attack_vectors = [Directions.UP_RIGHT, Directions.UP_LEFT]
			else:
				attack_vectors = [Directions.DOWN_RIGHT, Directions.DOWN_LEFT]
			right_attack_ray = self.cast_ray(piece, attack_vectors[0], 1)
			right_attack_des_piece = right_attack_ray[1]
			if (right_attack_des_piece is not None):
				if (not right_attack_des_piece.on_same_team(piece)):
					moves.append(Move(piece, piece_pos, right_attack_des_piece.get_pos(), right_attack_des_piece, SpecialMoves.PAWN_CAPTURE.value))
			left_attack_ray = self.cast_ray(piece, attack_vectors[1], 1)
			left_attack_des_piece = left_attack_ray[1]
			if (left_attack_des_piece is not None):
				if (not left_attack_des_piece.on_same_team(piece)):
					moves.append(Move(piece, piece_pos, left_attack_des_piece.get_pos(), left_attack_des_piece, SpecialMoves.PAWN_CAPTURE.value))

			if(self.en_passant_target is not None):
				en_passant_target_pos = self.en_passant_target.get_pos()
				if (en_passant_target_pos[1] == piece_pos[1]):
					en_passant_vector = []
					if (en_passant_target_pos[0] == piece_pos[0] - 1):
						en_passant_vector = (-1, piece.get_move_vectors()[0][1])
					elif (en_passant_target_pos[0] == piece_pos[0] + 1):
						en_passant_vector = (1, piece.get_move_vectors()[0][1])
					if (en_passant_vector != []):
						en_passant_des = [piece_pos[0] + en_passant_vector[0], piece_pos[1] + en_passant_vector[1]]
						moves.append(Move(piece, piece_pos, en_passant_des, None, SpecialMoves.EN_PASSANT.value, self.en_passant_target))


		if (isinstance(piece, King)):
			if (not piece.get_has_moved()):
				right_castle_ray = self.cast_ray(piece, Directions.RIGHT, -1)
				right_castle_des_piece = right_castle_ray[1]
				if (isinstance(right_castle_des_piece, Rook)):
					if (not right_castle_des_piece.get_has_moved()):
						moves.append(Move(piece, piece_pos, [6, 7*(1 - piece.get_team())], None, SpecialMoves.SHORT_CASTLE.value, right_castle_des_piece))
				left_castle_ray = self.cast_ray(piece, Directions.LEFT, -1)
				left_castle_des_piece = left_castle_ray[1]
				if (isinstance(left_castle_des_piece, Rook)):
					if (not left_castle_des_piece.get_has_moved()):
						moves.append(Move(piece, piece_pos, [2, 7*(1 - piece.get_team())], None, SpecialMoves.LONG_CASTLE.value, left_castle_des_piece))
		for direction in move_vectors:
			ray = self.cast_ray(piece, direction, move_length)
			found_empties, des_piece = ray
			for empty in found_empties:
				moves.append(Move(piece, piece_pos, empty))
			if (des_piece is not None and not isinstance(piece, Pawn)):
				if (piece.on_same_team(des_piece) == False):	
					moves.append(Move(piece, piece_pos, des_piece.get_pos(), des_piece))

		return moves

	def cast_ray(self, piece, direction, move_length):
		d_x, d_y = direction
		empty_positions = []
		current_position = [piece.get_pos()[0] + d_x, piece.get_pos()[1] + d_y]
		distance_traveled = 0
		if (self.in_bounds(current_position) == True):
			while (self.board_arr[current_position[1]][current_position[0]] is None):
				distance_traveled += 1
				empty_positions.append([current_position[0], current_position[1]])
				current_position[0] += d_x
				current_position[1] += d_y
				if (distance_traveled == move_length):
					return (empty_positions, None)
				if (self.in_bounds(current_position) == False):
					return (empty_positions, None)
		else:
			return (empty_positions, None)
		return (empty_positions, self.board_arr[current_position[1]][current_position[0]])


	def in_bounds(self, position):
		if(position[0] > 7 or position[0] < 0 or position[1] > 7 or position[1] < 0):
			return False
		return True

