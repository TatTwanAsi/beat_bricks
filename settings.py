class Settings:

	"""将游戏的参数设置都放在一个模块中"""
	def __init__(self):

		# 游戏屏幕
		self.bg_color = (100, 100, 100)
		self.screen_size = (1200, 800)
		self.screen_width, self.screen_height = self.screen_size

		# 板子
		self.board_width = 100
		self.board_height = 20
		self.board_color = (74, 138, 244)

		# 小球
		self.ball_width = 40
		self.ball_height = 40
		self.ball_color = (255, 200, 69)
		self.ball_speed_x = 1
		self.ball_speed_y = 0.6

		# 砖块
		self.brick_width = 70
		self.brick_height = 30
		self.brick_color = (25, 161, 94)

		# 墙
		self.row = 11
		self.column = 15

		# 道具
		self.heart_size = (30, 30)
		self.heart_num = 3
		self.lengthen_size = (40, 40)
		self.lengthen_num = 3
		self.lock_size = (50, 30)
		self.lock_num = 3
		self.turtle_size = (30, 30)
		self.turtle_num = 3
		self.through_wall_size = (70, 30)
		self.through_wall_num = 3