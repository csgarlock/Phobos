import sys, pygame
from piecetype import PieceType
from piece import Piece


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

		for piece in self.pieces:
			position = piece.get_pos()
			self.board_arr[position[1]][position[0]] = piece

	def get_piece_at(self, pos):
		return self.board_arr[pos[1]][pos[0]]

	def try_move_piece(self, source, des, piece):
		piece = self.board_arr[source[1]][source[0]]
		self.board_arr[source[1]][source[0]] = None
		piece.move(des)
		self.board_arr[des[1]][des[0]] = piece

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
