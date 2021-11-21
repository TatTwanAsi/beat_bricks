import pygame
from pygame.font import Font

from UI_element import UIElement


class UIManager:

	"""管理UI元素的类"""

	def __init__(self, game):

		"""初始化"""

		self.game = game
		self.screen = game.screen
		self.screen_rect = game.screen_rect
		self.settings = game.settings
		self.UI_text_color = game.settings.UI_text_color

		# 获取各个UI元素的图片surface，并指定其位置
		self.ball_image = pygame.image.load("images/ball.png")
		self.ball_image = pygame.transform.scale(self.ball_image, (self.settings.ball_width, self.settings.ball_height))
		self.lengthen_image = pygame.image.load("images/lengthen.png")
		self.lengthen_image = pygame.transform.scale(self.lengthen_image, (10, 10))
		self.lock_image = pygame.image.load("images/lock.png")
		self.lock_image = pygame.transform.scale(self.lock_image, (self.settings.lock_width/2, self.settings.lock_height/2))
		self.through_wall_image = pygame.image.load("images/through_wall.png")
		self.through_wall_image = pygame.transform.scale(self.through_wall_image, (self.settings.through_wall_width/2, self.settings.through_wall_height/2))
		self.turtle_image = pygame.image.load("images/turtle.png")
		self.turtle_image = pygame.transform.scale(self.turtle_image, (self.settings.turtle_width/2, self.settings.turtle_height/2))

		# 创建字体
		self.my_ball_font = pygame.font.SysFont('Comic Sans MS', 20)	# 剩余球数字体
		self.my_score_font = pygame.font.SysFont('Comic Sans MS', 35)	# 分数字体
		self.my_win_die_font = pygame.font.SysFont('Comic Sans MS', 100)# 显示游戏死亡或成功字体

		# 初始化各个板块的UI
		self._initialize_ball_num_UI()
		self._initialize_effect_UI()
		self._initialize_score_UI()
		self._initialize_win_UI()
		self._initialize_die_UI()


	def _initialize_ball_num_UI(self):

		"""创建显示小球剩余数目的UI"""
		self.ball_number = self.settings.ball_number											# 获取小球数目
		ball_num_surface = self.my_ball_font.render("balls left: ", True, self.UI_text_color)	# 创建文字UI的surface
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
		self.effect_UI_group = pygame.sprite.Group()


	def _initialize_score_UI(self):

		"""初始化分数UI"""
		self.score = self.game.score

		# 分数的描述文字("Score: ")
		score_description_surface = self.my_score_font.render("Score: ", True, self.UI_text_color)
		score_description_rect = score_description_surface.get_rect()
		score_description_rect.top = 10
		score_description_rect.right = self.screen_rect.right - 120
		score_description_UI = UIElement(score_description_surface, score_description_rect)

		# 分数的值
		score_value_surface = self.my_score_font.render(f"{self.score}", True, self.UI_text_color)
		score_value_rect = score_description_surface.get_rect()
		score_value_rect.top = 10
		score_value_rect.left = self.screen_rect.right - 120
		score_value_UI = UIElement(score_value_surface, score_value_rect)

		# 完整分数UI
		self.score_UI = pygame.sprite.Group()
		self.score_UI.add(score_description_UI)
		self.score_UI.add(score_value_UI)


	def _initialize_win_UI(self):

		"""初始化赢的UI"""
		win_UI_surface = self.my_win_die_font.render("YOU WIN", True, self.UI_text_color)
		win_UI_rect= win_UI_surface.get_rect()
		win_UI_rect.center = self.screen_rect.center
		self.win_UI = UIElement(win_UI_surface, win_UI_rect)


	def _initialize_die_UI(self):

		"""初始化死的UI"""
		die_UI_surface = self.my_win_die_font.render("YOU DIE", True, self.UI_text_color)
		die_UI_rect= die_UI_surface.get_rect()
		die_UI_rect.center = self.screen_rect.center
		self.die_UI = UIElement(die_UI_surface, die_UI_rect)


	def update(self):

		"""更新UI"""
		# while True:
		self._update_ball_left()		# 更新剩余小球数
		self._update_score()			# 更新游戏的得分


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


	def update_effect(self, effect_name='', is_push = None):

		"""更新道具效果UI，属于被动更新"""
		if effect_name == 'heart':
			# 吃到新道具，回血，但是效果UI不显示，而是显示到小球剩余数的板块中
			pass

		elif effect_name:
			if is_push == True:
				self._effect_UI_push(effect_name)
	
			elif is_push == False:
				self._effect_UI_pop(effect_name)
			self._set_effect_UI_position()


	def _effect_UI_push(self, effect_name):

		"""增加某个效果的UI"""
		for effect_UI in self.effect_UI_group:

			# 遍历道具效果UI编组
			# 检查其中是否已经有了这个效果
			# 若有的话，就把他从编组中删除
			if effect_UI.name == effect_name:
				effect_UI.kill()
				break

		# 创建某个效果的UI，将其压入效果UI编组中
		effect_UI_surface = pygame.image.load(f"images/{effect_name}.png")
		effect_UI_surface = pygame.transform.scale(effect_UI_surface, (55, 40))
		effect_UI_rect = effect_UI_surface.get_rect()
		effect_UI = UIElement(effect_UI_surface, effect_UI_rect, effect_name)
		self.effect_UI_group.add(effect_UI)


	def _effect_UI_pop(self, effect_name):

		"""删除某个效果的UI"""
		for effect_UI in self.effect_UI_group:

			# 遍历道具效果UI编组
			# 检查其中是否已经有了这个效果
			# 若有的话，就把他从编组中删除
			if effect_UI.name == effect_name:
				effect_UI.kill()
				break


	def _set_effect_UI_position(self):

		"""指定UI的位置"""
		num = 0
		for effect_UI in self.effect_UI_group:

			# 便利道具效果UI的编组
			# 指定每个UI元素的位置
			effect_UI.rect.left = 400 + num * 60
			effect_UI.rect.top = 10
			num += 1

	def _update_score(self):

		"""更新分数UI"""
		if self.score != self.game.score:
			
			self.score = self.game.score
			self.score_UI.sprites()[1].kill()
			score_value_surface = self.my_score_font.render(f"{self.score}", True, self.UI_text_color)
			score_value_rect = score_value_surface.get_rect()
			score_value_rect.top = 10
			score_value_rect.left = self.screen_rect.right - 120
			score_value_UI = UIElement(score_value_surface, score_value_rect)
			self.score_UI.add(score_value_UI)


	def show_me(self):

		"""显示UI"""
		self._show_ball_left()			# 显示小球剩余数
		self._show_effect()				# 显示效果
		self._show_score()				# 显示游戏得分


	def _show_ball_left(self):

		"""显示小球剩余个数"""
		self.ball_UI_group.draw(self.screen)
		self.screen.blit(self.ball_num_UI.image, self.ball_num_UI.rect)


	def _show_effect(self):

		"""显示道具效果UI"""
		self.effect_UI_group.draw(self.screen)
	

	def _show_score(self):

		"""显示分数UI"""
		self.score_UI.draw(self.screen)


	def show_win_UI(self):

		"""展示胜利的UI"""
		self.screen.blit(self.win_UI.image, self.win_UI.rect)
		pygame.display.flip()


	def show_die_UI(self):

		"""展示死亡的UI"""
		self.screen.blit(self.die_UI.image, self.win_UI.rect)
		pygame.display.flip()
