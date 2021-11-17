import pygame

class BeatBricks:

	"""管理《打砖块》的游戏资源以及行为"""
	def __init__(self):

		"""初始化游戏参数设置，加载游戏资源"""
		pygame.init()

		self.screen = pygame.display.set_mode((1200, 800))
		self.bg_color = (31, 31, 31)


	def run_game(self):

		"""游戏的主循环，事件监测以及更新画面"""
		while True:
			# 游戏主循环

			for event in pygame.event.get():
				# 事件检测
				if event.type == pygame.QUIT:
					quit()


			# 绘制背景，应用指定的背景颜色
			self.screen.fill(self.bg_color)

			# 将绘制的画面显示出来
			pygame.display.flip()


if __name__ == "__main__":

	bb = BeatBricks()
	bb.run_game()

