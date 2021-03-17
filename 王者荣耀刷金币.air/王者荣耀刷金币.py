# -*- encoding=utf8 -*-
__author__ = "maple"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
import logging
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)

if not cli_setup():
 auto_setup(__file__, logdir=None, devices=[
         "Android://127.0.0.1:5037/127.0.0.1:7555",
 ])
#auto_setup(__file__)


def run_again(func):
    def wappper(*args, **keyargs):
        try:
            func(*args, **keyargs)
        except:
            start()
    return wappper


# 跳过
def pass_this():
    if exists(Template(r"tpl1614235660364.png", record_pos=(0.461, -0.258), resolution=(1280, 720))):
        touch(Template(r"tpl1614235660364.png", record_pos=(0.461, -0.258), resolution=(1280, 720)))
        sleep(6)
        pass_this()


def click_this():
    if exists(Template(r"tpl1615034602129.png", record_pos=(0.0, 0.222), resolution=(1440, 810))):
        touch(Template(r"tpl1615034602129.png", record_pos=(0.0, 0.222), resolution=(1440, 810)))
        sleep(4)
        click_this()


# 开始闯关
# @run_again
def start():
    if exists(Template(r"tpl1615034509758.png", record_pos=(0.319, 0.183), resolution=(1440, 810))) and exists(Template(r"tpl1615034526826.png", record_pos=(0.097, 0.182), resolution=(1440, 810))):
        touch(Template(r"tpl1615034509758.png", record_pos=(0.319, 0.183), resolution=(1440, 810)))

    sleep(30)
    wait(Template(r"tpl1614235660364.png", record_pos=(0.461, -0.258), resolution=(1280, 720)))
    pass_this()
    sleep(4)
    wait(Template(r"tpl1615034602129.png", record_pos=(0.0, 0.222), resolution=(1440, 810)))
    if exists(Template(r"tpl1615034602129.png", record_pos=(0.0, 0.222), resolution=(1440, 810))):
        touch(Template(r"tpl1615034602129.png", record_pos=(0.0, 0.222), resolution=(1440, 810)))
    sleep(3)
    click_this()
    sleep(4)


for i in range(1, 141):
    start()
    print("已执行第"+ str(i) +"次")





