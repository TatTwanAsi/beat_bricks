import pygame


class Menu:

	"""管理菜单"""
	def __init__(self):

		"""初始化"""
		pygame.init()
		self.screen = pygame.display.set_mode((1200, 800))# 游戏屏幕的surface
		self.screen.fill((48, 56, 65))
		self.screen_rect = self.screen.get_rect()
		pygame.display.set_caption("Beat Bricks")
		self._initialize_button()	


	def _initialize_button(self):

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


	def run_menu(self, level_getter):

		"""主循环"""
		while True:

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					level_getter.level = None
					quit()
				elif event.type == pygame.MOUSEBUTTONUP:
					level_getter.level = self._check_level()
					quit()

			self._update_screen()
			

	def _check_level(self):

		"""检查点击的是哪个按钮"""
		if self.level_1_rect.left < pygame.mouse.get_pos()[0] < self.level_1_rect.right and self.level_1_rect.top < pygame.mouse.get_pos()[1] < self.level_1_rect.bottom:
			level = 1
		elif self.level_2_rect.left < pygame.mouse.get_pos()[0] < self.level_2_rect.right and self.level_2_rect.top < pygame.mouse.get_pos()[1] < self.level_2_rect.bottom:
			level = 2
		elif self.level_3_rect.left < pygame.mouse.get_pos()[0] < self.level_3_rect.right and self.level_3_rect.top < pygame.mouse.get_pos()[1] < self.level_3_rect.bottom:
			level = 3
		return level

	def _update_screen(self):

		"""更新屏幕"""
		self.screen.blit(self.level_1, self.level_1_rect)
		self.screen.blit(self.level_2, self.level_2_rect)
		self.screen.blit(self.level_3, self.level_3_rect)
		self.screen.blit(self.level_1_text, self.level_1_text_rect)
		self.screen.blit(self.level_2_text, self.level_2_text_rect)
		self.screen.blit(self.level_3_text, self.level_3_text_rect)
		
		pygame.display.flip()