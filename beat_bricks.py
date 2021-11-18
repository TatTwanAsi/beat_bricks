import pygame
from pygame.sprite import Sprite
import random

from settings import Settings
from board import Board
from brick import Brick
from bonus import PropHeart, PropLengthen, PropLock, PropThroughWall, PropTurtle


class BeatBricks:

	"""管理《打砖块》的游戏资源以及行为"""
	def __init__(self):

		"""加载游戏参数设置和游戏资源"""
		pygame.init()

		# 管理游戏设置的实例
		self.settings = Settings()

		# 游戏屏幕的surface和rect
		self.screen = pygame.display.set_mode(self.settings.screen_size)
		self.screen_rect = self.screen.get_rect()

		# 游戏中的板子
		self.board = Board(self.settings.board_width, self.settings.board_height, self.settings.board_color, self.screen_rect.midbottom)

		# 游戏中的砖块墙
		self.bricks = pygame.sprite.Group()

		# 游戏中的道具
		self.bonus = pygame.sprite.Group()

		# 创建墙
		self._create_wall()



	def _create_wall(self):

		"""创建游戏的一堵墙"""
		# 先用砖块将墙铺满
		self._fill_with_bricks()

		# 再用一些道具去替换到墙内的一些砖块
		self._replace_some_bricks_with_bonus()
		

	def _fill_with_bricks(self):

		"""用砖块将墙铺满"""
		row = self.settings.row
		column = self.settings.column

		increment_y = (float(self.settings.screen_height)/2)/(float(row)+1)
		increment_x = float(self.settings.screen_width)/(float(column)+1)

		brick_width = self.settings.brick_width
		brick_height = self.settings.brick_height
		brick_color = self.settings.brick_color

		for row_num in range(row):
			for column_num in range(column):
				location = ((column_num + 1.0)*increment_x, (row_num + 1.0)*increment_y)
				brick = Brick(brick_width, brick_height, brick_color, location)
				self.bricks.add(brick)


	def _replace_some_bricks_with_bonus(self):

		"""用一些道具将墙中的一些砖块替换掉"""
		# 生成道具
		self._generate_bonus()

		# 替换砖块
		self._replace_bricks()


	def _generate_bonus(self):

		"""生成道具，并指定其位置"""
		row = self.settings.row
		column = self.settings.column

		increment_y = (float(self.settings.screen_height)/2)/(float(row)+1)
		increment_x = float(self.settings.screen_width)/(float(column)+1)

		check_location = []

		# 心
		for num in range(self.settings.heart_num):
			while True:

				column_num = random.randint(0, column-1)
				row_num = random.randint(0, row-1)

				if (column_num, row_num) not in check_location:
					check_location.append((column_num, row_num))
					location = ((column_num + 1.0)*increment_x, (row_num + 1.0)*increment_y)
					heart = PropHeart(self.settings.heart_size, location)
					self.bonus.add(heart)
					break

		# 增长道具 
		for num in range(self.settings.lengthen_num):
			while True:

				column_num = random.randint(0, column-1)
				row_num = random.randint(0, row-1)
				
				if (column_num, row_num) not in check_location:
					check_location.append((column_num, row_num))
					location = ((column_num + 1.0)*increment_x, (row_num + 1.0)*increment_y)
					lengthen = PropLengthen(self.settings.lengthen_size, location)
					self.bonus.add(lengthen)
					break

		# 锁
		for num in range(self.settings.lock_num):
			while True:

				column_num = random.randint(0, column-1)
				row_num = random.randint(0, row-1)
				
				if (column_num, row_num) not in check_location:
					check_location.append((column_num, row_num))
					location = ((column_num + 1.0)*increment_x, (row_num + 1.0)*increment_y)
					lock = PropLock(self.settings.lock_size, location)
					self.bonus.add(lock)
					break

		# 乌龟
		for num in range(self.settings.turtle_num):
			while True:

				column_num = random.randint(0, column-1)
				row_num = random.randint(0, row-1)
				
				if (column_num, row_num) not in check_location:
					check_location.append((column_num, row_num))
					location = ((column_num + 1.0)*increment_x, (row_num + 1.0)*increment_y)
					turtle = PropTurtle(self.settings.turtle_size, location)
					self.bonus.add(turtle)
					break

		# 穿墙
		for num in range(self.settings.through_wall_num):
			while True:

				column_num = random.randint(0, column-1)
				row_num = random.randint(0, row-1)
				
				if (column_num, row_num) not in check_location:
					check_location.append((column_num, row_num))
					location = ((column_num + 1.0)*increment_x, (row_num + 1.0)*increment_y)
					through_wall = PropThroughWall(self.settings.through_wall_size, location)
					self.bonus.add(through_wall)
					break


	def _replace_bricks(self):

		"""检测道具编组和砖块编组的位置，若有重叠，则将重叠位置的砖块变更为道具"""
		pygame.sprite.groupcollide(self.bricks, self.bonus, True, False)


	def run_game(self):

		"""游戏的主循环，事件监测以及更新画面"""
		while True:
			# 游戏主循环
			self._check_event()
			self._move_board()
			self._update_screen()
			

	def _check_event(self):

		"""检测事件"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()


	def _move_board(self):

		"""让板子跟随鼠标移动，并且不让板子越界"""
		mouse_pos_x = pygame.mouse.get_pos()[0]
		left_border_x = 0
		right_border_x = self.settings.screen_width
		board_width = self.settings.board_width

		if mouse_pos_x - board_width/2 >= left_border_x and mouse_pos_x + board_width/2 <= right_border_x:
			self.board.rect.centerx = mouse_pos_x


	def _update_screen(self):

		"""屏幕的更新"""
		# 绘制背景，应用指定的背景颜色
		self.screen.fill(self.settings.bg_color)

		# 将板子绘制到背景上
		pygame.draw.rect(self.screen, self.board.color, self.board.rect)

		# 隐藏鼠标
		self._hide_mouse()

		# 绘制所有砖块
		self.bricks.draw(self.screen)

		# 绘制所有道具
		self.bonus.draw(self.screen)

		# 将绘制的画面显示出来
		pygame.display.flip()


	def _hide_mouse(self):

		"""当鼠标在游戏屏幕内时，将其隐藏"""
		mouse_x, mouse_y = pygame.mouse.get_pos()
		if mouse_x < self.settings.screen_width and mouse_x > 0 and mouse_y < self.settings.screen_height and mouse_y > 0:
		   pygame.mouse.set_visible(False)

		else:
			pygame.mouse.set_visible(True)



if __name__ == "__main__":

	bb = BeatBricks()
	bb.run_game()

