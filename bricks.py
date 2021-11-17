import pygame
from pygame.sprite import Sprite

class Bricks(Sprite):

	"""表示单个砖块的类"""
	def __init__(self, width, height, location):

		"""初始化砖块并设置其位置"""
		super().__init__()
		self.surface = pygame.Surface((width, heigth))