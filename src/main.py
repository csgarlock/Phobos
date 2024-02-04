import sys, pygame
import math
import spritesheet
from constants.piecetype import PieceType
from constants.directions import Directions
from constants.specialmoves import SpecialMoves
from piece import *
from board import Board
from move import Move

def main():
	pygame.init()

	size = width, height = 640, 640
	screen = pygame.display.set_mode(size)

	move_surface = pygame.Surface((width,height), pygame.SRCALPHA)

	Piece.setup_sprites()

	board_imag = pygame.image.load("..\\res\\chessboard.png")
	board_rec = board_imag.get_rect()	

	board = Board(True)
	print(board.piece_relations.pins)

	held_piece = None
	mouse_pos = [0, 0]
	move_source_pos = [0, 0]

	while True:
		for event in pygame.event.get():
			if (event.type == pygame.MOUSEMOTION):
				mouse_pos = event.pos

			if (event.type == pygame.MOUSEBUTTONDOWN):
				if (event.button == 1):
					mouse_pos = event.pos
					move_source_pos = loc_to_pos(event.pos)
					piece_at_pos = board.get_piece_at(move_source_pos)
					if (piece_at_pos is not None):
						if (piece_at_pos.get_team() == board.get_turn()):
							held_piece = piece_at_pos
							piece_moves = board.get_piece_moves(held_piece)
					else:
						held_piece = None

			if (event.type == pygame.MOUSEBUTTONUP):
				if (event.button == 1 and held_piece is not None):
					mouse_pos = event.pos
					move_des_pos = loc_to_pos(event.pos)
					move_des_piece = board.get_piece_at(move_des_pos)
					board.try_move_piece(Move(held_piece, move_source_pos, move_des_pos, move_des_piece))
					held_piece = None

			if (event.type == pygame.QUIT):
				sys.exit()

		screen.fill("white")

		screen.blit(board_imag, board_rec)
		for piece in board.get_pieces():
			if (piece is held_piece):
				pass
			else:
				screen.blit(piece.get_image(), piece.get_rect())
		if (held_piece is not None):
			rect = pygame.Rect(0, 0, 80, 80)
			rect.center = (mouse_pos[0], mouse_pos[1])
			screen.blit(held_piece.get_image(), rect)

		move_surface.fill((0, 0, 0, 0))
		if (held_piece is not None):
			for move in board.get_all_moves():
				if (move.get_piece() == held_piece):
					des = move.get_des()
					circle_color = pygame.Color(100, 100, 100, 100)
					if (move.get_des_piece() is not None or move.get_special_move() == SpecialMoves.EN_PASSANT.value):
						circle_color = pygame.Color(242, 43, 0, 100)
					pygame.draw.circle(move_surface, circle_color, (40 + (80 * des[0]), 40 + (80 * des[1])), 20)

		screen.blit(move_surface, (0, 0))

		pygame.display.flip()


def loc_to_pos(loc):
	return (math.floor(loc[0]/80), math.floor(loc[1]/80))


if __name__ == '__main__':
	main()