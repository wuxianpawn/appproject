"""
subprocess.call()
os.system(命令行命令) 也可以执行run。py文件，但是不能收集返回值，只是运行命令 启动服务就可以了
"""
import os
os.system('adb logcat')