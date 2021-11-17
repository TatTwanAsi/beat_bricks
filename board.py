import pygame

class Board:

	"""管理板子的类"""
	def __init__(self, width, height, color, location):

		"""初始化板子"""
		self.surface = pygame.Surface((width, height))
		self.rect = self.surface.get_rect()
		self.rect.midbottom = location
		self.color = color