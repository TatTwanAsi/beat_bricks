import pygame

from settings import Settings
from board import Board

class BeatBricks:

	"""管理《打砖块》的游戏资源以及行为"""
	def __init__(self):

		"""加载游戏参数设置和游戏资源"""
		pygame.init()

		# 管理游戏设置的实例
		self.settings = Settings()

		# 游戏屏幕的surface
		self.screen = pygame.display.set_mode(self.settings.screen_size)

		# 游戏中的板子
		self.board = Board(self.settings.board_width, self.settings.board_height, self.settings.board_color, self.screen.get_rect().midbottom)


	def run_game(self):

		"""游戏的主循环，事件监测以及更新画面"""
		while True:
			# 游戏主循环
			self._check_event()
			self._move_board()
			self._update_screen()
			


	def _check_event(self):

		"""检测事件"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()


	def _move_board(self):

		"""让板子跟随鼠标移动，并且不让板子越界"""
		mouse_pos_x = pygame.mouse.get_pos()[0]
		left_border_x = 0
		right_border_x = self.settings.screen_width
		board_width = self.settings.board_width

		if mouse_pos_x - board_width/2 >= left_border_x and mouse_pos_x + board_width/2 <= right_border_x:
			self.board.rect.centerx = mouse_pos_x


	def _update_screen(self):

		"""屏幕的更新"""
		# 绘制背景，应用指定的背景颜色
		self.screen.fill(self.settings.bg_color)

		# 将板子绘制到背景上
		pygame.draw.rect(self.screen, self.board.color, self.board.rect)

		self._hide_mouse()

		# 将绘制的画面显示出来
		pygame.display.flip()


	def _hide_mouse(self):

		"""当鼠标在游戏屏幕内时，将其隐藏"""
		mouse_x, mouse_y = pygame.mouse.get_pos()
		if mouse_x < self.settings.screen_width and mouse_x > 0 and mouse_y < self.settings.screen_height and mouse_y > 0:
		   pygame.mouse.set_visible(False)

		else:
			pygame.mouse.set_visible(True)



if __name__ == "__main__":

	bb = BeatBricks()
	bb.run_game()

