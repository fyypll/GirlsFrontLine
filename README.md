# GirlsFrontLine

#### 介绍
少女前线8-1n双zas炸狗与收后勤脚本

#### 1.炸狗脚本使用说明
本脚本基于airtest编写
使用的MuMu模拟器，分辨率1440*810

1.队伍配置
第一队放老板和zas
第二队单独一个zas

注意两个zas都需要满足条件，具体数值要求可到nga或者贴吧查找

2.注意点
让一队的zas和二队的zas先磨一点血，以保证在仓库中的受损排序是第一和第二位
先保证一队中的zas空弹药，二队的满弹药，因为进入地图后会将一队的zas和二队的zas互换(不换也可以，脚本会帮忙补弹药换位的)
换完就开始部署梯队开打了

~~确保游戏处于主界面再运行本脚本，否则会报错找不到位置~~

若游戏不在主界面，则会重启

### 其它问题
目前运行比较正常，脚本中部分功能没有写完因此没有调用

功能对目前的我来说是够用了，如无问题不会再改了(我懒...)

请使用v4版本，该版本优化了逻辑，炸一次狗的速度也更快，不再是动不动就300多s了(启动脚本的第一把除外)，目前过一遍炸狗流程平均在250s左右，为了稳定有些等待时间是不能删的，实在不知道别的大佬是怎么实现200s一局的

注释写的比较详细，有兴趣且有能力的可以自己修改以符合自身的需求



### 2.收后勤脚本使用说明

游戏保持在主界面，然后运行脚本即可。脚本每分钟会判断一次后勤队伍是否归来，脚本检测到后勤归来，收了奖励后会自动重新派遣。



### 注意

如果有些图片识别不出来，可能需要你重新截图，同一个脚本同样的代码同样的一张图。不同的airtest版本识别会有差别，总之没问题就不管，有报错识别不了就看看是不是。

如果脚本莫名其妙不停的重启游戏应用，多半就是有问题的，注释掉第 `453行` 的 `@bomb_dog_retry` 装饰器再调试，因为该装饰器是用来捕获异常的，脚本出错不会终止运行，而是会重启游戏重跑脚本。

要调试看报错就注释掉装饰器准没问题。确认脚本没问题了再取消注释即可。



代码写的比较垃圾，大神勿喷。