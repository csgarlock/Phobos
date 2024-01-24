import pygame
import spritesheet
from constants.piecetype import PieceType
from constants.directions import Directions


class Piece():

	def setup_sprites():
		global chroma_key
		chroma_key = pygame.Color(0, 140, 10)

		global piece_sheet
		piece_sheet = spritesheet.spritesheet("..\\res\\piece_spritesheet.png")

		global piece_locs
		piece_locs = [
		(0, 0, 80, 80), (80, 0, 80, 80), (160, 0, 80, 80), (240, 0, 80, 80), (320, 0, 80, 80), (400, 0, 80, 80),
		(0, 80, 80, 80), (80, 80, 80, 80), (160, 80, 80, 80), (240, 80, 80, 80), (320, 80, 80, 80), (400, 80, 80, 80)]

	def __init__(self, piece_type, team, position, graphical=True, move_vectors = [], move_length = -1):
		self.piece_type = piece_type
		self.position = position
		self.team = team
		self.move_vectors = move_vectors
		self.move_length = move_length
		if (graphical):
			self.rect = pygame.Rect(position[0] * 80, position[1] * 80, 80, 80)
			if (self.team == PieceType.WHITE.value):
				self.image = piece_sheet.image_at(piece_locs[piece_type], chroma_key)
			else:
				self.image = piece_sheet.image_at(piece_locs[piece_type+6], chroma_key)
			self.held = False

	def __str__(self):
		color = "White" if self.team == PieceType.WHITE.value else "Black"
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

	def __eq__(self, other):
		if not isinstance(other, Piece):
			return False
		if ((self.piece_type != other.piece_type) or (self.team != other.get_team())):
			return False
		if ((self.position[0] != other.position[0]) or (self.position[1] != other.position[1])):
			return False
		return True

	def move(self, des):
		self.position = [des[0], des[1]]

	def get_move_vectors(self):
		return self.move_vectors

	def get_move_length(self):
		return self.move_length

	def on_same_team(self, other):
		return self.team == other.get_team()

	def get_pos(self):
		return self.position

	def get_rect(self):
		self.rect.topleft = [self.position[0] * 80, self.position[1] * 80]
		return self.rect

	def get_image(self):
		return self.image

	def get_team(self):
		return self.team

	def get_piece_type(self):
		return (self.piece_type, self.team)


class King(Piece):

	def __init__(self, team, position, graphical=True):
		self.has_moved = False
		move_vectors = [
			Directions.UP, 
			Directions.UP_RIGHT,
			Directions.RIGHT,
			Directions.DOWN_RIGHT,
			Directions.DOWN,
			Directions.DOWN_LEFT,
			Directions.LEFT,
			Directions.UP_LEFT
		]
		move_length = 1
		super().__init__(PieceType.KING.value, team, position, graphical, move_vectors, move_length)

	def get_has_moved(self):
		return self.has_moved

	def move(self, des):
		self.has_moved = True
		super().move(des)

class Queen(Piece):

	def __init__(self, team, position, graphical=True):
		move_vectors = [
			Directions.UP, 
			Directions.UP_RIGHT,
			Directions.RIGHT,
			Directions.DOWN_RIGHT,
			Directions.DOWN,
			Directions.DOWN_LEFT,
			Directions.LEFT,
			Directions.UP_LEFT
		]
		move_length = -1
		super().__init__(PieceType.QUEEN.value, team, position, graphical, move_vectors, move_length)

class Bishop(Piece):

	def __init__(self, team, position, graphical=True):
		move_vectors = [ 
			Directions.UP_RIGHT,
			Directions.DOWN_RIGHT,
			Directions.DOWN_LEFT,
			Directions.UP_LEFT
		]
		move_length = -1
		super().__init__(PieceType.BISHOP.value, team, position, graphical, move_vectors, move_length)

class Rook(Piece):

	def __init__(self, team, position, graphical=True):
		self.has_moved = False
		move_vectors = [ 
			Directions.UP,
			Directions.RIGHT,
			Directions.DOWN,
			Directions.LEFT,
		]
		move_length = -1
		super().__init__(PieceType.ROOK.value, team, position, graphical, move_vectors, move_length)

	def get_has_moved(self):
		return self.has_moved

	def move(self, des):
		self.has_moved = True
		super().move(des)

class Knight(Piece):

	def __init__(self, team, position, graphical=True):
		move_vectors = Directions.KNIGHT_VECTORS
		move_length = 1
		super().__init__(PieceType.KNIGHT.value, team, position, graphical, move_vectors, move_length)

class Pawn(Piece):

	def __init__(self, team, position, graphical=True):
		self.has_moved = False
		move_vectors = []
		if (team == PieceType.WHITE.value):
			move_vectors = [Directions.UP]
		else :
			move_vectors = [Directions.DOWN]
		move_length = 2
		super().__init__(PieceType.PAWN.value, team, position, graphical, move_vectors, move_length)

	def get_has_moved(self):
		return self.has_moved

	def move(self, des):
		self.has_moved = True
		self.move_length = 1
		super().move(des)

	def get_move_length(self):
		return self.move_length
