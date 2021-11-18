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

		self.rect.midbottom = self.game.board.rect.center

		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

		self.speed_x = game.settings.ball_speed_x
		self.speed_y = game.settings.ball_speed_y


	def reset_pos(self):

		"""将小球的位置回归到板子上"""
		self.rect.midbottom = self.game.board.rect.center
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)
		self.speed_y *= -1


	def move(self):

		"""小球运动"""
		self._check_hit_border()
		self.x += self.speed_x
		self.y -= self.speed_y
		self.rect.x = self.x
		self.rect.y = self.y
		

	def _check_hit_border(self):

		"""
		监测小球是否碰壁
		若是，则改变运动方向
		"""
		if self.rect.left <= 0 or self.rect.right >= self.screen_rect.right:
			self.speed_x *= -1

		elif self.rect.top <= 0:
			self.speed_y *= -1


	def stick_to_board(self):

		"""小球附着在板子上"""
		self.rect.midbottom = self.game.board.rect.center


	def blitme(self):

		"""将小球绘制在板子上"""
		self.screen.blit(self.surface, self.rect)
	
	