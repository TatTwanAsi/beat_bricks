import pygame
from pygame.font import Font
import sys
import asyncio

class LevelSelectInterface:

	"""管理关卡选择界面的类"""
	def __init__(self):

		pygame.init()
		self.screen = pygame.display.set_mode((1200, 800))# 游戏屏幕的surface
		self.screen.fill((48, 56, 65))
		self.screen_rect = self.screen.get_rect()
		self._initialize_UI()

	def _initialize_UI(self):
	
		"""初始化按钮"""
		font = pygame.font.SysFont('Comic Sans MS', 40)

		self.back = pygame.Surface((120, 70))
		self.back.fill((79, 86, 94))
		self.back_rect = self.back.get_rect()
		self.back_rect.topleft = (3, 3)
		self.back_text = font.render('Back', True, (250, 250, 250))
		self.back_text_rect = self.back_text.get_rect()
		self.back_text_rect.center = self.back_rect.center

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


	async def update(self):

		"""更新"""
		while True:
			button = self._check_event()
			self._draw()
			if button:
				return button


	def _check_event(self):

		"""事件监测"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
	
			elif event.type == pygame.MOUSEBUTTONUP:
				button_name = self._check_level()
				return button_name
				


	def _check_level(self):
 
	 	"""检查点击的是哪个按钮"""
	 	level = None
	 	if self.level_1_rect.left < pygame.mouse.get_pos()[0] < self.level_1_rect.right and self.level_1_rect.top < pygame.mouse.get_pos()[1] < self.level_1_rect.bottom:
	 		return 'level_1'
	 	elif self.level_2_rect.left < pygame.mouse.get_pos()[0] < self.level_2_rect.right and self.level_2_rect.top < pygame.mouse.get_pos()[1] < self.level_2_rect.bottom:
	 		return 'level_2'
	 	elif self.level_3_rect.left < pygame.mouse.get_pos()[0] < self.level_3_rect.right and self.level_3_rect.top < pygame.mouse.get_pos()[1] < self.level_3_rect.bottom:
	 		return 'level_3'
	 	elif self.back_rect.left < pygame.mouse.get_pos()[0] < self.back_rect.right and self.back_rect.top < pygame.mouse.get_pos()[1] < self.back_rect.bottom:
	 		return 'main_menu'
	 	return None


	def _draw(self):

		"""更新屏幕"""
		self.screen.blit(self.level_1, self.level_1_rect)
		self.screen.blit(self.level_2, self.level_2_rect)
		self.screen.blit(self.level_3, self.level_3_rect)
		self.screen.blit(self.back, self.back_rect)
		self.screen.blit(self.level_1_text, self.level_1_text_rect)
		self.screen.blit(self.level_2_text, self.level_2_text_rect)
		self.screen.blit(self.level_3_text, self.level_3_text_rect)
		self.screen.blit(self.back_text, self.back_text_rect)
		pygame.display.flip()
