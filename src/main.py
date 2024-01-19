import sys, pygame
import spritesheet
from piecetype import PieceType
from piece import Piece
from board import Board

def main():
	pygame.init()

	size = width, height = 640, 640
	screen = pygame.display.set_mode(size)

	Piece.setup_sprites()

	board_imag = pygame.image.load("..\\res\\chessboard.png")
	board_rec = board_imag.get_rect()

	board = Board(True)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()

		screen.fill("white")

		screen.blit(board_imag, board_rec)
		board.blit_pieces(screen)

		pygame.display.flip()



if __name__ == '__main__':
	main()