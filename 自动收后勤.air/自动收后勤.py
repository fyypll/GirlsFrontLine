# -*- encoding=utf8 -*-
__author__ = "maple"

import datetime
from airtest.core.api import *
import logging
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)


auto_setup(__file__)

count = 0

def get_time():
	times = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	return times


def again_find():
	global count
	isexists1 = exists(Template(r"tpl1612894421046.png",record_pos=(-0.339, -0.077), resolution=(1440, 810)))
	if isexists1:
		touch(Template(r"tpl1612894421046.png",record_pos=(-0.339, -0.077), resolution=(1440, 810)))
		sleep(3)
		isexists2 = exists(Template(r"tpl1612894445416.png",record_pos=(0.001, -0.039), resolution=(1440, 810)))
		sleep(1)
		if isexists2:
			touch(Template(r"tpl1612894456578.png", record_pos=(0.082, 0.105), resolution=(1440, 810)))
			times = get_time()
			print("执行成功，当前时间>>"+times)
			count = count + 1
			print("成功收取后勤次数>>"+str(count))
	else:
		times = get_time()
		print("没有找到,当前时间>>"+times)

while True:
	sleep(60)
	again_find()
