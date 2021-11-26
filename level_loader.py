import json

"""用于加载关卡的模块"""
def get_setting_attr_dict(level_num):

	if level_num == 1:
		filename = 'json/level_1.json'

	elif level_num == 2:
		filename = 'json/level_2.json'

	elif level_num == 3:
		filename = 'json/level_3.json'

	with open(filename) as file_object:

		settings_attributes_dict = json.load(file_object)
		return settings_attributes_dict

