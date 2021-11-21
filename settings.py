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
		self.lengthen_num = 3
		self.lock_num = 2
		self.through_wall_num = 3	
		self.turtle_num = 1
		# 道具大小
		self.heart_width = 50
		self.heart_height = 50
		self.lengthen_width = 60
		self.lengthen_height = 60
		self.lock_width = 60
		self.lock_height = 40
		self.through_wall_width = 80
		self.through_wall_height = 40
		self.turtle_width = 50
		self.turtle_height = 50
		# 道具效果持续时间
		self.lengthen_span_time = 3
		self.lock_span_time = 2
		self.through_wall_span_time = 3
		self.turtle_span_time = 2

		# UI设置
		self.UI_text_color = (246, 252, 249)
		