from sys import platform, version_info
from asyncio import set_event_loop_policy, WindowsSelectorEventLoopPolicy

if platform == "win32" and version_info >= (3, 8, 0):
    set_event_loop_policy(WindowsSelectorEventLoopPolicy())

from FFxivPythonTrigger import *

Logger.print_log_level = Logger.DEBUG

try:
    register_module("SocketLogger")

    "core"
    register_modules([
        "HttpApi",
        "ChatLog",
        "XivMemory",
        "XivMagic",
        # "XivNetwork",
        "Command",
    ])

    "functions"
    "delete the '#' in front of each line to register as a default load plugin"
    register_modules([
        # "MoPlus",  # 鼠标功能增强
        # "ActorQuery",  # actor 查询
        # "Zoom2",  # 视距解限
        # "XivCombo",  # 连击绑定（一键系列）
        # "XivCraft",  # 生产规划器
        # "ACTLogLines",  # act接口
        # "SendKeys",  # 按键发送
        # "Markings",  # 标点功能
    ])
    start()
except Exception:
    pass
finally:
    close()
