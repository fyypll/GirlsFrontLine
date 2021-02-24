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
先保证一队中的zas空弹药，二队的满弹药，因为进入地图后会将一队的zas和二队的zas互换(不换也可以，脚本会帮忙补弹药换位的)
换完就开始部署梯队开打了

确保游戏处于主界面再运行本脚本，否则报错找不到位置
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
# swipe的第二张图、exists、assert_not_exists的全局隐式等待时间
# ST.FIND_TIMEOUT_TMP=20
start_time = 0
end_time = 0
count = 0


# 在地图上才进行缩放操作
def in_map_scaling():
    # 判断下，只在地图上才进行缩放
    if exists(Template(r"tpl1613990312943.png", record_pos=(-0.151, -0.244), resolution=(1440, 810))) and exists(Template(r"tpl1612972801554.png", record_pos=(
        0.387, 0.231), resolution=(1440, 810))):
        scaling()
    
    

# 缩放地图复位
def scaling():
    # 获取当前手机设备
    dev = device()
    # 向内捏合，捏两次保证缩到最小
    for i in range(2):
        dev.pinch(in_or_out='in', center=None, percent=0.5)
        sleep(1.5)
    # 向外捏合
    dev.pinch(in_or_out='out', center=None, percent=0.1)
    sleep(1)
    # 如果捏合的时候点出了重装页面，那么关闭并重新缩放地图
    if exists(Template(r"tpl1613063270994.png", record_pos=(-0.297, -0.212), resolution=(1440, 810))):
        touch(Template(r"tpl1613063307567.png", record_pos=(0.246, 0.224), resolution=(1440, 810)))
        sleep(2)
        scaling()


# 在战斗地图则终止战斗
def end_fight():
    wait(Template(r"tpl1612983057440.png", record_pos=(-0.255, -0.242), resolution=(1440, 810)))
    touch(Template(r"tpl1612983057440.png", record_pos=(-0.255, -0.242), resolution=(1440, 810)))
    wait(Template(r"tpl1613057829277.png", record_pos=(0.12, 0.104), resolution=(1440, 810)))
    touch(Template(r"tpl1613057829277.png", record_pos=(0.12, 0.104), resolution=(1440, 810)))


# 点击返回
def nav_back():
    if exists(Template(r"tpl1612973584765.png", target_pos=4, record_pos=(-0.369, -0.24), resolution=(1440, 810))):
        touch(Template(r"tpl1612973584765.png", target_pos=4, record_pos=(-0.369, -0.24), resolution=(1440, 810)))
        sleep(2)
        nav_back()
#     sleep(2)
#     keyevent("BACK")
#     sleep(2)
        


# 是否确认部署开始回合
def start_fight():
    # 如果按你还在那就是没有点击到，再点一次
    if exists(Template(r"tpl1612972801554.png", record_pos=(
        0.387, 0.231), resolution=(1440, 810))):
        touch(Template(r"tpl1612972801554.png", record_pos=(
        0.387, 0.231), resolution=(1440, 810)))
        # sleep(2)
        # 这里不能递归调用啦，因为弹出爆仓界面后还是能匹配到这个按钮的
        # 但是这时爆仓界面已经覆盖了按钮，按钮无法被点击，会造成循环点
        # start_fight()


# 点击左下角的机场
def click_airport_bottom_left():
    wait(Template(r"tpl1612978855358.png", target_pos=9, record_pos=(-0.389, 0.18), resolution=(1440, 810)))
    touch(Template(r"tpl1612978855358.png", target_pos=9, record_pos=(-0.389, 0.18), resolution=(1440, 810)))


# 点击左上角的机场
def click_airport_top_left():
    wait(Template(r"tpl1612978949744.png", target_pos=9, record_pos=(-0.319, -0.199), resolution=(1440, 810)))
    touch(Template(r"tpl1612978949744.png", target_pos=9, record_pos=(-0.319, -0.199), resolution=(1440, 810)))


# 确定部署梯队
def confirm_deployment():
    # 如果出现部署梯队界面
    if exists(Template(r"tpl1612973050340.png",
              record_pos=(-0.276, -0.206), resolution=(1440, 810))):
        touch(Template(r"tpl1612973088470.png", record_pos=(
    0.408, 0.216), resolution=(1440, 810)))


# 如果没有点击到导致不弹出部署队伍界面
def no_click_team():
    # 那就再次缩放地图
    scaling()
    # 再点一次左下角使其弹出部署队伍界面
    # 缩放界面会导致队伍取消选中状态，所以这里点两次
    click_airport_bottom_left()
    click_airport_bottom_left()


# 梯队编成中点击zas
def click_zas():
    if exists(Template(r"tpl1612973262610.png", record_pos=(-0.188, -0.237), resolution=(1440, 810))):
        wait(Template(r"tpl1612973337422.png", record_pos=(-0.158, -0.097), resolution=(1440, 810)))
        sleep(1)
        touch(Template(r"tpl1612973337422.png", record_pos=(-0.158, -0.097), resolution=(1440, 810)))
        sleep(2)
        click_zas()


# 点击军营中的zas
def click_barracks_zas():
    if exists(Template(r"tpl1612974573045.png", threshold=0.7, rgb=True, target_pos=8, record_pos=(-0.265, -0.176), resolution=(1440, 810))):
        touch(Template(r"tpl1612974573045.png", threshold=0.7, rgb=True, target_pos=8, record_pos=(-0.265, -0.176), resolution=(1440, 810)))
        sleep(2)
        click_barracks_zas()


# 更换zas
def replace_zas():
    # 首先点击左下角弹出部署队伍界面
    click_airport_bottom_left()
    sleep(2)
    
    wait(Template(r"tpl1612973222920.png", record_pos=(-0.301, 0.21), resolution=(1440, 810)),intervalfunc=no_click_team)
    sleep(1)
    touch(Template(r"tpl1612973222920.png", record_pos=(-0.301, 0.21), resolution=(1440, 810)))
    sleep(3)
    # 梯队编成中点击zas
    click_zas()
    wait(Template(r"tpl1612973383265.png", record_pos=(0.423, -0.147), resolution=(1440, 810)))
    touch(Template(r"tpl1612973383265.png", record_pos=(0.423, -0.147), resolution=(1440, 810)))
    sleep(1)
    wait(Template(r"tpl1612973435192.png", record_pos=(0.253, 0.174), resolution=(1440, 810)))
    touch(Template(r"tpl1612973435192.png", record_pos=(0.253, 0.174), resolution=(1440, 810)))
    sleep(1)
    # 点击军营中的zas
    click_barracks_zas()


# 补给梯队
def supply():
    if exists(Template(r"tpl1614082617655.png", target_pos=9, record_pos=(-0.277, -0.195), resolution=(1440, 810))):
        touch(Template(r"tpl1614082617655.png", target_pos=9, record_pos=(-0.277, -0.195), resolution=(1440, 810)))

        sleep(1)
    if exists(Template(r"tpl1614082617655.png", target_pos=9, record_pos=(-0.277, -0.195), resolution=(1440, 810))):
        touch(Template(r"tpl1614082617655.png", target_pos=9, record_pos=(-0.277, -0.195), resolution=(1440, 810)))
        sleep(1)
    if exists(Template(r"tpl1612980772706.png", record_pos=(0.438, 0.157), resolution=(1440, 810))):
        touch(Template(r"tpl1612980772706.png", record_pos=(0.438, 0.157), resolution=(1440, 810)))


# 撤退梯队
def retreat():
    if exists(Template(r"tpl1614082617655.png", target_pos=9, record_pos=(-0.277, -0.195), resolution=(1440, 810))) and exists(Template(r"tpl1613988823329.png", record_pos=(-0.202, -0.167), resolution=(1440, 810))):
        touch(Template(r"tpl1614082617655.png", target_pos=9, record_pos=(-0.277, -0.195), resolution=(1440, 810)))

        sleep(1)
    if exists(Template(r"tpl1612980931491.png", record_pos=(0.263, 0.214), resolution=(1440, 810))):
        touch(Template(r"tpl1612980931491.png", record_pos=(0.263, 0.214), resolution=(1440, 810)))
        sleep(1)
    if exists(Template(r"tpl1612984519435.png", record_pos=(-0.006, -0.037), resolution=(1440, 810))):
        touch(Template(r"tpl1612984551637.png", record_pos=(0.083, 0.107), resolution=(1440, 810)))


# 在地图上部署两个队伍
def deploy_two_team():
    click_airport_bottom_left()
    sleep(1)
    confirm_deployment()
    sleep(1)
    click_airport_top_left()
    sleep(1)
    confirm_deployment()


# 给左下角梯队规划炸狗路线
def plan_route():
    wait(Template(r"tpl1613989042459.png", record_pos=(-0.278, 0.178), resolution=(1440, 810)))
    touch(Template(r"tpl1613989042459.png", target_pos=4, record_pos=(-0.278, 0.178), resolution=(1440, 810)))
    sleep(1)
    touch(Template(r"tpl1612981328795.png", record_pos=(-0.44, 0.181), resolution=(1440, 810)))
    sleep(1)
    wait(Template(r"tpl1612981435916.png", target_pos=1, record_pos=(-0.215, 0.031), resolution=(1440, 810)))
    touch(Template(r"tpl1612981435916.png", target_pos=1, record_pos=(-0.215, 0.031), resolution=(1440, 810)))
    sleep(1)
    wait(Template(r"tpl1612984857140.png", target_pos=3, record_pos=(-0.288, 0.033), resolution=(1440, 810)))
    touch(Template(r"tpl1612984857140.png", target_pos=3, record_pos=(-0.288, 0.033), resolution=(1440, 810)))
    sleep(1)
    touch(Template(r"tpl1612981707528.png", record_pos=(0.426, 0.231), resolution=(1440, 810)))


# 如果装备仓库满了就点击装备强化按钮
def storehouse_full():
    if exists(Template(r"tpl1613035020293.png", record_pos=(0.0, -0.057), resolution=(1440, 810))):
        touch(Template(r"tpl1613035033982.png", record_pos=(0.128, 0.106), resolution=(1440, 810)))
        # sleep(2)
        # storehouse_full()

# 点击确认按钮
def comfirm_button():
    if exists(Template(r"tpl1613037938745.png", record_pos=(0.426, 0.224), resolution=(1440, 810))):
        touch(Template(r"tpl1613037938745.png", record_pos=(0.426, 0.224), resolution=(1440, 810)))
        sleep(2)
        comfirm_button()


# 拆解装备
def chai_zhuang_bei():
    # 首先先拆白色装备
    # 如果是在主页
    wait(Template(r"tpl1613995441235.png", record_pos=(0.403, -0.052), resolution=(1440, 810)))
    touch(Template(r"tpl1613995441235.png", record_pos=(0.403, -0.052), resolution=(1440, 810)))
    sleep(2)
    wait(Template(r"tpl1613035315767.png", record_pos=(-0.41, 0.048), resolution=(1440, 810)))
    touch(Template(r"tpl1613035315767.png", record_pos=(-0.41, 0.048), resolution=(1440, 810)))
    sleep(1)
    wait(Template(r"tpl1613995510960.png", record_pos=(-0.065, -0.126), resolution=(1440, 810)))
    touch(Template(r"tpl1613995510960.png", record_pos=(-0.065, -0.126), resolution=(1440, 810)))
    sleep(1)
    wait(Template(r"tpl1613037856497.png", record_pos=(0.426, 0.109), resolution=(1440, 810)))
    touch(Template(r"tpl1613037856497.png", record_pos=(0.426, 0.109), resolution=(1440, 810)))
    sleep(2)

    wait(Template(r"tpl1613037838594.png", record_pos=(0.425, 0.108), resolution=(1440, 810)))
    wait(Template(r"tpl1613037917903.png", record_pos=(0.422, 0.214), resolution=(1440, 810)))
    touch(Template(r"tpl1613037917903.png", record_pos=(0.422, 0.214), resolution=(1440, 810)))
    sleep(2)
    # 点击确认按钮
    comfirm_button()
    sleep(2)
    wait(Template(r"tpl1613037981165.png", record_pos=(0.334, -0.15), resolution=(1440, 810)))
    wait(Template(r"tpl1613037987997.png", record_pos=(0.386, 0.192), resolution=(1440, 810)))
    touch(Template(r"tpl1613037987997.png", record_pos=(0.386, 0.192), resolution=(1440, 810)))
    sleep(2)
    
    # 准备拆解蓝色装备
    wait(Template(r"tpl1613995510960.png", record_pos=(-0.065, -0.126), resolution=(1440, 810)))

    touch(Template(r"tpl1613995510960.png", record_pos=(-0.065, -0.126), resolution=(1440, 810)))
    # 预估为12件，都选中
    if exists(Template(r"tpl1613037838594.png", record_pos=(0.425, 0.108), resolution=(1440, 810))):
        for i in range(12):
            touch(Template(r"tpl1613052692777.png", record_pos=(-0.409, -0.186), resolution=(1440, 810)))
            sleep(0.2)
    # 点击确认按钮
    comfirm_button()
    sleep(2)
    wait(Template(r"tpl1613037981165.png", record_pos=(0.334, -0.15), resolution=(1440, 810)))
    wait(Template(r"tpl1613037987997.png", record_pos=(0.386, 0.192), resolution=(1440, 810)))
    touch(Template(r"tpl1613037987997.png", record_pos=(0.386, 0.192), resolution=(1440, 810)))
    sleep(1)
    if exists(Template(r"tpl1613104619512.png", record_pos=(0.031, -0.183), resolution=(1440, 810))):
        # 点击确认按钮
        comfirm_button()
        sleep(1)
    # 下面的代码大概...可能...也许...没机会运行了，但先不注释
    # 因为comfirm_button是检测到确定按钮就点击
    # 之所以这样做是因为有时候刚好网络波动会造成点击没生效，所以函数写成了确认按钮还存在就要点
    # 而上面步骤分解有高等级装备就会接着出现确认分解高等级按钮
    if exists(Template(r"tpl1613490589289.png", record_pos=(0.044, -0.178), resolution=(1440, 810))):
        # 点击确认按钮
        comfirm_button()


# 重新开启战斗
def restart():
    wait(Template(r"tpl1612983057440.png", record_pos=(-0.255, -0.242), resolution=(1440, 810)))
    touch(Template(r"tpl1612983057440.png", record_pos=(-0.255, -0.242), resolution=(1440, 810)))
    sleep(2)
    wait(Template(r"tpl1612983068454.png", record_pos=(-0.116, 0.105), resolution=(1440, 810)))
    touch(Template(r"tpl1612983068454.png", record_pos=(-0.116, 0.105), resolution=(1440, 810)))
    

# 收后勤任务
def houqin():
    if exists(Template(r"tpl1612894421046.png",record_pos=(-0.339, -0.077), resolution=(1440, 810))):
        touch(Template(r"tpl1612894421046.png",record_pos=(-0.339, -0.077), resolution=(1440, 810)))
        sleep(1)
        if exists(Template(r"tpl1612894445416.png",record_pos=(0.001, -0.039), resolution=(1440, 810))):
            touch(Template(r"tpl1612894456578.png", record_pos=(0.082, 0.105), resolution=(1440, 810)))
        # 等待一下，因为可能是多个后勤同时归来
        sleep(10)
        # 再检查还有木有后勤
        houqin()


# 关闭游戏并重开
def close_and_start():
    sleep(2)
    # 如果在战斗地图中，就终止作战
    if exists(Template(r"tpl1612983057440.png", record_pos=(-0.255, -0.242), resolution=(1440, 810))):
        # 终止战斗并返回主界面
        end_fight()
        sleep(10)
        nav_back()
        sleep(10)
        houqin()
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
    sleep(10)
    if exists(Template(r"tpl1613108634772.png", record_pos=(-0.297, -0.178), resolution=(1440, 810))):
        touch(Template(r"tpl1613108634772.png", record_pos=(-0.297, -0.178), resolution=(1440, 810)))
        sleep(10)
    if exists(Template(r"tpl1613318669960.png", record_pos=(-0.151, 0.09), resolution=(1440, 810))):
        touch(Template(r"tpl1613318669960.png", target_pos=4, record_pos=(-0.151, 0.09), resolution=(1440, 810)))
        sleep(2)
    if exists(Template(r"tpl1613318636018.png", record_pos=(-0.158, 0.09), resolution=(1440, 810))):
        touch(Template(r"tpl1613318647339.png", record_pos=(0.155, 0.089), resolution=(1440, 810)))
    # 点击后等待20s左右，大概就进入游戏主界面了
    sleep(20)
    if exists(Template(r"tpl1613318729048.png", record_pos=(-0.056, -0.099), resolution=(1440, 810))):
        touch(Template(r"tpl1613318781595.png", target_pos=2, record_pos=(-0.026, -0.157), resolution=(1440, 810)))
        sleep(10)
    # 关闭活动弹窗
    close_activity()
    sleep(5)
    # 返回首页
    click_back_activity()


# 点击返回按钮(即从活动界面返回)
def click_back_activity():
    if exists(Template(r"tpl1613318935294.png", record_pos=(-0.369, -0.25), resolution=(1440, 810))):
        touch(Template(r"tpl1613318935294.png", target_pos=4, record_pos=(-0.369, -0.25), resolution=(1440, 810)))
        sleep(10)
        click_back_activity()


# 关闭活动弹窗
def close_activity():
    if exists(Template(r"tpl1613318826969.png", record_pos=(0.412, -0.222), resolution=(1440, 810))):
        touch(Template(r"tpl1613318826969.png", record_pos=(0.412, -0.222), resolution=(1440, 810)))
        sleep(8)
        close_activity()

    
# 主界面点击战斗
def click_fight():
    # 如果找到了战斗图标
    if exists(Template(r"tpl1613054174818.png", record_pos=(0.245, 0.051), resolution=(1440, 810))):
        touch(Template(r"tpl1613054174818.png", record_pos=(0.245, 0.051), resolution=(1440, 810)))
        sleep(2)
        # 有时候网络刚好抽风，点了可能没效果，所以这里点击了再判断下
        click_fight()
    

# 选择并进入8_1n地图
def chose_81n_map():
    if exists(Template(r"tpl1613454816198.png", record_pos=(-0.409, -0.092), resolution=(1440, 810))):
        touch(Template(r"tpl1613454816198.png", record_pos=(-0.409, -0.092), resolution=(1440, 810)))
        sleep(1)
    if exists(Template(r"tpl1613054490281.png", record_pos=(-0.294, 0.024), resolution=(1440, 810))):
        # 获取当前手机设备
        dev = device()
        # 手指按照顺序依次滑过多个坐标,滑三次以保证滑到底
        for i in range(3):
            dev.swipe_along([[260, 644],[283, 286]])
        sleep(1)
        wait(Template(r"tpl1613055791912.png", record_pos=(-0.317, -0.199), resolution=(1440, 810)))
        touch(Template(r"tpl1613055791912.png", target_pos=8, record_pos=(-0.317, -0.199), resolution=(1440, 810)))
        sleep(1)
        touch([1363, 207])
        sleep(1)
        wait(Template(r"tpl1613061952109.png", record_pos=(0.0, -0.067), resolution=(1440, 810)))
        touch(Template(r"tpl1613061952109.png", record_pos=(0.0, -0.067), resolution=(1440, 810)))
        sleep(1)
        wait(Template(r"tpl1613056446830.png", record_pos=(0.278, 0.181), resolution=(1440, 810)))
        touch(Template(r"tpl1613056446830.png", record_pos=(0.278, 0.181), resolution=(1440, 810)))


# 缩放地图，换zas，布局下梯队
def map_plan():
    # 缩放地图复位
    in_map_scaling()
    # 更换打手
    replace_zas()
    nav_back()
    sleep(2)
    # 缩放地图复位
    in_map_scaling()
    # 部署两个梯队
    deploy_two_team()


# 仓库满了点击强化按钮，返回首页，进工厂拆装备，然后返回首页
def click_strengthen_chai_back():
    # 如果装备仓库满了就点击装备强化按钮
    storehouse_full()
    sleep(2)
    # 然后点击左上角返回按钮返回首页
    nav_back()
    sleep(2)
    houqin()
    sleep(5)
    # 拆装备
    chai_zhuang_bei()
    sleep(1)
    # 拆完装备就返回首页
    nav_back()
    sleep(6)
    houqin()


# 任务完成信息统计
def time_info(count):
    global start_time, end_time
    end_time = datetime.datetime.now()
    times = str((end_time - start_time).seconds)
    print("#==============第"+str(count)+"次任务信息=================")
    print("#")
    print("#    任务开始时间：" + str(start_time))
    print("#    任务结束时间：" + str(end_time))
    print("#    本次任务耗时：" + times + "秒")
    print("#")
    print("#========================================")


# 异常捕获，失败重跑(这是一个装饰器)
def retry(func):
    def run_case_again(*args, **keyargs):
        try:
            func(*args, **keyargs)
        except:
            close_and_start()
    return run_case_again


# 这里开始炸狗了
# 说吧，你打算炸多少次？资源有限，量力而行哟，那就炸它个140次吧
for i in range(140):
    # global count
    count = i+1
    # 记录程序开始执行时间
    start_time = datetime.datetime.now()
    # =======================================================================
    # sleep(5)
    # 如果遇到后勤队伍归来
    if exists(Template(r"tpl1612894421046.png",record_pos=(-0.339, -0.077), resolution=(1440, 810))):
        # 收后勤
        houqin()
    
    # 如果有战斗按钮，那就是游戏主界面
    if exists(Template(r"tpl1613054174818.png", record_pos=(0.245, 0.051), resolution=(1440, 810))):
        # 点击战斗进入选图
        touch(Template(r"tpl1613054174818.png", record_pos=(0.245, 0.051), resolution=(1440, 810)))
        # 大概4s后进入地图选择界面
        sleep(4)
        # 选择8-1n地图，进入
        chose_81n_map()
        sleep(2)
        # 判断下有木有弹出装备仓库爆仓弹窗
        if exists(Template(r"tpl1613035020293.png", record_pos=(0.0, -0.057), resolution=(1440, 810))):
            # 有就点击强化，返回首页，进工厂，分解，然后再返回首页
            click_strengthen_chai_back()
            # 打印任务时间信息
            time_info(count)
            # 然后结束本次循环，从头开始
            continue
    if exists(Template(r"tpl1613990312943.png", record_pos=(-0.151, -0.244), resolution=(1440, 810))) and exists(Template(r"tpl1612972801554.png", record_pos=(
        0.387, 0.231), resolution=(1440, 810))):
        # 缩放地图，换zas，布局下梯队
        map_plan()
        # 布局完成，点击开始作战
        start_fight()
        sleep(2)
        # 判断下有木有弹出装备仓库爆仓弹窗
        if exists(Template(r"tpl1613035020293.png", record_pos=(0.0, -0.057), resolution=(1440, 810))):
            # 有就点击强化，返回首页，进工厂，分解，然后再返回首页
            click_strengthen_chai_back()
            # 打印任务时间信息
            time_info(count)
            continue
        # 等几s等到左上角遮挡梯队的横条消失
        sleep(6)
        # 补给左上角梯队
        supply()
        sleep(1)
        # 补给完了就撤退
        retreat()
        sleep(1)
        # 点击计划模式，给左下角梯队规划路线并执行计划
        plan_route()
        sleep(2)
        # 如果遇到没有口粮弹药进击必败
        if exists(Template(r"tpl1614003508989.png", record_pos=(-0.048, -0.058), resolution=(1440, 810))):
            touch(Template(r"tpl1614003553801.png", record_pos=(-0.092, 0.106), resolution=(1440, 810)))
            sleep(1)
            restart()
            continue
        # 等待110s左右
        sleep(110)
        # 使用wait进行等待兼容，等到了就立马执行下一句
        # 因为100s明显是不够的，150s是最高，而时间是在两者间浮动的，也没法写死
        # 如果超时了还是没等到，多半是网络波动导致出问题了，重启下
        wait(Template(r"tpl1613989550759.png", record_pos=(0.046, 0.016), resolution=(1440, 810)), timeout=50)
        # 如果显示弹药耗尽那么就是打完了
        if exists(Template(r"tpl1613989550759.png", record_pos=(0.046, 0.016), resolution=(1440, 810))):
            # 每15回合，拆一次装备
            if (count) % 15 == 0:
                # 此时还在地图上，先终止作战回到选图页面
                end_fight()
                sleep(5)
                # 点击左上角返回按钮
                nav_back()
                sleep(5)
                # 回到首页判断下有木有后勤完成归来的小队，收下后勤
                houqin()
                # 后勤收完还在首页，进工厂开始拆装备
                chai_zhuang_bei()
                sleep(2)
                # 拆完返回首页
                nav_back()
                sleep(5)
                houqin()
            else:
                # 如不是15的倍数，重启地图
                restart()
                sleep(5)
                # 打印任务时间信息
                time_info(count)
                continue
    
    if exists(Template(r"tpl1612983057440.png", record_pos=(-0.255, -0.242), resolution=(1440, 810))) and exists(Template(r"tpl1613989550759.png", record_pos=(0.046, 0.016), resolution=(1440, 810))):
        restart()
        # 打印任务时间信息
        time_info(count)
        continue
        
    # 要是都不是上面的情况，那就重启游戏
    close_and_start()
    # 打印任务时间信息
    time_info(count)
    continue

