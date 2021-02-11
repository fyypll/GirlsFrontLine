# -*- encoding=utf8 -*-
__author__ = "maple"

from airtest.core.api import *
import logging
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)


auto_setup(__file__)

# 缩放战场地图方便重新定位
def neihe():
    # 获取当前手机设备
    dev = device()
    # 向内捏合
    for i in range(2):
        dev.pinch(in_or_out='in', center=None, percent=0.5)
        sleep(2.5)
    # 向外捏合
    dev.pinch(in_or_out='out', center=None, percent=0.1)
    sleep(2.5)


# 是否确定开始
def start():
    wait(Template(r"tpl1612972801554.png", record_pos=(
        0.387, 0.231), resolution=(1440, 810)))
    touch(Template(r"tpl1612972801554.png", record_pos=(
        0.387, 0.231), resolution=(1440, 810)))
        
    

# 点击左下角的机场
def airport_bottom_left():
    wait(Template(r"tpl1612978855358.png", target_pos=9, record_pos=(-0.389, 0.18), resolution=(1440, 810)))
    touch(Template(r"tpl1612978855358.png", target_pos=9, record_pos=(-0.389, 0.18), resolution=(1440, 810)))


# 点击左上角的机场
def airport_top_left():
    wait(Template(r"tpl1612978949744.png", target_pos=9, record_pos=(-0.319, -0.199), resolution=(1440, 810)))
    touch(Template(r"tpl1612978949744.png", target_pos=9, record_pos=(-0.319, -0.199), resolution=(1440, 810)))



# 确定部署梯队
def confirm_team():
    wait(Template(r"tpl1612973050340.png",
                  record_pos=(-0.276, -0.206), resolution=(1440, 810)))
    touch(Template(r"tpl1612973088470.png", record_pos=(
        0.408, 0.216), resolution=(1440, 810)))


# 更换打手，默认为二号位
def change_renxing():
    airport_bottom_left()
    wait(Template(r"tpl1612973222920.png",
                   record_pos=(-0.301, 0.21), resolution=(1440, 810)))
    touch(Template(r"tpl1612973222920.png",
                   record_pos=(-0.301, 0.21), resolution=(1440, 810)))
    wait(Template(r"tpl1612973262610.png",
                  record_pos=(-0.188, -0.237), resolution=(1440, 810)))
    wait(Template(r"tpl1612973337422.png",
                   record_pos=(-0.158, -0.097), resolution=(1440, 810)))
    touch(Template(r"tpl1612973337422.png",
                   record_pos=(-0.158, -0.097), resolution=(1440, 810)))
    wait(Template(r"tpl1612973383265.png", record_pos=(
        0.423, -0.147), resolution=(1440, 810)))
    touch(Template(r"tpl1612973383265.png", record_pos=(
        0.423, -0.147), resolution=(1440, 810)))
    wait(Template(r"tpl1612973435192.png", record_pos=(
        0.253, 0.174), resolution=(1440, 810)))
    touch(Template(r"tpl1612973435192.png", record_pos=(
        0.253, 0.174), resolution=(1440, 810)))
    wait(Template(r"tpl1612974573045.png", threshold=0.7, rgb=True,
                  target_pos=8, record_pos=(-0.265, -0.176), resolution=(1440, 810)))
    touch(Template(r"tpl1612974573045.png", threshold=0.7, rgb=True,
                   target_pos=8, record_pos=(-0.265, -0.176), resolution=(1440, 810)))
    sleep(2)
    wait(Template(r"tpl1612973584765.png", target_pos=4,
                   record_pos=(-0.369, -0.24), resolution=(1440, 810)))
    touch(Template(r"tpl1612973584765.png", target_pos=4,
                   record_pos=(-0.369, -0.24), resolution=(1440, 810)))

    
# 给二队补给并撤退
def buji_chetui():
    sleep(12)
    wait(Template(r"tpl1612984403815.png", target_pos=4, record_pos=(-0.235, -0.151), resolution=(1440, 810)))

    touch(Template(r"tpl1612984403815.png", target_pos=4, record_pos=(-0.235, -0.151), resolution=(1440, 810)))
    sleep(2)
    touch(Template(r"tpl1612984403815.png", target_pos=4, record_pos=(-0.235, -0.151), resolution=(1440, 810)))
    wait(Template(r"tpl1612980772706.png", record_pos=(0.438, 0.157), resolution=(1440, 810)))
    touch(Template(r"tpl1612980772706.png", record_pos=(0.438, 0.157), resolution=(1440, 810)))
    sleep(2)
    wait(Template(r"tpl1612985718458.png", target_pos=4, record_pos=(-0.234, -0.155), resolution=(1440, 810)))
    touch(Template(r"tpl1612985718458.png", target_pos=4, record_pos=(-0.234, -0.155), resolution=(1440, 810)))
    wait(Template(r"tpl1612980931491.png", record_pos=(0.263, 0.214), resolution=(1440, 810)))
    touch(Template(r"tpl1612980931491.png", record_pos=(0.263, 0.214), resolution=(1440, 810)))
    sleep(2)
    wait(Template(r"tpl1612984519435.png", record_pos=(-0.006, -0.037), resolution=(1440, 810)))
    touch(Template(r"tpl1612984551637.png", record_pos=(0.083, 0.107), resolution=(1440, 810)))


    
# 回到地图，部署两个队伍
def select_two_team():
    airport_bottom_left()
    confirm_team()
    airport_top_left()
    confirm_team()
    

# 给一队规划炸狗路线
def plan_route():
    wait(Template(r"tpl1612981259942.png", target_pos=6, record_pos=(-0.367, 0.178), resolution=(1440, 810)))
    touch(Template(r"tpl1612981259942.png", target_pos=6, record_pos=(-0.367, 0.178), resolution=(1440, 810)))
    sleep(2)
    touch(Template(r"tpl1612981328795.png", record_pos=(-0.44, 0.181), resolution=(1440, 810)))
    sleep(2)
    wait(Template(r"tpl1612984658766.png", target_pos=5, record_pos=(-0.278, 0.188), resolution=(1440, 810)))
    touch(Template(r"tpl1612984658766.png", target_pos=4, record_pos=(-0.278, 0.188), resolution=(1440, 810)))
    sleep(2)
    wait(Template(r"tpl1612981435916.png", target_pos=1, record_pos=(-0.215, 0.031), resolution=(1440, 810)))
    touch(Template(r"tpl1612981435916.png", target_pos=1, record_pos=(-0.215, 0.031), resolution=(1440, 810)))
    sleep(2)
    wait(Template(r"tpl1612984857140.png", target_pos=3, record_pos=(-0.288, 0.033), resolution=(1440, 810)))
    touch(Template(r"tpl1612984857140.png", target_pos=3, record_pos=(-0.288, 0.033), resolution=(1440, 810)))

    sleep(2)
    touch(Template(r"tpl1612981707528.png", record_pos=(0.426, 0.231), resolution=(1440, 810)))


# 炸狗流程
def start_zhagou():
    # 首先缩放地图复位
    neihe()
    # 更换打手
    change_renxing()
    # 部署两个梯队
    select_two_team()
    # 确认开始
    start()
    wait(Template(r"tpl1612980410750.png", record_pos=(-0.153, -0.235), resolution=(1440, 810)))
    # 给二队补给并撤退
    buji_chetui()
    # 给一队规划炸狗路线并执行
    plan_route()
    sleep(150)
    wait(Template(r"tpl1612983018269.png", record_pos=(0.049, 0.004), resolution=(1440, 810)))
    wait(Template(r"tpl1612983057440.png", record_pos=(-0.255, -0.242), resolution=(1440, 810)))
    touch(Template(r"tpl1612983057440.png", record_pos=(-0.255, -0.242), resolution=(1440, 810)))
    wait(Template(r"tpl1612983068454.png", record_pos=(-0.116, 0.105), resolution=(1440, 810)))
    touch(Template(r"tpl1612983068454.png", record_pos=(-0.116, 0.105), resolution=(1440, 810)))
    sleep(6)

    
# 重复多少把
def again_zhagou(cishu):
    for i in range(cishu):
        start_zhagou()

        
# 开始炸狗，输入要打多少把
again_zhagou(140)