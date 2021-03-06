# -*- encoding=utf8 -*-

"""
准备工作：

本脚本基于airtest编写
使用的MuMu模拟器，分辨率1440*810

1.队伍配置
一队老板加打手zas
二队单独一个zas

2.注意点
让一队的zas和二队的zas先磨一点血，以保证在仓库中的受损排序是第一和第二位
先保证一队中的zas空弹药，二队的满弹药，因为进入地图后会将一队的zas和二队的zas互换
换完就开始部署编队开打了
"""

__author__ = "maple"

from airtest.core.api import *
from airtest.core.android.rotation import XYTransformer
from airtest.core.android.android import Android
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
        sleep(1.5)
    # 向外捏合
    dev.pinch(in_or_out='out', center=None, percent=0.1)
    sleep(2.5)
    # 如果点到了重装，那么关闭并重新缩放
    is_zz = exists(Template(r"tpl1613063270994.png", record_pos=(-0.297, -0.212), resolution=(1440, 810)))
    if is_zz:
        wait(Template(r"tpl1613063307567.png", record_pos=(0.246, 0.224), resolution=(1440, 810)))
        touch(Template(r"tpl1613063307567.png", record_pos=(0.246, 0.224), resolution=(1440, 810)))
        sleep(2)
        neihe()


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
    sleep(1)
    wait(Template(r"tpl1612973050340.png",
                  record_pos=(-0.276, -0.206), resolution=(1440, 810)))
    touch(Template(r"tpl1612973088470.png", record_pos=(
        0.408, 0.216), resolution=(1440, 810)))


# 更换打手，默认为二号位
def change_renxing():
    airport_bottom_left()
    sleep(2)
    wait(Template(r"tpl1612973222920.png",
                   record_pos=(-0.301, 0.21), resolution=(1440, 810)))
    touch(Template(r"tpl1612973222920.png",
                   record_pos=(-0.301, 0.21), resolution=(1440, 810)))
    sleep(2)
    wait(Template(r"tpl1612973262610.png",
                  record_pos=(-0.188, -0.237), resolution=(1440, 810)))
    wait(Template(r"tpl1612973337422.png",
                   record_pos=(-0.158, -0.097), resolution=(1440, 810)))
    touch(Template(r"tpl1612973337422.png",
                   record_pos=(-0.158, -0.097), resolution=(1440, 810)))
    sleep(2)
    wait(Template(r"tpl1612973383265.png", record_pos=(
        0.423, -0.147), resolution=(1440, 810)))
    touch(Template(r"tpl1612973383265.png", record_pos=(
        0.423, -0.147), resolution=(1440, 810)))
    sleep(2)
    wait(Template(r"tpl1612973435192.png", record_pos=(
        0.253, 0.174), resolution=(1440, 810)))
    touch(Template(r"tpl1612973435192.png", record_pos=(
        0.253, 0.174), resolution=(1440, 810)))
    sleep(2)
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
    # wait(Template(r"tpl1612984403815.png", target_pos=4, record_pos=(-0.235, -0.151), resolution=(1440, 810)),timeout=40)

    # touch(Template(r"tpl1612984403815.png", target_pos=4, record_pos=(-0.235, -0.151), resolution=(1440, 810)))
    touch([335, 176])
    sleep(2)
    # touch(Template(r"tpl1612984403815.png", target_pos=4, record_pos=(-0.235, -0.151), resolution=(1440, 810)))
    touch([335, 176])
    sleep(1)
    wait(Template(r"tpl1612980772706.png", record_pos=(0.438, 0.157), resolution=(1440, 810)))
    touch(Template(r"tpl1612980772706.png", record_pos=(0.438, 0.157), resolution=(1440, 810)))
    sleep(2)
    wait(Template(r"tpl1612985718458.png", target_pos=4, record_pos=(-0.234, -0.155), resolution=(1440, 810)))
    touch(Template(r"tpl1612985718458.png", target_pos=4, record_pos=(-0.234, -0.155), resolution=(1440, 810)))
    sleep(5)
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
    # wait(Template(r"tpl1612984658766.png", target_pos=5, record_pos=(-0.278, 0.188), resolution=(1440, 810)))
    # touch(Template(r"tpl1612984658766.png", target_pos=4, record_pos=(-0.278, 0.188), resolution=(1440, 810)))
    touch([275, 680])
    sleep(2)
    wait(Template(r"tpl1612981435916.png", target_pos=1, record_pos=(-0.215, 0.031), resolution=(1440, 810)))
    touch(Template(r"tpl1612981435916.png", target_pos=1, record_pos=(-0.215, 0.031), resolution=(1440, 810)))
    sleep(2)
    wait(Template(r"tpl1612984857140.png", target_pos=3, record_pos=(-0.288, 0.033), resolution=(1440, 810)))
    touch(Template(r"tpl1612984857140.png", target_pos=3, record_pos=(-0.288, 0.033), resolution=(1440, 810)))

    sleep(3)
    touch(Template(r"tpl1612981707528.png", record_pos=(0.426, 0.231), resolution=(1440, 810)))
    # 如果遇到没有弹药和口粮遇敌必败弹窗则重开
    no_food_restart()
    # 重开后，在地图上开始布局
    ditu_plan()
    

# 如果装备仓库满了，就拆装备
def storehouse_full():
    is_full = exists(Template(r"tpl1613035020293.png", record_pos=(0.0, -0.057), resolution=(1440, 810)))
    if is_full:
        wait(Template(r"tpl1613035033982.png", record_pos=(0.128, 0.106), resolution=(1440, 810)))
        touch(Template(r"tpl1613035033982.png", record_pos=(0.128, 0.106), resolution=(1440, 810)))
        sleep(2)
        wait(Template(r"tpl1612973584765.png", target_pos=4,
                       record_pos=(-0.369, -0.24), resolution=(1440, 810)))
        touch(Template(r"tpl1612973584765.png", target_pos=4,
                       record_pos=(-0.369, -0.24), resolution=(1440, 810)))
        sleep(2)
        chaizhuangbei()
    
        
# 拆解装备
def chaizhuangbei():
    # 拆白色装备
    # 在主页进行定位
    wait(Template(r"tpl1613035238319.png", record_pos=(0.399, -0.062), resolution=(1440, 810)))
    touch(Template(r"tpl1613035238319.png", record_pos=(0.399, -0.062), resolution=(1440, 810)))
    sleep(2)
    wait(Template(r"tpl1613035315767.png", record_pos=(-0.41, 0.048), resolution=(1440, 810)))
    touch(Template(r"tpl1613035315767.png", record_pos=(-0.41, 0.048), resolution=(1440, 810)))
    sleep(2)
    wait(Template(r"tpl1613035339578.png", record_pos=(-0.058, -0.119), resolution=(1440, 810)))
    
    touch(Template(r"tpl1613035339578.png", record_pos=(-0.058, -0.119), resolution=(1440, 810)))
    sleep(2)
    wait(Template(r"tpl1613037738897.png", record_pos=(-0.231, -0.24), resolution=(1440, 810)))
    wait(Template(r"tpl1613037856497.png", record_pos=(0.426, 0.109), resolution=(1440, 810)))
    touch(Template(r"tpl1613037856497.png", record_pos=(0.426, 0.109), resolution=(1440, 810)))
    sleep(2)

    wait(Template(r"tpl1613037838594.png", record_pos=(0.425, 0.108), resolution=(1440, 810)))
    wait(Template(r"tpl1613037917903.png", record_pos=(0.422, 0.214), resolution=(1440, 810)))
    touch(Template(r"tpl1613037917903.png", record_pos=(0.422, 0.214), resolution=(1440, 810)))
    sleep(2)
    wait(Template(r"tpl1613037938745.png", record_pos=(0.426, 0.224), resolution=(1440, 810)))
    touch(Template(r"tpl1613037938745.png", record_pos=(0.426, 0.224), resolution=(1440, 810)))
    sleep(2)
    wait(Template(r"tpl1613037981165.png", record_pos=(0.334, -0.15), resolution=(1440, 810)))
    wait(Template(r"tpl1613037987997.png", record_pos=(0.386, 0.192), resolution=(1440, 810)))
    touch(Template(r"tpl1613037987997.png", record_pos=(0.386, 0.192), resolution=(1440, 810)))
    sleep(2)
    # 准备拆解蓝色装备
    wait(Template(r"tpl1613035339578.png", record_pos=(-0.058, -0.119), resolution=(1440, 810)))

    touch(Template(r"tpl1613035339578.png", record_pos=(-0.058, -0.119), resolution=(1440, 810)))
    
    # 预估为12件，都选中
    for i in range(12):
        wait(Template(r"tpl1613037838594.png", record_pos=(0.425, 0.108), resolution=(1440, 810)))
        touch(Template(r"tpl1613052692777.png", record_pos=(-0.409, -0.186), resolution=(1440, 810)))
        sleep(1)
    wait(Template(r"tpl1613037938745.png", record_pos=(0.426, 0.224), resolution=(1440, 810)))
    touch(Template(r"tpl1613037938745.png", record_pos=(0.426, 0.224), resolution=(1440, 810)))
    sleep(2)
    wait(Template(r"tpl1613037981165.png", record_pos=(0.334, -0.15), resolution=(1440, 810)))
    wait(Template(r"tpl1613037987997.png", record_pos=(0.386, 0.192), resolution=(1440, 810)))
    touch(Template(r"tpl1613037987997.png", record_pos=(0.386, 0.192), resolution=(1440, 810)))
    sleep(2)
    wait(Template(r"tpl1613104619512.png", record_pos=(0.031, -0.183), resolution=(1440, 810)))
    wait(Template(r"tpl1613104632746.png", record_pos=(0.099, 0.207), resolution=(1440, 810)))
    touch(Template(r"tpl1613104632746.png", record_pos=(0.099, 0.207), resolution=(1440, 810)))
    sleep(2)
    # 拆完装备回到首页
    wait(Template(r"tpl1612973584765.png", target_pos=4,
                   record_pos=(-0.369, -0.24), resolution=(1440, 810)))
    touch(Template(r"tpl1612973584765.png", target_pos=4,
                   record_pos=(-0.369, -0.24), resolution=(1440, 810)))
    sleep(2)
        
        
# 遇到更换失败，显示弹药口粮耗尽遇敌必败则重开
def no_food_restart():
    sleep(2)
    is_exists = exists(Template(r"tpl1613045862916.png", record_pos=(-0.046, -0.057), resolution=(1440, 810)))
    if is_exists:
        touch(Template(r"tpl1613045874272.png", record_pos=(-0.09, 0.106), resolution=(1440, 810)))
        restart()
        # 重启若遇到装备爆仓
        storehouse_full()
        # close_and_start()
    

# 重新战斗
def restart():
    wait(Template(r"tpl1612983057440.png", record_pos=(-0.255, -0.242), resolution=(1440, 810)))
    touch(Template(r"tpl1612983057440.png", record_pos=(-0.255, -0.242), resolution=(1440, 810)))
    sleep(2)
    wait(Template(r"tpl1612983068454.png", record_pos=(-0.116, 0.105), resolution=(1440, 810)))
    touch(Template(r"tpl1612983068454.png", record_pos=(-0.116, 0.105), resolution=(1440, 810)))
    sleep(6)


# 终止战斗并返回主界面
def end_fight():
    wait(Template(r"tpl1612983057440.png", record_pos=(-0.255, -0.242), resolution=(1440, 810)))
    touch(Template(r"tpl1612983057440.png", record_pos=(-0.255, -0.242), resolution=(1440, 810)))
    sleep(2)
    wait(Template(r"tpl1613057829277.png", record_pos=(0.12, 0.104), resolution=(1440, 810)))
    touch(Template(r"tpl1613057829277.png", record_pos=(0.12, 0.104), resolution=(1440, 810)))
    sleep(2)
    wait(Template(r"tpl1612973584765.png", target_pos=4,
                   record_pos=(-0.369, -0.24), resolution=(1440, 810)))
    touch(Template(r"tpl1612973584765.png", target_pos=4,
                   record_pos=(-0.369, -0.24), resolution=(1440, 810)))
    sleep(2)
    


# 收后勤任务
def houqin():
	isexists1 = exists(Template(r"tpl1612894421046.png",record_pos=(-0.339, -0.077), resolution=(1440, 810)))
	if isexists1:
		touch(Template(r"tpl1612894421046.png",record_pos=(-0.339, -0.077), resolution=(1440, 810)))
		sleep(3)
		isexists2 = exists(Template(r"tpl1612894445416.png",record_pos=(0.001, -0.039), resolution=(1440, 810)))
		sleep(1)
		if isexists2:
			touch(Template(r"tpl1612894456578.png", record_pos=(0.082, 0.105), resolution=(1440, 810)))


# 在游戏主界面进入8-1n
def main_in_81n():
	# 先判断有没有后勤归来的队伍
    isexists1 = exists(Template(r"tpl1612894421046.png",record_pos=(-0.339, -0.077), resolution=(1440, 810)))
    if isexists1:
        for i in range(4):
            houqin()
            sleep(5)
    is_main = exists(Template(r"tpl1613054174818.png", record_pos=(0.245, 0.051), resolution=(1440, 810)))
    # 如果在游戏主界面
    if is_main:
        wait(Template(r"tpl1613054174818.png", record_pos=(0.245, 0.051), resolution=(1440, 810)))
        touch(Template(r"tpl1613054174818.png", record_pos=(0.245, 0.051), resolution=(1440, 810)))
        sleep(1)
        wait(Template(r"tpl1613054490281.png", record_pos=(-0.294, 0.024), resolution=(1440, 810)))
        # 获取当前手机设备
        dev = device()
        # 手指按照顺序依次滑过多个坐标,滑三次以保证滑到底
        for i in range(3):
            dev.swipe_along([[260, 644],[283, 286]])
        sleep(2)
        wait(Template(r"tpl1613055791912.png", record_pos=(-0.317, -0.199), resolution=(1440, 810)))
        touch(Template(r"tpl1613055791912.png", target_pos=8, record_pos=(-0.317, -0.199), resolution=(1440, 810)))
        sleep(1)
        is_81n = exists(Template(r"tpl1613056147161.png", record_pos=(-0.122, -0.153), resolution=(1440, 810)))
        if is_81n:
            wait(Template(r"tpl1613056227863.png", record_pos=(0.449, -0.131), resolution=(1440, 810)))
            touch(Template(r"tpl1613056227863.png", record_pos=(0.449, -0.131), resolution=(1440, 810)))
            sleep(2)

            wait(Template(r"tpl1613061952109.png", record_pos=(0.0, -0.067), resolution=(1440, 810)))
            touch(Template(r"tpl1613061952109.png", record_pos=(0.0, -0.067), resolution=(1440, 810)))
            sleep(2)
            wait(Template(r"tpl1613056446830.png", record_pos=(0.278, 0.181), resolution=(1440, 810)))
            touch(Template(r"tpl1613056446830.png", record_pos=(0.278, 0.181), resolution=(1440, 810)))
            sleep(8)


# 从8-1n返回主界面
# def back_home():
# wait(Template(r"tpl1613057498610.png", record_pos=(-0.445, -0.234), resolution=(1440, 810)))
# touch(Template(r"tpl1613057498610.png", record_pos=(-0.445, -0.234), resolution=(1440, 810)))
# sleep(2)
# wait(Template(r"tpl1612973584765.png", target_pos=4,
#                        record_pos=(-0.369, -0.24), resolution=(1440, 810)))
# touch(Template(r"tpl1612973584765.png", target_pos=4,
#                        record_pos=(-0.369, -0.24), resolution=(1440, 810)))


# 返回主界面
# 关闭app，重新登录
def close_and_start():
    # 如果在战斗地图中，就终止作战
    is_figth = exists(Template(r"tpl1612983057440.png", record_pos=(-0.255, -0.242), resolution=(1440, 810)))
    if is_figth:
        # 终止战斗并返回主界面
        end_fight()
    else:
        # 获取设备
        dev = device()
        # 关闭少女前线
        stop_app('com.sunborn.girlsfrontline.cn')
        sleep(5)
        # 打开少女前线
        start_app('com.sunborn.girlsfrontline.cn')
        sleep(10)
        wait(Template(r"tpl1613108555413.png", record_pos=(0.001, 0.186), resolution=(1440, 810)))
        touch(Template(r"tpl1613108555413.png", record_pos=(0.001, 0.186), resolution=(1440, 810)))
        sleep(15)
        wait(Template(r"tpl1613108634772.png", record_pos=(-0.297, -0.178), resolution=(1440, 810)))
        touch(Template(r"tpl1613108634772.png", record_pos=(-0.297, -0.178), resolution=(1440, 810)))
        sleep(10)


# 进入到地图则开始布局
def ditu_plan():
    # 缩放地图复位
    neihe()
    # 更换打手
    change_renxing()
    # 缩放地图复位
    neihe()
    # 部署两个梯队
    select_two_team()
    # 确认开始
    start()
    sleep(2)
    # wait(Template(r"tpl1612980410750.png", record_pos=(-0.153, -0.235), resolution=(1440, 810)))
    # 给二队补给并撤退
    buji_chetui()


# 炸狗流程
def start_zhagou(num):
    # 在游戏主界面进入炸狗图
    main_in_81n()
    # 进入地图开始布局
    ditu_plan()
    # 给一队规划炸狗路线并执行
    plan_route()
    sleep(150)
    # wait(Template(r"tpl1612983018269.png", record_pos=(0.049, 0.004), resolution=(1440, 810)),timeout=40)
    is_exist = exists(Template(r"tpl1612983018269.png", record_pos=(0.049, 0.004), resolution=(1440, 810)))
    if is_exist:
        # 如果已经作战15次啦
        if num % 15 == 0:
            # 回主界面
            # back_home()
            # 终止战斗并返回主界面
            end_fight()
            sleep(5)
            # 查看有木有后勤归来
            for i in range(4):
                houqin()
                sleep(5)
            # 开拆装备
            chaizhuangbei()
        else:
            # 重启地图
            restart()
            sleep(5)
            # 装备仓库满了就拆装备
            storehouse_full()

    
# 打算运行多少次
def again_zhagou(num):
    for i in range(num):
        print("当前执行次数 >> " + str(i+1))
        # 把循环的次数传进去方便判断
        start_zhagou(i+1)



# dev = device()
# # 输出设备上安装的软件的包名
# print(dev.list_app(third_only=True))
# # 关闭少女前线
# stop_app('com.sunborn.girlsfrontline.cn')
# # 打开少女前线
# start_app('com.sunborn.girlsfrontline.cn')

        
# 开始炸狗，输入要打多少把
again_zhagou(140)

