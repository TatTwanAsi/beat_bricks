class Settings:

	"""将游戏的参数设置都放在一个模块中"""
	def __init__(self):

		# 游戏屏幕
		self.bg_color = (30, 30, 30)
		self.screen_size = (1200, 800)
		self.screen_width, self.screen_height = self.screen_size

		# 板子
		self.board_width = 100
		self.board_height = 20
		self.board_color = (74, 138, 244)

		# 砖块
		self.brick_width = 70
		self.brick_height = 30
		self.brick_color = (25, 161, 94)

		# 砖块墙
		self.row = 11
		self.column = 15