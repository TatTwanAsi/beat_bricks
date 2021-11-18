import pygame

class Ball:

	"""管理小球的类"""

	def __init__(self, game):

		"""初始化小球"""
		self.game = game
		self.screen = game.screen
		self.screen_rect = game.screen_rect
		self.width = game.settings.ball_width
		self.height = game.settings.ball_height

		self.surface = pygame.image.load("images/ball.png")
		self.surface = pygame.transform.scale(self.surface, (self.width, self.height))
		self.rect = self.surface.get_rect()

		self.x = self.rect.x
		self.y = self.rect.y

	def stick_to_board(self):

		"""小球附着在板子上"""
		self.rect.midbottom = self.game.board.rect.center


	def blitme(self):

		"""将小球绘制在板子上"""
		self.screen.blit(self.surface, self.rect)
	
	