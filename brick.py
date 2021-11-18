import pygame
from pygame.sprite import Sprite

class Brick(Sprite):

	"""表示单个砖块的类"""
	def __init__(self, width, height, color, location):

		"""初始化砖块并设置其位置"""
		super().__init__()
		self.image = pygame.Surface((width, height))
		self.image.fill(color)
		self.rect = self.image.get_rect()
		self.rect.midtop = location