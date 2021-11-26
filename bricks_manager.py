import pygame

from brick import Brick


class BricksManager:

	"""管理砖块的类"""

	def __init__(self, game):
		
		"""初始化"""

		# 墙的行数和列数
		self.row = game.settings.row
		self.column = game.settings.column

		# 墙上一个单元在x，y上的大小
		self.unit_y = (float(game.screen_height)/2)/(float(self.row)+1)
		self.unit_x = float(game.screen_width)/(float(self.column)+1)

		# 砖块的参数
		self.brick_width = game.settings.brick_width
		self.brick_height = game.settings.brick_height
		self.brick_color = game.settings.brick_color
		self.max_hit_num = game.settings.brick_max_hit_num

		self.bricks = pygame.sprite.Group() # 砖块的编组

		self._fill_wall_with_bricks()		# 在墙上铺满砖块


	def _fill_wall_with_bricks(self):
		
		"""在墙上铺满砖块"""
		for row_num in range(self.row):
			for column_num in range(self.column):
				location = ((column_num + 1.0)*self.unit_x, 20 + (row_num + 1.0)*self.unit_y)
				#if column_num == 4 and row_num == 6:
				#	brick = Brick(self.brick_width, self.brick_height, (153, 199, 148), location, self.max_hit_num)
				#elif column_num == 2 and row_num == 3:
				#	brick = Brick(self.brick_width, self.brick_height, (201, 205, 227), location, self.max_hit_num)
				#else:
				brick = Brick(self.brick_width, self.brick_height, self.brick_color, location, self.max_hit_num)
				self.bricks.add(brick)