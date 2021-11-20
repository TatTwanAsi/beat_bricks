class Settings:

	"""将游戏的参数设置都放在一个模块中"""
	def __init__(self):

		# 游戏屏幕
		self.bg_color = (100, 100, 100)
		self.screen_size = (1200, 800)
		self.screen_width, self.screen_height = self.screen_size

		# 板子
		self.board_width = 200
		self.board_height = 20
		self.board_color = (74, 138, 244)

		# 小球
		self.ball_width = 40
		self.ball_height = 40
		self.ball_color = (255, 200, 69)
		self.ball_speed_x = 0.6
		self.ball_speed_y = 0.8
		self.ball_number = 3	# 小球的个数

		# 砖块
		self.brick_width = 115 
		self.brick_height = 45 
		self.brick_color = (25, 161, 94)

		# 墙
		self.row = 7
		self.column = 9

		# 道具
		self.heart_num = 2
		self.lengthen_num = 1
		self.lock_num = 1
		self.through_wall_num = 2	
		self.turtle_num = 2

		self.heart_size = (50, 50)
		self.lengthen_size = (60, 80)
		self.lock_size = (60, 40)
		self.through_wall_size = (80, 40)
		self.turtle_size = (50, 50)
		
		