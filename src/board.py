import sys, pygame
from constants.piecetype import PieceType
from constants.directions import Directions
from piece import Piece
from move import Move


class Board:

	def __init__(self, starting = True, Board = None):
		self.pieces = []
		self.board_arr = [[None for i in range(8)] for j in range(8)]
		if (starting):
			#Fill the default starting board
			self.pieces.append(Piece(PieceType.ROOK.value, False, [0, 0]))
			self.pieces.append(Piece(PieceType.ROOK.value, False, [7, 0]))
			self.pieces.append(Piece(PieceType.ROOK.value, True, [0, 7]))
			self.pieces.append(Piece(PieceType.ROOK.value, True, [7, 7]))

			self.pieces.append(Piece(PieceType.KNIGHT.value, False, [1, 0]))
			self.pieces.append(Piece(PieceType.KNIGHT.value, False, [6, 0]))
			self.pieces.append(Piece(PieceType.KNIGHT.value, True, [1, 7]))
			self.pieces.append(Piece(PieceType.KNIGHT.value, True, [6, 7]))

			self.pieces.append(Piece(PieceType.BISHOP.value, False, [2, 0]))
			self.pieces.append(Piece(PieceType.BISHOP.value, False, [5, 0]))
			self.pieces.append(Piece(PieceType.BISHOP.value, True, [2, 7]))
			self.pieces.append(Piece(PieceType.BISHOP.value, True, [5, 7]))

			self.pieces.append(Piece(PieceType.QUEEN.value, False, [3, 0]))
			self.pieces.append(Piece(PieceType.QUEEN.value, True, [3, 7]))

			self.pieces.append(Piece(PieceType.KING.value, False, [4, 0]))
			self.pieces.append(Piece(PieceType.KING.value, True, [4, 7]))

			for i in range(0, 8):
				self.pieces.append(Piece(PieceType.PAWN.value, False, [i, 1]))
				self.pieces.append(Piece(PieceType.PAWN.value, True, [i, 6]))
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
		piece_type, is_white = piece.get_piece_type()
		if (piece_type == PieceType.PAWN.value):
			pass

		if (piece_type == PieceType.KNIGHT.value):
			pass

		if (piece_type == PieceType.BISHOP.value):
			pass

		if (piece_type == PieceType.QUEEN.value):
			pass

		if (piece_type == PieceType.ROOK.value):
			pass

		if (piece_type == PieceType.KING.value):
			pass

		return []

	def try_move_piece(self, move):
		piece = move.get_piece()
		source = move.get_source()
		self.board_arr[source[1]][source[0]] = None
		des = move.get_des()
		piece.move(des)
		self.board_arr[des[1]][des[0]] = piece

	def cast_ray(self, piece, direction):
		d_x, d_y = direction
		empty_positions = []
		current_position = [piece.get_pos()[0] + d_x, piece.get_pos()[1] + d_y]
		while (self.board_arr[current_position[1]][current_position[0]] is None):
			empty_positions.append[current_position[0], current_position[1]]
			current_position[0] += d_x
			current_position[1] += d_y
		return (empty_positions, self.board_arr[current_position[1]][current_position[0]])


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
