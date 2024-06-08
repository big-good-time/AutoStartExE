from PySide6.QtWidgets import *
from PySide6.QtCore import QTimer
from model import Model
from functools import partial
import os
import platform

class ButtonClickedFunc():
    def __init__(self, model: Model, pathList: list):
        self.model = model
        self.timer = QTimer()
        self.runExE = RunExE()
        self.pathIndex = 0
        self.pathList = pathList
        print(self.pathList)
    
    def startButtonClicked(self, index):
        """启动按钮点击"""
        self.run(index)
    
    def breakWaitTime(self):
        """跳出等待，跳出时间等待"""
        self.timer.stop()
        self.run()
        self.autoStart()
        
    
    def quitAuto(self):
        """退出自动"""
        self.timer.stop()
    
    def manualButtonCliked(self):
        """手动开始"""
        self.autoStart()
    
    def run(self, index: int | None = None):
        if not index: index = self.pathIndex
        if index >= len(self.model.pathList): 
            self.timer.stop
        else:
            flag = self.runExE.run(self.model.pathList[index][0])
            
            
            if flag:
                self.pathList[index][0].setStyleSheet('background-color: #98FB98;')
            else:
                self.pathList[index][0].setStyleSheet('background-color: #FA8072;')
            self.pathIndex += 1
            return flag

    def autoStart(self):
        self.timer.stop()
        self.timer.timeout.disconnect()
        self.timer.timeout.connect(self.run)
        self.timer.start(self.model.spaceTime * 1000)
        
    def windowStart(self):
        self.timer.timeout.connect(self.autoStart)
        self.timer.start(self.model.waitTime * 1000 - self.model.spaceTime * 1000)

class DataSetFunc():
    def __init__(self, model: Model):
        self.model = model
    
    def waitTimeEdit(self, whatTime: str):
        """修改等待时间"""
        self.model.data['waitTime'] = int(whatTime)
        self.model.setData()
    
    def spaceTimeEdit(self, spaceTime: str):
        """修改间隔时间"""
        self.model.data['spaceTime'] = int(spaceTime)
        self.model.setData()
    
    def pathEdit(self, path: str, index: int):
        """修改文件地址"""
        self.model.data['pathList'][index][0] = path
        self.model.setData()
    
    def noteEdit(self, note: str, index: int):
        """修改备注信息"""
        self.model.data['pathList'][index][1] = note
        self.model.setData()
    
    def addPath(self):
        """添加一个空的 path"""
        self.model.data['pathList'].append(['', '', False])

class RunExE():

    def run(self, path):
        if platform.system() == 'windows': path = f"& '{path}'"
        if os.system(path):
            return False
        else:
            return True
        