import pygame
import asyncio
import time
import sys
from pygame.sprite import Sprite

from settings import Settings
from board import Board
from ball import Ball
from bonus_manager import BonusManager
from bricks_manager import BricksManager
from UI_manager import UIManager
from level_loader import get_setting_attr_dict
from interface_manager import InterfaceManager

class BeatBricks:

	"""管理《打砖块》的游戏资源以及行为"""
	def __init__(self):

		"""创建界面管理对象，进入主菜单"""
		self.interface_manager = InterfaceManager()


if __name__ == "__main__":

	bb = BeatBricks()
	asyncio.run(bb.interface_manager.run_interface())