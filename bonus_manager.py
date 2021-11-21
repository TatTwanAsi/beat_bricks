import pygame
import random

from bonus import PropHeart, PropLengthen, PropLock, PropThroughWall, PropTurtle


class BonusManager:

	"""管理所有道具的类"""
	def __init__(self, game):

		"""初始化"""
		# 墙的行和列
		self.row = game.settings.row
		self.column = game.settings.column
		# 墙上每个单元格在x，y上的大小
		self.unit_y = (float(game.settings.screen_height)/2)/(float(self.row)+1)
		self.unit_x = float(game.settings.screen_width)/(float(self.column)+1)
		self.bonus = pygame.sprite.Group()	# 创建一个空的道具编组
		self.bonus_locations = []			# 存放各个道具的位置，防止生成的道具位置重叠
		# 各个道具的个数
		self.heart_num = game.settings.heart_num
		self.lengthen_num = game.settings.lengthen_num
		self.lock_num = game.settings.lock_num
		self.turtle_num = game.settings.turtle_num
		self.through_wall_num = game.settings.through_wall_num
		# 各个道具的大小
		self.heart_size = (game.settings.heart_width, game.settings.heart_height)
		self.lengthen_size = (game.settings.lengthen_width, game.settings.lengthen_height)
		self.lock_size = (game.settings.lock_width, game.settings.lock_height)
		self.through_wall_size = (game.settings.through_wall_width, game.settings.through_wall_height)
		self.turtle_size = (game.settings.turtle_width, game.settings.turtle_height)
		self._generate_bonus()	# 生成道具


	def _generate_bonus(self):

		"""生成五种道具"""
		self._generate_heart()
		self._generate_lengthen()
		self._generate_lock()
		self._generate_turtle()
		self._generate_through_wall()


	def _generate_heart(self):

		"""生成心道具"""
		for num in range(self.heart_num):
			while True:
				# 生成两个随机数，分别代表道具的行和列，
				column_num = random.randint(0, self.column-1)
				row_num = random.randint(0, self.row-1)

				# 检查所生成的位置是否已被其他道具占有
				# 若是，则更换位置
				# 直到与其他道具位置不冲突位置
				if (column_num, row_num) not in self.bonus_locations:
					self.bonus_locations.append((column_num, row_num))
					location = ((column_num + 1.0)*self.unit_x, (row_num + 2.0)*self.unit_y)
					heart = PropHeart(self.heart_size, location)
					self.bonus.add(heart)
					break


	def _generate_lengthen(self):

		"""生成增长道具"""
		for num in range(self.lengthen_num):
			while True:
				# 生成两个随机数，分别代表道具的行和列，
				column_num = random.randint(0, self.column-1)
				row_num = random.randint(0, self.row-1)

				# 检查所生成的位置是否已被其他道具占有
				# 若是，则更换位置
				# 直到与其他道具位置不冲突位置
				if (column_num, row_num) not in self.bonus_locations:
					self.bonus_locations.append((column_num, row_num))
					location = ((column_num + 1.0)*self.unit_x, (row_num + 2.0)*self.unit_y)
					lengthen = PropLengthen(self.heart_size, location)
					self.bonus.add(lengthen)
					break


	def _generate_lock(self):
		
		"""生成琐道具"""
		for num in range(self.lock_num):
			while True:
				# 生成两个随机数，分别代表道具的行和列，
				column_num = random.randint(0, self.column-1)
				row_num = random.randint(0, self.row-1)

				# 检查所生成的位置是否已被其他道具占有
				# 若是，则更换位置
				# 直到与其他道具位置不冲突位置
				if (column_num, row_num) not in self.bonus_locations:
					self.bonus_locations.append((column_num, row_num))
					location = ((column_num + 1.0)*self.unit_x, (row_num + 2.0)*self.unit_y)
					lock = PropLock(self.lock_size, location)
					self.bonus.add(lock)
					break


	def _generate_through_wall(self):
		
		"""生成穿墙道具"""
		for num in range(self.through_wall_num):
			while True:
				# 生成两个随机数，分别代表道具的行和列，
				column_num = random.randint(0, self.column-1)
				row_num = random.randint(0, self.row-1)

				# 检查所生成的位置是否已被其他道具占有
				# 若是，则更换位置
				# 直到与其他道具位置不冲突位置
				if (column_num, row_num) not in self.bonus_locations:
					self.bonus_locations.append((column_num, row_num))
					location = ((column_num + 1.0)*self.unit_x, (row_num + 2.0)*self.unit_y)
					through_wall = PropThroughWall(self.through_wall_size, location)
					self.bonus.add(through_wall)
					break
					

	def _generate_turtle(self):
		
		"""生成乌龟道具"""
		for num in range(self.turtle_num):
			while True:
				# 生成两个随机数，分别代表道具的行和列，
				column_num = random.randint(0, self.column-1)
				row_num = random.randint(0, self.row-1)

				# 检查所生成的位置是否已被其他道具占有
				# 若是，则更换位置
				# 直到与其他道具位置不冲突位置
				if (column_num, row_num) not in self.bonus_locations:
					self.bonus_locations.append((column_num, row_num))
					location = ((column_num + 1.0)*self.unit_x, (row_num + 2.0)*self.unit_y)
					turtle = PropTurtle(self.turtle_size, location)
					self.bonus.add(turtle)
					break