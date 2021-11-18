import pygame
from pygame.sprite import Sprite

class PropHeart(Sprite):

	"""管理心道具的类"""
	def __init__(self, size, location):
		
		"""初始化心道具"""
		super().__init__()
		self.image = pygame.image.load("images/heart.png")
		self.image = pygame.transform.scale(self.image, size)
		self.rect = self.image.get_rect()
		self.rect.midtop = location


class PropLengthen(Sprite):

	"""管理增长挡板的道具"""
	def __init__(self, size, location):
		
		"""初始化增长挡板道具"""
		super().__init__()
		self.image = pygame.image.load("images/lengthen.png")
		self.image = pygame.transform.scale(self.image, size)
		self.rect = self.image.get_rect()
		self.rect.midtop = location


class PropLock(Sprite):

	"""管理锁道具的类"""
	def __init__(self, size, location):
		
		"""初始化锁道具"""
		super().__init__()
		self.image = pygame.image.load("images/lock.png")
		self.image = pygame.transform.scale(self.image, size)
		self.rect = self.image.get_rect()
		self.rect.midtop = location


class PropThroughWall(Sprite):

	"""管理穿墙道具的类"""
	def __init__(self, size, location):
		
		"""初始化穿墙道具"""
		super().__init__()
		self.image = pygame.image.load("images/ThroughWall.png")
		self.image = pygame.transform.scale(self.image, size)
		self.rect = self.image.get_rect()
		self.rect.midtop = location


class PropTurtle(Sprite):

	"""管理乌龟道具的类"""
	def __init__(self, size, location):
		
		"""初始化乌龟道具"""
		super().__init__()
		self.image = pygame.image.load("images/turtle.png")
		self.image = pygame.transform.scale(self.image, size)
		self.rect = self.image.get_rect()
		self.rect.midtop = location