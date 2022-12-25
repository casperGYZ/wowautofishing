# 声明：一切自动化都有封号风险，请自行斟酌后果。
# 本项目以学习为主

# 思路：

10.0之后版本钓鱼就不再需要必须右键点击鱼漂去抬杆了，可以通过按键来完成，因此我们判断的方式可以不再是图像检测而是声音检测。

每一次上钩的声音是并不相同的，最简单最基础的办法就是设置一个阈值，当超过阈值就自动收杆

灵感来自于大佬分享：
https://github.com/codingories/mywowfishing.git

# 准备工作：
## 安装：
python 3.7
audioop
pyautogui
cv2
mss
numpy
pyaudio

## 准备钓鱼宏

/console SoftTargetInteractArc 2
/console SoftTargetInteractRange 30

内置可用的指令调整可互动范围

设置钓鱼技能为 '['
设置与目标互动为 ']'
