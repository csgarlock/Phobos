import pygame
import spritesheet
from piecetype import PieceType

class Piece:

	def setup_sprites():
		global chroma_key
		chroma_key = pygame.Color(0, 140, 10)

		global piece_sheet
		piece_sheet = spritesheet.spritesheet("..\\res\\piece_spritesheet.png")

		global piece_locs
		piece_locs = [
		(0, 0, 80, 80), (80, 0, 80, 80), (160, 0, 80, 80), (240, 0, 80, 80), (320, 0, 80, 80), (400, 0, 80, 80),
		(0, 80, 80, 80), (80, 80, 80, 80), (160, 80, 80, 80), (240, 80, 80, 80), (320, 80, 80, 80), (400, 80, 80, 80)]

	def __init__(self, piece_type, is_white, position, graphical=True):
		self.piece_type = piece_type
		self.position = position
		self.is_white = is_white
		if (graphical):
			self.rect = pygame.Rect(position[0] * 80, position[1] * 80, 80, 80)
			if (is_white):
				self.image = piece_sheet.image_at(piece_locs[piece_type], chroma_key)
			else:
				self.image = piece_sheet.image_at(piece_locs[piece_type+6], chroma_key)
			self.held = False

	def __str__(self):
		color = "White" if self.is_white else "Black"
		piece = ""
		if(self.piece_type == 0):
			piece = "King"
		elif (self.piece_type == 1):
			piece = "Queen"
		elif (self.piece_type == 2):
			piece = "Bishop"
		elif (self.piece_type == 3):
			piece = "Knight"
		elif (self.piece_type == 4):
			piece = "Rook"
		else:
			piece = "Pawn"
		return color + " " + piece

	def move(self, des):
		self.position = des

	def get_pos(self):
		return self.position

	def get_rect(self):
		self.rect.topleft = [self.position[0] * 80, self.position[1] * 80]
		return self.rect

	def get_image(self):
		return self.image

