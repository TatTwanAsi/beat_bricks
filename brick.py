import pygame
from pygame.sprite import Sprite

YELLOW = (249, 174, 87)
RED = (221, 81, 69)

class Brick(Sprite):

	"""表示单个砖块的类"""
	def __init__(self, width, height, color, location, max_hit_num):

		"""初始化砖块并设置其位置"""
		super().__init__()
		self.image = pygame.Surface((width, height))
		self.color = color
		self.image.fill(self.color)
		self.rect = self.image.get_rect()
		self.rect.midtop = location
		self.hit_num = 0				# 被撞到了0次
		self.max_hit_num = max_hit_num	# 最大撞击次数


	def hit(self):

		# 砖块被撞，状态更新
		self.hit_num += 1
		if self.hit_num >= self.max_hit_num:
			self.kill()

		elif self.hit_num == 1:
			# 若没有死，改变砖块颜色
			self.image.fill(YELLOW)

		elif self.hit_num == 2:
			self.image.fill(RED)