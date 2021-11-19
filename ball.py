import pygame
import asyncio
import time

from pygame.sprite import Sprite

class Ball(Sprite):

	"""管理小球的类"""

	def __init__(self, game):

		"""初始化小球"""
		super().__init__()
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

		self.bricks = game.bricks_manager.bricks
		self.board = game.board
		self.bonus = game.bonus_manager.bonus

		# 小球属性
		self.is_lock = False
		self.is_through_wall = False
		self.is_turtle = False


	def reset_pos(self):

		"""将小球的位置回归到板子上"""
		self.rect.midbottom = self.game.board.rect.center
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)
		self.speed_x = self.game.settings.ball_speed_x
		self.speed_y = self.game.settings.ball_speed_y


	def move(self):

		"""小球运动"""

		# 如果小球中了锁的道具效果，则粘在板子上不动
		if self.is_lock:
			self._stick_to_board()

		else:
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
			self.speed_x *= -1.0

		elif self.rect.top <= 0:
			self.speed_y *= -1.0


	def check_beat_brick(self):
		
		"""
		检查是否打到砖块
		若是，则删除该砖块
		并改变运动位置
		"""
		collided_brick = pygame.sprite.spritecollideany(self, self.bricks)
		if collided_brick:

			# 根据碰撞时小球与砖块的位置关系，改变小球的运动方向
			if collided_brick.rect.left < self.rect.centerx < collided_brick.rect.right:
				self.speed_y *= -1.0

			elif collided_brick.rect.top < self.rect.centery < collided_brick.rect.bottom:
				self.speed_x *= -1.0

			# 删除该砖块
			collided_brick.kill()


	def check_hit_board(self):
		
		"""
		检查是否碰到板子
		若是,则改变方向
		"""
		if self.rect.bottom > self.board.rect.centery and self.rect.right > self.board.rect.left and self.rect.left < self.board.rect.right:
			self.speed_y *= -1.0


	def check_hit_bonus(self):

		"""
		检查是否碰到道具
		若是，则赋予小球相应的属性
		"""
		collided_bonus = pygame.sprite.spritecollideany(self, self.bonus)
		if collided_bonus:
			if collided_bonus.get_name() == 'heart':
				self.game.settings.ball_number += 1

			elif collided_bonus.get_name() == 'lengthen':
				self.board.is_lengthen = True

			elif collided_bonus.get_name() == 'lock':
				self.is_lock = True

			elif collided_bonus.get_name() == 'through_wall':
				self.is_through_wall = True

			elif collided_bonus.get_name() == 'turtle':
				self.is_turtle = True

			collided_bonus.kill()


	async def check_effect(self):

		"""检查球的道具效果"""

		# 吃到锁头道具，就黏在板子上动不了
		if self.is_lock == True:
			task_free = asyncio.create_task(self._free_ball_after(3))
			await task_free


	def _stick_to_board(self):

		"""小球附着在板子上"""
		self.rect.midbottom = self.game.board.rect.center
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)
		self.speed_x *= -1
		self.speed_y = self.game.settings.ball_speed_y


	async def _free_ball_after(self, delay):

		"""经过delay秒后，小球释放"""
		await asyncio.sleep(delay)
		self.is_lock = False



	def blitme(self):

		"""将小球绘制在板子上"""
		self.screen.blit(self.surface, self.rect)
	
	