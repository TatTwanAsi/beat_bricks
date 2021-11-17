class Settings:

	"""将游戏的参数设置都放在一个模块中"""
	def __init__(self):

		# 游戏屏幕
		self.bg_color = (30, 30, 30)
		self.screen_size = (1200, 800)
		self.screen_width, self.screen_height = self.screen_size