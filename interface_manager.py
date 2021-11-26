import pygame
import asyncio

from main_menu_interface import MainMenuInterface
from level_select_interface import LevelSelectInterface
from game_interface import GameInterface

class InterfaceManager:

	"""管理界面的类"""
	def __init__(self):

		self.interface = MainMenuInterface()


	async def run_interface(self):

		# 运行界面
		while True:
			task_interface_update = asyncio.create_task(self.interface.update())
			next_interface = await task_interface_update
			if next_interface:
				self._switch_interface(next_interface)
			


	def _switch_interface(self, other_interface):

		# 切换界面
		if other_interface == 'main_menu':
			self.interface = MainMenuInterface()
		elif other_interface == 'level_select':
			self.interface = LevelSelectInterface()
		elif other_interface == 'level_1':
			self.interface = GameInterface(1)
		elif other_interface == 'level_2':
			self.interface = GameInterface(2)
		elif other_interface == 'level_3':
			self.interface = GameInterface(3)

