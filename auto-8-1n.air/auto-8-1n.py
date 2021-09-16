# -*- encoding=utf8 -*-
__author__ = "maple"

from airtest.core.api import *
from airtest.core.android.rotation import XYTransformer
from airtest.core.android.android import Android
from airtest.cli.parser import cli_setup
import datetime
import logging
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)

if not cli_setup():
    auto_setup(__file__, logdir=False, devices=[
        "Android://127.0.0.1:5037/127.0.0.1:7555",
    ])
# auto_setup(__file__)

# 设置隐式(默认)等待时长
# touch、wait、swipe的第一张图片识别时长，assert_exists、double_click的断言时长将受此影响
ST.FIND_TIMEOUT = 60
# swipe的第二张图、exists、assert_not_exists的全局隐式等待时间
# ST.FIND_TIMEOUT_TMP=20
start_time = 0
end_time = 0
count = 1


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
        sleep(2)
    # 向外捏合
    dev.pinch(in_or_out='out', center=None, percent=0.1)
    sleep(1)
    # 如果捏合的时候点出了重装页面，那么关闭并重新缩放地图
    if exists(Template(r"tpl1613063270994.png", record_pos=(-0.297, -0.212), resolution=(1440, 810))):
        touch(Template(r"tpl1613063307567.png", record_pos=(
            0.246, 0.224), resolution=(1440, 810)))
        sleep(2)
        scaling()


# 在战斗地图则终止战斗
def end_fight():
    touch(wait(Template(r"tpl1612983057440.png",
                        record_pos=(-0.255, -0.242), resolution=(1440, 810))))
    touch(wait(Template(r"tpl1613057829277.png", record_pos=(
        0.12, 0.104), resolution=(1440, 810))))


# 点击返回
def nav_back():
    if exists(Template(r"tpl1612973584765.png", target_pos=4, record_pos=(-0.369, -0.24), resolution=(1440, 810))):
        touch(Template(r"tpl1612973584765.png", target_pos=4,
                       record_pos=(-0.369, -0.24), resolution=(1440, 810)))
        sleep(2)
        nav_back()
        # keyevent("BACK")


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
    touch(Template(r"tpl1631786895621.png", target_pos=9, record_pos=(-0.383, 0.177), resolution=(1440, 810)))


# 点击左上角的机场
def click_airport_top_left():
    touch(Template(r"tpl1631786952292.png", target_pos=9, record_pos=(-0.306, -0.203), resolution=(1440, 810)))



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
        touch(wait(Template(r"tpl1614181809151.png",
                            record_pos=(-0.172, 0.133), resolution=(1440, 810))))
        sleep(2)
        click_zas()


# 点击仓库中的zas
def click_barracks_zas():
    if exists(Template(r"tpl1614181750397.png", record_pos=(-0.324, 0.001), resolution=(1440, 810))):
        touch(Template(r"tpl1614181750397.png",
                       record_pos=(-0.324, 0.001), resolution=(1440, 810)))
        sleep(2)
        click_barracks_zas()


# 更换zas
def replace_zas():
    # 首先点击左下角弹出部署队伍界面
    click_airport_bottom_left()
    sleep(2)
    wait(Template(r"tpl1612973222920.png", record_pos=(-0.301, 0.21),
                  resolution=(1440, 810)), intervalfunc=no_click_team)
    sleep(1)
    touch([278, 706])
    sleep(4)
    # 梯队编成中点击zas
    click_zas()
    touch([1320, 195])
    sleep(1)
    touch([1091, 653])
    sleep(1)
    # 点击仓库中的zas
    click_barracks_zas()


# 补给梯队
def supply():
    touch(Template(r"tpl1631786952292.png", target_pos=9, record_pos=(-0.306, -0.203), resolution=(1440, 810)))
    sleep(1)
    touch(Template(r"tpl1631786952292.png", target_pos=9, record_pos=(-0.306, -0.203), resolution=(1440, 810)))

    if exists(Template(r"tpl1612980772706.png", record_pos=(0.438, 0.157), resolution=(1440, 810))):
        touch(Template(r"tpl1612980772706.png", record_pos=(
            0.438, 0.157), resolution=(1440, 810)))


# 撤退梯队
def retreat():
    touch(Template(r"tpl1631786952292.png", target_pos=9, record_pos=(-0.306, -0.203), resolution=(1440, 810)))
    sleep(1)
    if exists(Template(r"tpl1612980931491.png", record_pos=(0.263, 0.214), resolution=(1440, 810))):
        touch(Template(r"tpl1612980931491.png", record_pos=(
            0.263, 0.214), resolution=(1440, 810)))
        sleep(1)
    if exists(Template(r"tpl1612984519435.png", record_pos=(-0.006, -0.037), resolution=(1440, 810))):
        touch(Template(r"tpl1612984551637.png", record_pos=(
            0.083, 0.107), resolution=(1440, 810)))


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
    touch(Template(r"tpl1631786895621.png", target_pos=9, record_pos=(-0.383, 0.177), resolution=(1440, 810)))
    sleep(1)
    touch(Template(r"tpl1612981328795.png",
                   record_pos=(-0.44, 0.181), resolution=(1440, 810)))
    sleep(1)
    touch(Template(r"tpl1631787632598.png", target_pos=7, record_pos=(-0.267, -0.037), resolution=(1440, 810)))
    sleep(1)
    touch(Template(r"tpl1631787712078.png", target_pos=3, record_pos=(-0.272, 0.056), resolution=(1440, 810)))
    sleep(1)
    touch(Template(r"tpl1612981707528.png", record_pos=(
        0.426, 0.231), resolution=(1440, 810)))

# 如果装备仓库满了就点击装备强化按钮


def storehouse_full():
    if exists(Template(r"tpl1613035020293.png", record_pos=(0.0, -0.057), resolution=(1440, 810))):
        touch(Template(r"tpl1613035033982.png", record_pos=(
            0.128, 0.106), resolution=(1440, 810)))
        # sleep(2)
        # storehouse_full()

# 点击确认按钮


def comfirm_button():
    if exists(Template(r"tpl1613037938745.png", record_pos=(0.426, 0.224), resolution=(1440, 810))):
        touch(Template(r"tpl1613037938745.png", record_pos=(
            0.426, 0.224), resolution=(1440, 810)))
        sleep(2)
        comfirm_button()


# 拆解装备
def chai_zhuang_bei():
    # 首先先拆白色装备
    # 如果是在主页
    touch(wait(Template(r"tpl1613995441235.png", record_pos=(
        0.403, -0.052), resolution=(1440, 810))))
    sleep(1)
    # 点击资源回收
    touch(wait(Template(r"tpl1631757600606.png",
                        record_pos=(-0.409, 0.047), resolution=(1440, 810))))
    sleep(1)
    # 点击选择装备
    touch([554, 232])
    sleep(2)
    # 如果是降序，就点击为升序
    if exists(Template(r"tpl1631755931733.png", record_pos=(0.394, 0.087), resolution=(1440, 810))):
        # 点击排序使其为升序
        touch([1330, 530])
        sleep(1)
    # 点击智能选择
    touch([1327, 716])
    sleep(1)
    # 点击确认按钮
    comfirm_button()
    sleep(1)
    touch(wait(Template(r"tpl1631515911098.png", record_pos=(
        0.386, 0.19), resolution=(1440, 810))))
    sleep(1)

    # 准备拆解蓝色装备
    touch([554, 232])
    # 预估为12件，都选中
    if exists(Template(r"tpl1613037838594.png", record_pos=(0.425, 0.108), resolution=(1440, 810))):
        for i in range(12):
            touch(Template(r"tpl1613052692777.png",
                           record_pos=(-0.409, -0.186), resolution=(1440, 810)))
            sleep(0.1)
    # 点击确认按钮
    comfirm_button()
    sleep(1)
    touch(wait(Template(r"tpl1631515911098.png", record_pos=(
        0.386, 0.19), resolution=(1440, 810))))
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
    touch(wait(Template(r"tpl1612983057440.png",
                        record_pos=(-0.255, -0.242), resolution=(1440, 810))))
    sleep(2)
    touch(wait(Template(r"tpl1612983068454.png",
                        record_pos=(-0.116, 0.105), resolution=(1440, 810))))


# 收后勤任务
def houqin():
    if exists(Template(r"tpl1612894421046.png", record_pos=(-0.339, -0.077), resolution=(1440, 810))):
        touch(Template(r"tpl1612894421046.png",
                       record_pos=(-0.339, -0.077), resolution=(1440, 810)))
        sleep(1)
        if exists(Template(r"tpl1612894445416.png", record_pos=(0.001, -0.039), resolution=(1440, 810))):
            touch(Template(r"tpl1612894456578.png", record_pos=(
                0.082, 0.105), resolution=(1440, 810)))
        # 等待一下，因为可能是多个后勤同时归来
        sleep(8)
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
    sleep(2)
    # 打开少女前线
    start_app('com.sunborn.girlsfrontline.cn')
    wait(Template(r"tpl1613108555413.png", record_pos=(
        0.001, 0.186), resolution=(1440, 810)))
    touch(Template(r"tpl1613108555413.png", record_pos=(
        0.001, 0.186), resolution=(1440, 810)))
    wait(Template(r"tpl1613108634772.png",
                  record_pos=(-0.297, -0.178), resolution=(1440, 810)))
    if exists(Template(r"tpl1613108634772.png", record_pos=(-0.297, -0.178), resolution=(1440, 810))):
        touch(Template(r"tpl1613108634772.png",
                       record_pos=(-0.297, -0.178), resolution=(1440, 810)))
        sleep(10)
    if exists(Template(r"tpl1613318669960.png", record_pos=(-0.151, 0.09), resolution=(1440, 810))):
        touch(Template(r"tpl1613318669960.png", target_pos=4,
                       record_pos=(-0.151, 0.09), resolution=(1440, 810)))
        sleep(2)
    if exists(Template(r"tpl1613318636018.png", record_pos=(-0.158, 0.09), resolution=(1440, 810))):
        touch(Template(r"tpl1613318647339.png", record_pos=(
            0.155, 0.089), resolution=(1440, 810)))
    sleep(10)
    if exists(Template(r"tpl1613054174818.png", record_pos=(0.245, 0.051), resolution=(1440, 810))):
        return 0
    else:
        # 点击后等待10s左右，大概就进入游戏主界面了
        sleep(10)
    if exists(Template(r"tpl1613318729048.png", record_pos=(-0.056, -0.099), resolution=(1440, 810))):
        touch(Template(r"tpl1613318781595.png", target_pos=2,
                       record_pos=(-0.026, -0.157), resolution=(1440, 810)))
        sleep(10)
    # 关闭活动弹窗
    close_activity()
    sleep(5)
    # 返回首页
    click_back_activity()
    print("重启任务完成!")


# 点击返回按钮(即从活动界面返回)
def click_back_activity():
    if exists(Template(r"tpl1613318935294.png", record_pos=(-0.369, -0.25), resolution=(1440, 810))):
        touch(Template(r"tpl1613318935294.png", target_pos=4,
                       record_pos=(-0.369, -0.25), resolution=(1440, 810)))
        sleep(2)
        click_back_activity()


# 关闭活动弹窗
def close_activity():
    if exists(Template(r"tpl1613318826969.png", record_pos=(0.412, -0.222), resolution=(1440, 810))):
        touch(Template(r"tpl1613318826969.png", record_pos=(
            0.412, -0.222), resolution=(1440, 810)))
        sleep(8)
        close_activity()


# 主界面点击战斗
def click_fight():
    # 如果找到了战斗图标
    if exists(Template(r"tpl1613054174818.png", record_pos=(0.245, 0.051), resolution=(1440, 810))):
        touch(Template(r"tpl1613054174818.png", record_pos=(
            0.245, 0.051), resolution=(1440, 810)))
        sleep(2)
        # 有时候网络刚好抽风，点了可能没效果，所以这里点击了再判断下
        click_fight()


# 选择并进入8_1n地图
def chose_81n_map():
    if exists(Template(r"tpl1613454816198.png", record_pos=(-0.409, -0.092), resolution=(1440, 810))):
        touch(Template(r"tpl1613454816198.png",
                       record_pos=(-0.409, -0.092), resolution=(1440, 810)))
        sleep(1)
    if exists(Template(r"tpl1631445475397.png", record_pos=(0.428, -0.185), resolution=(1440, 810))):
        # 获取当前手机设备
        dev = device()
        # 手指按照顺序依次滑过多个坐标,滑三次以保证滑到底
        for i in range(3):
            dev.swipe_along([[260, 644], [283, 286]])
        sleep(1)
        # 点击第八战役
        touch([282, 119])
        sleep(1)
        # 点击夜战
        touch([1363, 205])
        sleep(1)
        touch(wait(Template(r"tpl1613061952109.png", record_pos=(
            0.0, -0.067), resolution=(1440, 810))))
        sleep(1)
        touch(wait(Template(r"tpl1613056446830.png", record_pos=(
            0.278, 0.181), resolution=(1440, 810))))


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
    print("#=============================================")


# 异常捕获，失败重跑(这是一个装饰器)
def bomb_dog_retry(func):
    def run_case_again(*args, **keyargs):
        try:
            func(*args, **keyargs)
        except:
            close_and_start()
    return run_case_again


# 这里开始炸狗了，加上装饰器，失败重跑
@bomb_dog_retry
def bomb_dog():
    global count
    # 如果遇到后勤队伍归来
    if exists(Template(r"tpl1612894421046.png", record_pos=(-0.339, -0.077), resolution=(1440, 810))):
        # 收后勤
        houqin()

    # 如果有战斗按钮，那就是游戏主界面
    if exists(Template(r"tpl1613054174818.png", record_pos=(0.245, 0.051), resolution=(1440, 810))):
        # 点击战斗进入选图
        touch(Template(r"tpl1613054174818.png", record_pos=(
            0.245, 0.051), resolution=(1440, 810)))
        # 大概4s后进入地图选择界面
        sleep(4)
        # 选择8-1n地图，进入
        chose_81n_map()
        sleep(2)
        # 判断下有木有弹出装备仓库爆仓弹窗
        if exists(Template(r"tpl1613035020293.png", record_pos=(0.0, -0.057), resolution=(1440, 810))):
            # 有就点击强化，返回首页，进工厂，分解，然后再返回首页
            click_strengthen_chai_back()
            return 0

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
            return 0

        # 等几s等到左上角遮挡梯队的横条消失
        sleep(4)
        # 补给左上角梯队
        supply()
        sleep(2)
        # 补给完了就撤退
        retreat()
        sleep(1)
        # 如果炸狗队没有弹药则重开
        if exists(Template(r"tpl1631785478927.png", threshold=0.5, record_pos=(-0.131, 0.123), resolution=(1440, 810))):
            restart()
            return 0
        # 点击计划模式，给左下角梯队规划路线并执行计划
        plan_route()
        sleep(110)
        # 使用wait进行等待兼容，等到了就立马执行下一句
        wait(Template(r"tpl1631578586262.png", record_pos=(
            0.312, 0.236), resolution=(1440, 810)), timeout=50)

        # 如果行动点数为1那么就是打完了
        if exists(Template(r"tpl1631578586262.png", record_pos=(0.312, 0.236), resolution=(1440, 810))):
            # 每15回合拆一次装备(具体看你的装备仓库够几回合)
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
                nav_back()
                sleep(5)
                houqin()
                return 0
            else:
                sleep(1)
                # 如不是15的倍数，重启地图
                restart()
                sleep(5)
                return 0

    if exists(Template(r"tpl1612983057440.png", record_pos=(-0.255, -0.242), resolution=(1440, 810))) and exists(Template(r"tpl1631578586262.png", record_pos=(0.312, 0.236), resolution=(1440, 810))):
        sleep(1)
        restart()
        return 0

    # 若既不在主页，也不在地图页面，那就重启
    close_and_start()
    # 打印任务时间信息


# 循环炸狗
for i in range(1, 101):
    start_time = datetime.datetime.now()
    bomb_dog()
    time_info(i)
    count = i


# 炸狗任务完成后切换为收后勤
close_and_start()
while True:
    houqin()
    sleep(60)
