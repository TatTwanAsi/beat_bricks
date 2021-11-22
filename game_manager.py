import asyncio

from menu import Menu
from beat_bricks import BeatBricks

class LevelGetter:

	"""获取关卡信息的类"""
	def __init__(self):

		"""初始化"""
		self.level = None


if __name__ == "__main__":

	level_getter = LevelGetter()
	while True:
		m = Menu()
		m.run_menu(level_getter)
		print(1)
		if level_getter:
			bb = BeatBricks(level_getter.level)
			asyncio.run(bb.run_game())
		else:
			quit()