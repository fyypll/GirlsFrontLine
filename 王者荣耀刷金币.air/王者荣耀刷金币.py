# -*- encoding=utf8 -*-
__author__ = "maple"

from airtest.core.api import *
import logging
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)

auto_setup(__file__)


def main_ui():
    wait(Template(r"tpl1614235268446.png", record_pos=(0.264, 0.14), resolution=(1280, 720)))
    touch(Template(r"tpl1614235268446.png", record_pos=(0.264, 0.14), resolution=(1280, 720)))
    sleep(1)
    wait(Template(r"tpl1614235318747.png", record_pos=(-0.435, -0.107), resolution=(1280, 720)))
    touch(Template(r"tpl1614235318747.png", record_pos=(-0.435, -0.107), resolution=(1280, 720)))
    sleep(1)
    wait(Template(r"tpl1614235361741.png", record_pos=(0.002, 0.048), resolution=(1280, 720)))
    touch(Template(r"tpl1614235361741.png", record_pos=(0.002, 0.048), resolution=(1280, 720)))
    sleep(1)
    wait(Template(r"tpl1614235505779.png", record_pos=(-0.235, -0.125), resolution=(1280, 720)))
    touch(Template(r"tpl1614235505779.png", record_pos=(-0.235, -0.125), resolution=(1280, 720)))
    wait(Template(r"tpl1614235540135.png", record_pos=(-0.025, -0.055), resolution=(1280, 720)))
    touch(Template(r"tpl1614235540135.png", record_pos=(-0.025, -0.055), resolution=(1280, 720)))
    wait(Template(r"tpl1614235451025.png", record_pos=(0.441, 0.102), resolution=(1280, 720)))
    touch(Template(r"tpl1614235451025.png", record_pos=(0.441, 0.102), resolution=(1280, 720)))
    wait(Template(r"tpl1614235573297.png", record_pos=(0.294, 0.22), resolution=(1280, 720)))
    touch(Template(r"tpl1614235573297.png", record_pos=(0.294, 0.22), resolution=(1280, 720)))
    sleep(1)


# 跳过
def pass_this():
    if exists(Template(r"tpl1614235660364.png", record_pos=(0.461, -0.258), resolution=(1280, 720))):
        touch(Template(r"tpl1614235660364.png", record_pos=(0.461, -0.258), resolution=(1280, 720)))
        sleep(6)
        pass_this()


# 开始闯关
def start():
    wait(Template(r"tpl1614235609211.png", record_pos=(0.317, 0.182), resolution=(1280, 720)))
    if exists(Template(r"tpl1614235609211.png", record_pos=(0.317, 0.182), resolution=(1280, 720))) and exists(Template(r"tpl1614236097958.png", record_pos=(0.098, 0.184), resolution=(1280, 720))):
        touch(Template(r"tpl1614235609211.png", record_pos=(0.317, 0.182), resolution=(1280, 720)))

    sleep(30)
    wait(Template(r"tpl1614235660364.png", record_pos=(0.461, -0.258), resolution=(1280, 720)))
    pass_this()
    
    sleep(4)
    wait(Template(r"tpl1614235756012.png", record_pos=(0.001, 0.223), resolution=(1280, 720)))
    if exists(Template(r"tpl1614235756012.png", record_pos=(0.001, 0.223), resolution=(1280, 720))):
        touch(Template(r"tpl1614235756012.png", record_pos=(0.001, 0.223), resolution=(1280, 720)))
    sleep(3)
    if exists(Template(r"tpl1614235788745.png", record_pos=(0.361, 0.233), resolution=(1280, 720))):
        touch(Template(r"tpl1614235788745.png", record_pos=(0.361, 0.233), resolution=(1280, 720)))
    sleep(4)

for i in range(1, 141):
    start()
    print("已执行第"+ str(i) +"次")





