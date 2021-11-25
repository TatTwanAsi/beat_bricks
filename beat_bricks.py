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
import sys

class BeatBricks:

	"""管理《打砖块》的游戏资源以及行为"""
	def __init__(self):

		"""加载游戏参数设置和游戏资源"""
		pygame.init()
		self.level = self._run_main_menu()	# 运行菜单
		if level:
			self._initialize_game()
			
		else:
			sys.exit()


	def _run_main_menu(self):

		"""运行主菜单"""
		self.screen = pygame.display.set_mode((1200, 800))
		self.screen.fill((48, 56, 65))
		self.screen_rect = self.screen.get_rect()
		self._initialize_main_menu_UI()

		# 主循环
		while True:

			# 事件监测
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == pygame.MOUSEBUTTONUP:
					self._check_main_menu_button()

			# 更新屏幕
			self.screen.blit(self.caption, self.caption_rect)
			self.screen.blit(self.start_game_button, self.start_game_button_rect)
			self.screen.blit(self.history_score, self.history_score_rect)
			self.screen.blit(self.quit_game_button, self.quit_game_button_rect)
			self.screen.blit(self.start_game_text, self.start_game_text_rect)
			self.screen.blit(self.history_score_text, self.history_score_text_rect)
			self.screen.blit(self.quit_game_text, self.quit_game_text_rect)
			pygame.display.flip()


	def _check_main_menu_button(self):

		"""检查用户点击了主菜单的哪个按钮"""
		if self.caption_rect.left < pygame.mouse.get_pos()[0] < self.caption_rect.right and self.caption_rect.top < pygame.mouse.get_pos()[1] < self.caption_rect.bottom:
			self._run_select_level_menu()


	def _initialize_main_menu_UI(self):

		"""初始化主菜单的UI"""
		caption_font = pygame.font.SysFont('Comic Sans MS', 200)
		font = font = pygame.font.SysFont('Comic Sans MS', 30)

		self.caption = font.render('Beat Bricks', True, (250, 250, 250))
		self.caption_rect = self.caption.get_rect()
		self.caption_rect.center = self.screen_rect.center
		self.caption_rect.centery - 200

		self.start_game_button = pygame.Surface((200, 100))
		self.start_game_button.fill((79, 86, 94))
		self.start_game_button_rect = self.start_game_button.get_rect()
		self.start_game_button_rect.center = (600, 500)
		self.start_game_text = font.render('Start', True, (250, 250, 250))
		self.start_game_text_rect = self.start_game_button_text.get_rect()
		self.start_game_text_rect.center = self.start_game_button_rect.center

		self.history_score_button = pygame.Surface((200, 200))
		self.history_score_button.fill((79, 86, 94))
		self.history_score_button_rect = self.start_game_button.get_rect()
		self.history_score_button_rect.center = (600, 600)
		self.history_score_text = font.render('History', True, (250, 250, 250))
		self.history_score_text_rect = self.start_game_button_text.get_rect()
		self.history_score_text_rect.center = self.start_game_button_rect.center


		self.quit_game_button = pygame.Surface((200, 200))
		self.quit_game_button.fill((79, 86, 94))
		self.quit_game_button_rect = self.start_game_button.get_rect()
		self.quit_game_rect.center = (600, 700)
		self.quit_game_text = font.render('Quit', True, (250, 250, 250))
		self.quit_game_text_rect = self.start_game_button_text.get_rect()
		self.quit_game_text_rect.center = self.start_game_button_rect.center


	def _run_select_level_menu(self):

		"""运行关卡选择界面"""
		self.screen = pygame.display.set_mode((1200, 800))# 游戏屏幕的surface
		self.screen.fill((48, 56, 65))
		self.screen_rect = self.screen.get_rect()
		self._initialize_level_button()

		# 主循环
		while True:

			# 事件监测
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

				elif event.type == pygame.MOUSEBUTTONUP:
					level = self._check_level()
					if level:
						return level

			# 更新屏幕
			self.screen.blit(self.level_1, self.level_1_rect)
			self.screen.blit(self.level_2, self.level_2_rect)
			self.screen.blit(self.level_3, self.level_3_rect)
			self.screen.blit(self.level_1_text, self.level_1_text_rect)
			self.screen.blit(self.level_2_text, self.level_2_text_rect)
			self.screen.blit(self.level_3_text, self.level_3_text_rect)
			
			pygame.display.flip()


	def _initialize_level_button(self):

		"""初始化按钮"""
		font = pygame.font.SysFont('Comic Sans MS', 40)
		self.level_1 = pygame.Surface((200, 200))
		self.level_1.fill((79, 86, 94))
		self.level_1_rect = self.level_1.get_rect()
		self.level_1_rect.center = (300, 300)
		self.level_1_text = font.render('level 1', True, (250, 250, 250))
		self.level_1_text_rect = self.level_1_text.get_rect()
		self.level_1_text_rect.center = self.level_1_rect.center

		self.level_2 = pygame.Surface((200, 200))
		self.level_2.fill((79, 86, 94))
		self.level_2_rect = self.level_2.get_rect()
		self.level_2_rect.center = (600, 300)
		self.level_2_text = font.render('level 2', True, (250, 250, 250))
		self.level_2_text_rect = self.level_2_text.get_rect()
		self.level_2_text_rect.center = self.level_2_rect.center

		self.level_3 = pygame.Surface((200, 200))
		self.level_3.fill((79, 86, 94))
		self.level_3_rect = self.level_3.get_rect()
		self.level_3_rect.center = (900, 300)
		self.level_3_text = font.render('level 3', True, (250, 250, 250))
		self.level_3_text_rect = self.level_3_text.get_rect()
		self.level_3_text_rect.center = self.level_3_rect.center


	def _initialize_game(self):

		"""初始化游戏"""
		self.settings = Settings(**get_setting_attr_dict(self.level))	# 管理游戏设置的实例
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


	def _check_level(self):

		"""检查点击的是哪个按钮"""
		level = None
		if self.level_1_rect.left < pygame.mouse.get_pos()[0] < self.level_1_rect.right and self.level_1_rect.top < pygame.mouse.get_pos()[1] < self.level_1_rect.bottom:
			level = 1
		elif self.level_2_rect.left < pygame.mouse.get_pos()[0] < self.level_2_rect.right and self.level_2_rect.top < pygame.mouse.get_pos()[1] < self.level_2_rect.bottom:
			level = 2
		elif self.level_3_rect.left < pygame.mouse.get_pos()[0] < self.level_3_rect.right and self.level_3_rect.top < pygame.mouse.get_pos()[1] < self.level_3_rect.bottom:
			level = 3
		return level


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
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					sys.exit()
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
			sys.exit()

	def _check_die(self):

		"""检查是否死亡"""
		# 若小球剩余数量为0，则判定为死亡，游戏结束
		if self.settings.ball_number <= 0:
			self.UI_manager.show_die_UI()
			time.sleep(2)
			sys.exit()


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

	bb = BeatBricks()
	asyncio.run(bb.run_game())