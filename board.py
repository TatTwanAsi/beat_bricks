import pygame

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


	def move(self):

		"""让板子跟随鼠标移动，并且不让板子越界"""
		mouse_pos_x = pygame.mouse.get_pos()[0]
		left_border_x = 0
		right_border_x = self.settings.screen_width
		board_width = self.settings.board_width

		if mouse_pos_x - board_width/2 >= left_border_x and mouse_pos_x + board_width/2 <= right_border_x:
			self.rect.centerx = mouse_pos_x


	def blitme(self):

		"""将板子绘制到屏幕上"""
		self.screen.blit(self.surface, self.rect)