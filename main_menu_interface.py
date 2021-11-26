import pygame
from pygame.font import Font
import sys
import asyncio

class MainMenuInterface:

	"""管理主菜单界面的类"""
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((1200, 800))
		self.screen.fill((48, 56, 65))
		self.screen_rect = self.screen.get_rect()
		self._initialize_UI()


	def _initialize_UI(self):

		"""初始化主菜单的UI"""
		caption_font = pygame.font.SysFont('Comic Sans MS', 160)
		font = pygame.font.SysFont('Comic Sans MS', 30)

		self.caption = caption_font.render('Beat Bricks', True, (250, 250, 250))
		self.caption_rect = self.caption.get_rect()
		self.caption_rect.center = self.screen_rect.center
		self.caption_rect.centery -= 200

		self.start_game_button = pygame.Surface((200, 100))
		self.start_game_button.fill((79, 86, 94))
		self.start_game_button_rect = self.start_game_button.get_rect()
		self.start_game_button_rect.center = (600, 400)
		self.start_game_text = font.render('Start', True, (250, 250, 250))
		self.start_game_text_rect = self.start_game_text.get_rect()
		self.start_game_text_rect.center = self.start_game_button_rect.center

		self.quit_game_button = pygame.Surface((200, 100))
		self.quit_game_button.fill((79, 86, 94))
		self.quit_game_button_rect = self.quit_game_button.get_rect()
		self.quit_game_button_rect.center = (600, 600)
		self.quit_game_text = font.render('Quit', True, (250, 250, 250))
		self.quit_game_text_rect = self.quit_game_text.get_rect()
		self.quit_game_text_rect.center = self.quit_game_button_rect.center


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
				button_name = self._check_main_menu_button()
				return button_name


	def _check_main_menu_button(self):

		"""检查用户点击了主菜单的哪个按钮"""
		if self.start_game_button_rect.left < pygame.mouse.get_pos()[0] < self.start_game_button_rect.right and self.start_game_button_rect.top < pygame.mouse.get_pos()[1] < self.start_game_button_rect.bottom:
			return 'level_select'
		elif self.quit_game_button_rect.left < pygame.mouse.get_pos()[0] < self.quit_game_button_rect.right and self.quit_game_button_rect.top < pygame.mouse.get_pos()[1] < self.quit_game_button_rect.bottom:
			sys.exit()
		return None


	def _draw(self):

		"""更新屏幕"""
		self.screen.blit(self.caption, self.caption_rect)
		self.screen.blit(self.start_game_button, self.start_game_button_rect)
		self.screen.blit(self.quit_game_button, self.quit_game_button_rect)
		self.screen.blit(self.start_game_text, self.start_game_text_rect)
		self.screen.blit(self.quit_game_text, self.quit_game_text_rect)
		pygame.display.flip()