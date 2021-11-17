import pygame

class Board:

	"""管理板子的类"""
	def __init__(self, width, height, color, location):

		"""初始化板子"""
		self.rect = pygame.Rect(0, 0, width, height)
		self.rect.midbottom = location
		self.color = color