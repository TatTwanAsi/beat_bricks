import pygame
import asyncio
import time
from pygame.sprite import Sprite

from settings import Settings
from board import Board
from ball import Ball
from bonus_manager import BonusManager
from bricks_manager import BricksManager
from UI_manager import UIManager
from level_loader import get_setting_attr_dict

class BeatBricks:

	"""管理《打砖块》的游戏资源以及行为"""
	def __init__(self, level):

		"""加载游戏参数设置和游戏资源"""
		pygame.init()
		self.settings = Settings(**get_setting_attr_dict(level))										# 管理游戏设置的实例
		self.screen = pygame.display.set_mode(self.settings.screen_size)# 游戏屏幕的surface
		self.screen_rect = self.screen.get_rect()						# 游戏屏幕的rect
		self.score = 0 													# 游戏得分 
		self.UI_manager = UIManager(self)								# 创建管理UI的实例
		self.bonus_manager = BonusManager(self)							# 管理道具的实例
		self.bricks_manager = BricksManager(self)						# 管理砖块的实例
		self.board = Board(self)										# 游戏中的板子
		self.ball = Ball(self)											# 游戏中的小球
		self._create_wall()												# 创建墙
		self.is_pause = False											# 游戏是否暂停
		pygame.display.set_caption("Beat Bricks")						# 设置标题


	def _create_wall(self):

		"""创建游戏的一堵墙"""
		# 砖块管理实例在初始化时，用砖块填满了游戏的墙
		# 道具管理实例在初始化时，在墙上生成了一系列道具
		# 用已有的道具去替换掉墙上的一些砖块
		pygame.sprite.groupcollide(self.bricks_manager.bricks, self.bonus_manager.bonus, True, False)


	async def run_game(self):

		"""运行游戏，执行两个协程"""
		# 主循环协程
		task_main_loop = asyncio.create_task(self._main_loop())
		# 检测道具属性的协程
		task_check_effect_loop = asyncio.create_task(self._check_effect_loop())
		await task_main_loop
		await task_check_effect_loop
		await task_get_mouse_speed_x
			

	async def _main_loop(self):

		"""游戏的主循环，事件监测以及更新画面"""
		while True:
			# 游戏主循环
			self._check_input_event()		# 检测输入事件
			self.board.move()				# 板子的运动
			self._update_ball()				# 更新小球的运动
			self.UI_manager.update()		# 更新UI
			self._check_win()				# 检测胜利
			self._check_die()				# 检测死亡
			self._update_screen()			# 更新屏幕
			await asyncio.sleep(0.00000000000000001)


	def _check_input_event(self):

		"""检测输入事件"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					quit()
				elif event.key == pygame.K_ESCAPE:
					self.is_pause = True
				elif event.key == pygame.K_r:
					self.is_pause = False


	def _update_ball(self):

		"""检查小球的状态，管理小球的运动"""
		self.ball.move() #小球运动

		# 若小球越过底部边界，则游戏暂停0.5秒，然后将小球归位
		if self.ball.rect.top > self.screen_rect.bottom:
			self.settings.ball_number -= 1
			self.score -= 1
			time.sleep(0.5)
			self.ball.reset_pos()

		# 检测小球是否打到砖块
		self.ball.check_beat_brick()

		# 检测小球是否打到板子
		self.ball.check_hit_board()

		# 检测小球是否打到道具
		self.ball.check_hit_bonus()


	def _check_win(self):

		"""检查是否胜利"""
		# 若砖块全部被打掉，则游戏胜利
		if len(self.bricks_manager.bricks) == 0:
			self.bricks_manager.bricks.draw(self.screen)
			self.UI_manager.show_win_UI()
			time.sleep(2)
			quit()


	def _check_die(self):

		"""检查是否死亡"""
		# 若小球剩余数量为0，则判定为死亡，游戏结束
		if self.settings.ball_number <= 0:
			self.UI_manager.show_die_UI()
			time.sleep(2)
			quit()


	def _update_screen(self):

		"""屏幕的更新"""
		self.screen.fill(self.settings.bg_color) 	# 绘制背景，应用指定的背景颜色
		self.board.blitme()  						# 将板子绘制到背景上
		self.bricks_manager.bricks.draw(self.screen)# 绘制所有砖块
		self.bonus_manager.bonus.draw(self.screen) 	# 绘制所有道具
		self.ball.blitme() 							# 将小球绘制
		self.UI_manager.show_me()
		pygame.display.flip() 						# 将绘制的画面显示出来


	async def _check_effect_loop(self):

		"""检查游戏中各个元素是否被赋予了道具效果"""
		while True:
			task_check_board_effect = asyncio.create_task(self.board.check_effect())
			task_check_ball_effect = asyncio.create_task(self.ball.check_effect())
			await task_check_board_effect
			await task_check_ball_effect
			await asyncio.sleep(0.00000000000000001)


if __name__ == "__main__":

	bb = BeatBricks(3)
	asyncio.run(bb.run_game())