import sys, pygame
from constants.piecetype import PieceType
from constants.directions import Directions
from piece import *
from move import Move


class Board:

	def __init__(self, starting = True, Board = None):
		self.pieces = []
		self.board_arr = [[None for i in range(8)] for j in range(8)]
		if (starting):
			#Fill the default starting board
			self.pieces.append(Rook(False, [0, 0]))
			self.pieces.append(Rook(False, [7, 0]))
			self.pieces.append(Rook(True, [0, 7]))
			self.pieces.append(Rook(True, [7, 7]))

			self.pieces.append(Knight(False, [1, 0]))
			self.pieces.append(Knight(False, [6, 0]))
			self.pieces.append(Knight(True, [1, 7]))
			self.pieces.append(Knight(True, [6, 7]))

			self.pieces.append(Bishop(False, [2, 0]))
			self.pieces.append(Bishop(False, [5, 0]))
			self.pieces.append(Bishop(True, [2, 7]))
			self.pieces.append(Bishop(True, [5, 7]))

			self.pieces.append(Queen(False, [3, 0]))
			self.pieces.append(Queen(True, [3, 7]))

			self.pieces.append(King(False, [4, 0]))
			self.pieces.append(King(True, [4, 7]))

			for i in range(0, 8):
				self.pieces.append(Pawn(False, [i, 1]))
				self.pieces.append(Pawn(True, [i, 6]))
		else:
			pass

		self.generated_moves = False
		self.moves = []

		for piece in self.pieces:
			position = piece.get_pos()
			self.board_arr[position[1]][position[0]] = piece

	def get_piece_at(self, pos):
		return self.board_arr[pos[1]][pos[0]]

	def get_all_moves(self):
		if (not self.generated_moves):
			for piece in self.pieces:
				self.moves.extend(self.get_piece_moves(piece))
			self.generated_moves = True
		return self.moves

	def get_piece_moves(self, piece):
		moves = []
		move_vectors = piece.get_move_vectors()
		move_length = piece.get_move_length()
		for direction in move_vectors:
			ray = cast_ray(piece, direction, move_length)


	def try_move_piece(self, move):
		piece = move.get_piece()
		source = move.get_source()
		self.board_arr[source[1]][source[0]] = None
		des = move.get_des()
		piece.move(des)
		self.board_arr[des[1]][des[0]] = piece

	def cast_ray(self, piece, direction, move_length):
		d_x, d_y = direction
		empty_positions = []
		current_position = [piece.get_pos()[0] + d_x, piece.get_pos()[1] + d_y]
		while (self.board_arr[current_position[1]][current_position[0]] is None and in_bounds(current_position)):
			empty_positions.append[current_position[0], current_position[1]]
			current_position[0] += d_x
			current_position[1] += d_y
		return (empty_positions, self.board_arr[current_position[1]][current_position[0]])

	def in_bounds(position):
		if(position[0] > 7 or position[0] < 0 or position[1] > 7 or position[1] < 0):
			return False
		return True


	def blit_pieces(self, screen, mouse_pos, held_piece):
		for piece in self.pieces:
			if (piece is held_piece):
				pass
			else:
				screen.blit(piece.get_image(), piece.get_rect())
		if (held_piece is not None):
			rect = pygame.Rect(0, 0, 80, 80)
			rect.center = (mouse_pos[0], mouse_pos[1])
			screen.blit(held_piece.get_image(), rect)
