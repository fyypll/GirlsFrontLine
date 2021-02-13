# -*- encoding=utf8 -*-

"""
准备工作：

本脚本基于airtest编写
使用的MuMu模拟器，分辨率1440*810

1.队伍配置
一队放老板和zas
二队单独一个zas

2.注意点
让一队的zas和二队的zas先磨一点血，以保证在仓库中的受损排序是第一和第二位
先保证一队中的zas空弹药，二队的满弹药，因为进入地图后会将一队的zas和二队的zas互换
换完就开始部署梯队开打了

"""

__author__ = "maple"

from airtest.core.api import *
from airtest.core.android.rotation import XYTransformer
from airtest.core.android.android import Android
import datetime
import logging
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)

auto_setup(__file__)

# 设置隐式(默认)等待时长
# touch、wait、swipe的第一张图片识别时长，assert_exists、double_click的断言时长将受此影响
ST.FIND_TIMEOUT=60


# 缩放地图复位
def scaling():
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
    if exists(Template(r"tpl1613063270994.png", record_pos=(-0.297, -0.212), resolution=(1440, 810))):
        touch(Template(r"tpl1613063307567.png", record_pos=(0.246, 0.224), resolution=(1440, 810)))
        sleep(2)
        scaling()


# 关闭游戏并重开
def close_and_start():
    # 如果在战斗地图中，就终止作战
    if exists(Template(r"tpl1612983057440.png", record_pos=(-0.255, -0.242), resolution=(1440, 810))):
        # 终止战斗并返回主界面
        end_fight()
    # 获取设备
    dev = device()
    # 关闭少女前线
    stop_app('com.sunborn.girlsfrontline.cn')
    sleep(5)
    # 打开少女前线
    start_app('com.sunborn.girlsfrontline.cn')
    sleep(10)
    wait(Template(r"tpl1613108555413.png", record_pos=(0.001, 0.186), resolution=(1440, 810)))
    sleep(2)
    touch(Template(r"tpl1613108555413.png", record_pos=(0.001, 0.186), resolution=(1440, 810)))
    sleep(15)
    wait(Template(r"tpl1613108634772.png", record_pos=(-0.297, -0.178), resolution=(1440, 810)))
    sleep(2)
    touch(Template(r"tpl1613108634772.png", record_pos=(-0.297, -0.178), resolution=(1440, 810)))
    # 点击后等待15s左右，大概就进入游戏主界面了
    sleep(15)


# 终止战斗并返回主界面
def end_fight():
    wait(Template(r"tpl1612983057440.png", record_pos=(-0.255, -0.242), resolution=(1440, 810)))
    touch(Template(r"tpl1612983057440.png", record_pos=(-0.255, -0.242), resolution=(1440, 810)))
    sleep(2)
    wait(Template(r"tpl1613057829277.png", record_pos=(0.12, 0.104), resolution=(1440, 810)))
    touch(Template(r"tpl1613057829277.png", record_pos=(0.12, 0.104), resolution=(1440, 810)))
    sleep(2)
    wait(Template(r"tpl1612973584765.png", target_pos=4, record_pos=(-0.369, -0.24), resolution=(1440, 810)))
    # 终止作战会切换画面，出现图标等待2s以保证能成功点到
    sleep(2)
    touch(Template(r"tpl1612973584765.png", target_pos=4, record_pos=(-0.369, -0.24), resolution=(1440, 810)))
    sleep(2)


# 是否确认部署开始回合
def start():
    wait(Template(r"tpl1612972801554.png", record_pos=(
        0.387, 0.231), resolution=(1440, 810)))
    touch(Template(r"tpl1612972801554.png", record_pos=(
        0.387, 0.231), resolution=(1440, 810)))
    sleep(4)
    # 如果重启地图了弹窗提示装备爆仓了
    if storehouse_full():
        # 从首页进入工厂拆装备
        chai_zhuang_bei()
    sleep(8)


# 点击左下角的机场
def airport_bottom_left():
    wait(Template(r"tpl1612978855358.png", target_pos=9, record_pos=(-0.389, 0.18), resolution=(1440, 810)))
    touch(Template(r"tpl1612978855358.png", target_pos=9, record_pos=(-0.389, 0.18), resolution=(1440, 810)))
    sleep(2)


# 点击左上角的机场
def airport_top_left():
    wait(Template(r"tpl1612978949744.png", target_pos=9, record_pos=(-0.319, -0.199), resolution=(1440, 810)))
    touch(Template(r"tpl1612978949744.png", target_pos=9, record_pos=(-0.319, -0.199), resolution=(1440, 810)))
    sleep(2)


# 确定部署梯队
def confirm_team():
    sleep(1)
    wait(Template(r"tpl1612973050340.png",
              record_pos=(-0.276, -0.206), resolution=(1440, 810)))
    sleep(1)
    touch(Template(r"tpl1612973088470.png", record_pos=(
    0.408, 0.216), resolution=(1440, 810)))
    sleep(1)


# 如果没有点击到导致不弹出部署队伍界面
def no_team():
    # 那就再次缩放地图
    scaling()
    # 再点一次左下角使其弹出部署队伍界面
    airport_bottom_left()


# 更换zas
def change_zas():
    # 首先点击左下角弹出部署队伍界面
    airport_bottom_left()
    wait(Template(r"tpl1612973222920.png", record_pos=(-0.301, 0.21), resolution=(1440, 810)),intervalfunc=no_team)
    touch(Template(r"tpl1612973222920.png", record_pos=(-0.301, 0.21), resolution=(1440, 810)))
    sleep(3)
    wait(Template(r"tpl1612973262610.png", record_pos=(-0.188, -0.237), resolution=(1440, 810)))
    wait(Template(r"tpl1612973337422.png", record_pos=(-0.158, -0.097), resolution=(1440, 810)))
    touch(Template(r"tpl1612973337422.png", record_pos=(-0.158, -0.097), resolution=(1440, 810)))
    sleep(2)
    wait(Template(r"tpl1612973383265.png", record_pos=(0.423, -0.147), resolution=(1440, 810)))
    touch(Template(r"tpl1612973383265.png", record_pos=(0.423, -0.147), resolution=(1440, 810)))
    sleep(0.5)
    wait(Template(r"tpl1612973435192.png", record_pos=(0.253, 0.174), resolution=(1440, 810)))
    touch(Template(r"tpl1612973435192.png", record_pos=(0.253, 0.174), resolution=(1440, 810)))
    sleep(1)
    wait(Template(r"tpl1612974573045.png", threshold=0.7, rgb=True, target_pos=8, record_pos=(-0.265, -0.176), resolution=(1440, 810)))
    touch(Template(r"tpl1612974573045.png", threshold=0.7, rgb=True, target_pos=8, record_pos=(-0.265, -0.176), resolution=(1440, 810)))
    sleep(1)
    wait(Template(r"tpl1612973584765.png", target_pos=4, record_pos=(-0.369, -0.24), resolution=(1440, 810)))
    touch(Template(r"tpl1612973584765.png", target_pos=4, record_pos=(-0.369, -0.24), resolution=(1440, 810)))
    # 返地图会切换画面，等待5s
    sleep(5)


# 给左上角小队补给并撤退
def supply_and_retreat():
    # wait(Template(r"tpl1612984403815.png", target_pos=4, record_pos=(-0.235, -0.151), resolution=(1440, 810)))
    # touch(Template(r"tpl1612984403815.png", target_pos=4, record_pos=(-0.235, -0.151), resolution=(1440, 810)))
    # touch(Template(r"tpl1612984403815.png", target_pos=4, record_pos=(-0.235, -0.151), resolution=(1440, 810)))
    # 点击选中左上角梯队
    # 上面图片识别有一定几率识别为一队导致脚本出错，遂改为坐标
    # 缩放地图复位，避免点击坐标位置不对
    scaling()
    touch([335, 176])
    sleep(2)
    touch([335, 176])
    sleep(1)
    wait(Template(r"tpl1612980772706.png", record_pos=(0.438, 0.157), resolution=(1440, 810)))
    touch(Template(r"tpl1612980772706.png", record_pos=(0.438, 0.157), resolution=(1440, 810)))
    sleep(2)
    # 等2s以免出现网络波动
    # 补给后左上角小队口粮弹药都是满的，右下角的梯队显示是空的
    # 所以识别没有问题，不会出错识别到右下角梯队去
    wait(Template(r"tpl1612985718458.png", target_pos=4, record_pos=(-0.234, -0.155), resolution=(1440, 810)))
    touch(Template(r"tpl1612985718458.png", target_pos=4, record_pos=(-0.234, -0.155), resolution=(1440, 810)))
    # 等s以免出现网络波动
    sleep(5)
    wait(Template(r"tpl1612980931491.png", record_pos=(0.263, 0.214), resolution=(1440, 810)))
    touch(Template(r"tpl1612980931491.png", record_pos=(0.263, 0.214), resolution=(1440, 810)))
    # 等2s以免出现网络波动
    sleep(2)
    wait(Template(r"tpl1612984519435.png", record_pos=(-0.006, -0.037), resolution=(1440, 810)))
    touch(Template(r"tpl1612984551637.png", record_pos=(0.083, 0.107), resolution=(1440, 810)))
    sleep(2)


# 在地图上部署两个队伍
def select_two_team():
    airport_bottom_left()
    confirm_team()
    airport_top_left()
    confirm_team()


# 给左下角梯队规划炸狗路线
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
    sleep(3)


# 如果装备仓库满了，就回首页
def storehouse_full():
    if exists(Template(r"tpl1613035020293.png", record_pos=(0.0, -0.057), resolution=(1440, 810))):
        wait(Template(r"tpl1613035033982.png", record_pos=(0.128, 0.106), resolution=(1440, 810)))
        touch(Template(r"tpl1613035033982.png", record_pos=(0.128, 0.106), resolution=(1440, 810)))
        sleep(2)
        wait(Template(r"tpl1612973584765.png", target_pos=4, record_pos=(-0.369, -0.24), resolution=(1440, 810)))
        touch(Template(r"tpl1612973584765.png", target_pos=4, record_pos=(-0.369, -0.24), resolution=(1440, 810)))
        sleep(2)
        return True
    else:
        return False


# 拆解装备
def chai_zhuang_bei():
    # 首先先拆白色装备
    # 如果是在主页
    wait(Template(r"tpl1613035238319.png", record_pos=(0.399, -0.062), resolution=(1440, 810)))
    touch(Template(r"tpl1613035238319.png", record_pos=(0.399, -0.062), resolution=(1440, 810)))
    sleep(2)
    wait(Template(r"tpl1613035315767.png", record_pos=(-0.41, 0.048), resolution=(1440, 810)))
    touch(Template(r"tpl1613035315767.png", record_pos=(-0.41, 0.048), resolution=(1440, 810)))
    sleep(1)
    wait(Template(r"tpl1613035339578.png", record_pos=(-0.058, -0.119), resolution=(1440, 810)))
    
    touch(Template(r"tpl1613035339578.png", record_pos=(-0.058, -0.119), resolution=(1440, 810)))
    sleep(1)
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
    wait(Template(r"tpl1612973584765.png", target_pos=4, record_pos=(-0.369, -0.24), resolution=(1440, 810)))
    touch(Template(r"tpl1612973584765.png", target_pos=4, record_pos=(-0.369, -0.24), resolution=(1440, 810)))
    sleep(2)


# 遇到更换失败，显示弹药口粮耗尽遇敌必败
def no_food_restart():
    if exists(Template(r"tpl1613045862916.png", record_pos=(-0.046, -0.057), resolution=(1440, 810))):
        touch(Template(r"tpl1613045874272.png", record_pos=(-0.09, 0.106), resolution=(1440, 810)))
        return True
    else:
        return False


# 重新战斗
def restart():
    wait(Template(r"tpl1612983057440.png", record_pos=(-0.255, -0.242), resolution=(1440, 810)))
    touch(Template(r"tpl1612983057440.png", record_pos=(-0.255, -0.242), resolution=(1440, 810)))
    sleep(2)
    wait(Template(r"tpl1612983068454.png", record_pos=(-0.116, 0.105), resolution=(1440, 810)))
    touch(Template(r"tpl1612983068454.png", record_pos=(-0.116, 0.105), resolution=(1440, 810)))
    sleep(6)
    

# 收后勤任务
def houqin():
    if exists(Template(r"tpl1612894421046.png",record_pos=(-0.339, -0.077), resolution=(1440, 810))):
        # 假设4个小队全回来了
        for i in range(4):
            if exists(Template(r"tpl1612894421046.png",record_pos=(-0.339, -0.077), resolution=(1440, 810))):
                touch(Template(r"tpl1612894421046.png",record_pos=(-0.339, -0.077), resolution=(1440, 810)))
                sleep(3)
                if exists(Template(r"tpl1612894445416.png",record_pos=(0.001, -0.039), resolution=(1440, 810))):
                    touch(Template(r"tpl1612894456578.png", record_pos=(0.082, 0.105), resolution=(1440, 810)))
                sleep(5)
    sleep(5)


# 在游戏主界面进入8-1n
def main_in_81n():
	# 先判断有没有后勤归来的队伍
    if exists(Template(r"tpl1612894421046.png",record_pos=(-0.339, -0.077), resolution=(1440, 810))):
        for i in range(4):
            houqin()
    # 如果在游戏主界面
    if exists(Template(r"tpl1613054174818.png", record_pos=(0.245, 0.051), resolution=(1440, 810))):
        wait(Template(r"tpl1613054174818.png", record_pos=(0.245, 0.051), resolution=(1440, 810)))
        touch(Template(r"tpl1613054174818.png", record_pos=(0.245, 0.051), resolution=(1440, 810)))
        sleep(5)
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
        if exists(Template(r"tpl1613056147161.png", record_pos=(-0.122, -0.153), resolution=(1440, 810))):
            wait(Template(r"tpl1613056227863.png", record_pos=(0.449, -0.131), resolution=(1440, 810)))
            touch(Template(r"tpl1613056227863.png", record_pos=(0.449, -0.131), resolution=(1440, 810)))
            sleep(2)
            wait(Template(r"tpl1613061952109.png", record_pos=(0.0, -0.067), resolution=(1440, 810)))
            touch(Template(r"tpl1613061952109.png", record_pos=(0.0, -0.067), resolution=(1440, 810)))
            sleep(2)
            wait(Template(r"tpl1613056446830.png", record_pos=(0.278, 0.181), resolution=(1440, 810)))
            touch(Template(r"tpl1613056446830.png", record_pos=(0.278, 0.181), resolution=(1440, 810)))
            sleep(6)


# 缩放地图，换zas，布局下梯队，开始回合并将左上角梯队补给撤退
def map_plan():
    # 缩放地图复位
    scaling()
    # 更换打手
    change_zas()
    # 缩放地图复位
    scaling()
    # 部署两个梯队
    select_two_team()
    # 布局完成，确认开始回合
    start()
    sleep(2)
    # 给左上角队伍补给并撤退
    supply_and_retreat()


# 从主界面到炸狗一条龙
def start_bomb_dog(num):
    # 从主界面进入地图，如果在主界面就进8_1n地图，否则啥也不干
    main_in_81n()
    # 缩放地图，换zas，布局下梯队，开始回合并将左上角梯队补给撤退
    map_plan()
    # 计划模式给左下角梯队规划路线并确认执行
    plan_route()
    # 如果点击确认执行，遇到没有口粮弹药战斗必败的情况，那么就重开进地图重新部署
    if no_food_restart():
        restart()
        map_plan()
        plan_route()
    # 如果一切正常,点击执行按钮后没有其它问题弹窗，那么就等待150s
    sleep(150)
    # 如果战斗结束了(此时弹药刚好用完)
    if exists(Template(r"tpl1612983018269.png", record_pos=(0.049, 0.004), resolution=(1440, 810))):
        # 每15回合，拆一次装备
        if num % 15 == 0:
            # 此时还在地图上，先终止作战，回到首页
            end_fight()
            # 先等3s，加上end_fight的2s，共5s
            sleep(3)
            # 回到首页判断下有木有后勤完成归来的小队，收下后勤
            houqin()
            # 后勤收完还在首页，那就进工厂开始拆装备
            chai_zhuang_bei()
        else:
            # 如不是15的倍数，该干嘛干嘛
            # 重启地图
            restart()


# 循环炸狗
def loop_bomb_dog(num):
    for i in range(num):
        # 记录程序开始执行时间
        start_time = datetime.datetime.now()
        print("开始执行，当前次数 >> " + str(i+1) + " 时间 >> " + str(start_time))
        
        # 开始从主界面进入地图进行战斗
        start_bomb_dog(i+1)
        
        # 记录程序跑完一套后的时间
        end_time = datetime.datetime.now()
        print("执行完毕，当前次数 >> " + str(i+1) + " 时间 >> " + str(end_time))
        print("本次任务耗时 >> " + str((end_time - start_time).seconds) + " s")


# 说吧，你打算炸多少次？资源有限，量力而行哟，那就炸它个140次吧
loop_bomb_dog(140)














