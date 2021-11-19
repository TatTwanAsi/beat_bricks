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
		self.name = 'heart'


	def get_name(self):

		"""返回道具名称"""
		return self.name


class PropLengthen(Sprite):

	"""管理增长挡板的道具"""
	def __init__(self, size, location):
		
		"""初始化增长挡板道具"""
		super().__init__()
		self.image = pygame.image.load("images/lengthen.png")
		self.image = pygame.transform.scale(self.image, size)
		self.rect = self.image.get_rect()
		self.rect.midtop = location
		self.name = 'lengthen'


	def get_name(self):

		"""返回道具名称"""
		return self.name


class PropLock(Sprite):

	"""管理锁道具的类"""
	def __init__(self, size, location):
		
		"""初始化锁道具"""
		super().__init__()
		self.image = pygame.image.load("images/lock.png")
		self.image = pygame.transform.scale(self.image, size)
		self.rect = self.image.get_rect()
		self.rect.midtop = location
		self.name = 'lock'


	def get_name(self):

		"""返回道具名称"""
		return self.name


class PropThroughWall(Sprite):

	"""管理穿墙道具的类"""
	def __init__(self, size, location):
		
		"""初始化穿墙道具"""
		super().__init__()
		self.image = pygame.image.load("images/ThroughWall.png")
		self.image = pygame.transform.scale(self.image, size)
		self.rect = self.image.get_rect()
		self.rect.midtop = location
		self.name = 'through_wall'


	def get_name(self):

		"""返回道具名称"""
		return self.name


class PropTurtle(Sprite):

	"""管理乌龟道具的类"""
	def __init__(self, size, location):
		
		"""初始化乌龟道具"""
		super().__init__()
		self.image = pygame.image.load("images/turtle.png")
		self.image = pygame.transform.scale(self.image, size)
		self.rect = self.image.get_rect()
		self.rect.midtop = location
		self.name = 'turtle'


	def get_name(self):

		"""返回道具名称"""
		return self.name