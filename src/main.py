import sys, pygame
import math
import spritesheet
from constants.piecetype import PieceType
from constants.directions import Directions
from piece import Piece
from board import Board
from move import Move

def main():
	pygame.init()

	size = width, height = 640, 640
	screen = pygame.display.set_mode(size)

	Piece.setup_sprites()

	board_imag = pygame.image.load("..\\res\\chessboard.png")
	board_rec = board_imag.get_rect()

	board = Board(True)

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
						held_piece = piece_at_pos
					else:
						held_piece = None

			if (event.type == pygame.MOUSEBUTTONUP):
				if (event.button == 1 and held_piece is not None):
					mouse_pos = event.pos
					move_des_pos = loc_to_pos(event.pos)
					board.try_move_piece(Move(held_piece, move_source_pos, move_des_pos))
					print(Move(held_piece, move_source_pos, move_des_pos))
					held_piece = None

			if (event.type == pygame.QUIT):
				sys.exit()

		screen.fill("white")

		screen.blit(board_imag, board_rec)
		board.blit_pieces(screen, mouse_pos, held_piece)

		pygame.display.flip()


def loc_to_pos(loc):
	return (math.floor(loc[0]/80), math.floor(loc[1]/80))


if __name__ == '__main__':
	main()