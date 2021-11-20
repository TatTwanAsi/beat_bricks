import pygame
from pygame.sprite import Sprite


class UIElement(Sprite):

	"""UI元素的类"""
	def __init__(self, surface, rect):

		"""初始化"""
		super().__init__()
		self.image = surface
		self.rect = rect