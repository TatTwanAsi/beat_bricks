import pygame
import asyncio
import time

class Board:

	"""管理板子的类"""
	def __init__(self, game):

		"""初始化板子"""
		self.game = game
		self.settings = game.settings
		self.screen = game.screen
		self.screen_rect = game.screen_rect
		self.width = game.settings.board_width
		self.height = game.settings.board_height
		self.color = game.settings.board_color

		self.surface = pygame.Surface((self.width, self.height))
		self.surface.fill(self.color)
		self.rect = self.surface.get_rect()
		self.rect.midbottom = self.screen_rect.midbottom

		# 板子属性
		self.is_lengthen = False


	def move(self):

		"""让板子跟随鼠标移动，并且不让板子越界"""
		mouse_pos_x = pygame.mouse.get_pos()[0]
		left_border_x = 0
		right_border_x = self.settings.screen_width
		board_width = self.settings.board_width

		if mouse_pos_x - board_width/2 >= left_border_x and mouse_pos_x + board_width/2 <= right_border_x:
			self.rect.centerx = mouse_pos_x


	async def check_effect(self):

		"""
		检查板子的道具效果
		若检测到增长属性为真，则增长
		增长3秒后，变回原来的长度
		"""
		# print(1)
		if self.is_lengthen:
			task_lengthen = asyncio.create_task(self._lengthen_board())
			task_shorten = asyncio.create_task(self._turn_width_back_after(self.settings.lengthen_span_time))
			await task_lengthen
			await task_shorten
		await asyncio.sleep(0.0000000001)


	async def _lengthen_board(self):

		"""增长板子"""
		self.is_lengthen = False
		self.surface = pygame.Surface((self.width * 3, self.height))
		self.surface.fill(self.color)
		self.rect = self.surface.get_rect()
		self.rect.bottom = self.screen_rect.bottom
		self.rect.centerx = pygame.mouse.get_pos()[0]


	async def _turn_width_back_after(self, delay):
		
		"""等待delay秒后将板子变回原来的长度"""
		await asyncio.sleep(delay)
		self.surface = pygame.Surface((self.width, self.height))
		self.surface.fill(self.color)
		self.rect = self.surface.get_rect()
		self.rect.bottom = self.screen_rect.bottom
		self.rect.centerx = pygame.mouse.get_pos()[0]
		self.game.UI_manager.update_effect('lengthen', False)
		print('delete_lengthen')


	def blitme(self):

		"""将板子绘制到屏幕上"""
		self.screen.blit(self.surface, self.rect)