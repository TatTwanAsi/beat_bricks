import pygame
from pygame.font import Font

from UI_element import UIElement


class UIManager:

	"""管理UI元素的类"""

	def __init__(self, game):

		"""初始化"""

		# 加载图片
		self.screen = game.screen
		self.screen_rect = game.screen_rect
		self.settings = game.settings
		# 获取各个UI元素的图片surface，并指定其位置
		self.ball_image = pygame.image.load("images/ball.png")
		self.ball_image = pygame.transform.scale(self.ball_image, (self.settings.ball_width, self.settings.ball_height))
		self.heart_image = pygame.image.load("images/heart.png")
		self.heart_image = pygame.transform.scale(self.heart_image, self.settings.heart_size)
		self.lengthen_image = pygame.image.load("images/lengthen.png")
		self.lengthen_image = pygame.transform.scale(self.lengthen_image, self.settings.lengthen_size)
		self.lock_image = pygame.image.load("images/lock.png")
		self.lock_image = pygame.transform.scale(self.lock_image, self.settings.lock_size)
		self.through_wall_image = pygame.image.load("images/turtle.png")
		self.through_wall_image = pygame.transform.scale(self.through_wall_image, self.settings.through_wall_size)

		# 创建字体
		pygame.init()
		self.myfont = pygame.font.SysFont('Comic Sans MS', 20)

		# 初始化各个板块的UI
		self._initialize_ball_num_UI()
		self._initialize_effect_UI()
		self._initialize_score_UI()


	def _initialize_ball_num_UI(self):

		"""创建显示小球剩余数目的UI"""
		self.ball_number = self.settings.ball_number											# 获取小球数目
		ball_num_surface = self.myfont.render("balls left: ", True, (246, 252, 249))	# 创建文字UI的surface
		ball_num_rect = ball_num_surface.get_rect()								# 获取文字UI的rect
		ball_num_rect.top = 10													# 指定文字UI的y
		ball_num_rect.left = 10													# 指定文字UI的x
		self.ball_num_UI = UIElement(ball_num_surface, ball_num_rect)

		# 创建小球图片UI的编组
		self.ball_UI_group = pygame.sprite.Group()

		# 创建图片UI并压入编组		
		for num in range(self.ball_number):

			# 给每个小球UI指定位置
			ball_image = self.ball_image.copy()
			ball_image_rect = ball_image.get_rect()
			ball_image_rect.left = 110 + num * 40
			ball_image_rect.top = 5
			ball_UI = UIElement(ball_image, ball_image_rect)
			self.ball_UI_group.add(ball_UI)


	def _initialize_effect_UI(self):

		"""初始化效果的UI"""
		pass


	def _initialize_score_UI(self):

		"""初始化分数UI"""
		pass


	def update(self):

		"""更新UI"""
		# while True:
		self._update_ball_left()		# 更新剩余小球数
		self._update_effect()			# 更新表示道具效果的图标，以及效果还要持续多久才结束
		self._update_score()			# 更新游戏的得分


	def show_me(self):

		"""显示UI"""
		self._show_ball_left()			# 显示小球剩余数
		self._show_effect()				# 显示效果
		self._show_score()				# 显示游戏得分


	def _update_ball_left(self):

		"""更新小球剩余个数，并显示"""
		ball_num_change = self.settings.ball_number - self.ball_number	# 小球数变化

		if ball_num_change == -1:

			# 小球减少
			self.ball_UI_group.sprites()[-1].kill()

		elif ball_num_change == 1:

			# 小球增加
			ball_image = self.ball_image.copy()
			ball_image_rect = ball_image.get_rect()
			ball_image_rect.left = 110 + len(self.ball_UI_group) * 40
			ball_image_rect.top = 5
			ball_UI = UIElement(ball_image, ball_image_rect)
			self.ball_UI_group.add(ball_UI)

		self.ball_number = self.settings.ball_number


	def _show_ball_left(self):

		"""显示小球剩余个数"""
		self.ball_UI_group.draw(self.screen)
		self.screen.blit(self.ball_num_UI.image, self.ball_num_UI.rect)


	def _update_effect(self):

		"""更新道具效果UI"""
		pass


	def _show_effect(self):

		"""显示道具效果UI"""
		pass


	def _update_score(self):

		"""更新分数UI"""
		pass


	def _show_score(self):

		"""显示分数UI"""
		pass