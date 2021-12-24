#!/bin/bash - 
#===============================================================================
#
#          FILE: a.sh
# 
#         USAGE: ./a.sh 
# 
#   DESCRIPTION: 
# 
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: YOUR NAME (), 
#  ORGANIZATION: 
#       CREATED: 2021/12/23 14:14
#      REVISION:  ---
#===============================================================================

set -o nounset                              # Treat unset variables as an error


time=$(date "+%Y-%m-%d %H:%M:%S")
echo "当前开始时间:" $time

echo "解锁屏幕+++"
/usr/bin/adb shell input keyevent 224
sleep 3

/usr/bin/adb shell input swipe 350 1000 350 300
sleep 5

/usr/bin/adb shell am start -n com.tencent.wework/.launch.LaunchSplashActivity activity
sleep 20

# 进入工作台
echo "进入工作台+++"
/usr/bin/adb shell input tap 450 1225
sleep 5

# 点击打卡
echo "点击打卡+++"
/usr/bin/adb shell input tap 130 325
sleep 5

# 点击下班打卡
echo "点击下班打卡+++"
/usr/bin/adb shell input tap 350 830
sleep 5

# 点击下班打卡
echo "点击下班打卡+++"
/usr/bin/adb shell input tap 350 830
sleep 5

# 强制关闭
echo "强制关闭应用++"
/usr/bin/adb shell am force-stop com.tencent.wework
sleep 5

echo "锁屏+++"
/usr/bin/adb shell input keyevent 26

time=$(date "+%Y-%m-%d %H:%M:%S")
echo "当前结束时间:" $time
echo ""
echo ""

