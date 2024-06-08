from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QLineEdit, QRadioButton, QHBoxLayout, QVBoxLayout
from functools import partial
from controller import DataSetFunc, ButtonClickedFunc

class Ui():
    
    def setUi(self, widget, model):
        self.pathList = []
        self.model = model

        self.dataSetFunc = DataSetFunc(self.model)
        self.buttonFunc = ButtonClickedFunc(self.model, self.pathList)
        self.mainLayout = QVBoxLayout()
        widget.setLayout(self.mainLayout)

        titleLayout = QHBoxLayout()
        self.label1 = QLabel()
        self.label1.setText('前置时间')
        self.label2 = QLabel()
        self.label2.setText('启动间隔')

        self.waitTimeLineEdit = QLineEdit()
        self.waitTimeLineEdit.setText(str(self.model.waitTime))
        self.waitTimeLineEdit.textChanged.connect(self.dataSetFunc.waitTimeEdit)

        self.spaceTime = QLineEdit()
        self.spaceTime.setText(str(self.model.spaceTime))
        self.spaceTime.textChanged.connect(self.dataSetFunc.spaceTimeEdit)

        self.manualStart = QPushButton()
        self.manualStart.setText('手动开始')
        self.manualStart.clicked.connect(self.buttonFunc.manualButtonCliked)
        self.quitAuto = QPushButton()
        self.quitAuto.setText('退出自动')
        self.quitAuto.clicked.connect(self.buttonFunc.quitAuto)
        self.breakWaitTime = QPushButton()
        self.breakWaitTime.setText('跳出等待')
        self.breakWaitTime.clicked.connect(self.buttonFunc.breakWaitTime)

        titleLayout.addWidget(self.label1)
        titleLayout.addWidget(self.waitTimeLineEdit)
        titleLayout.addWidget(self.label2)
        titleLayout.addWidget(self.spaceTime)
        titleLayout.addWidget(self.manualStart)
        titleLayout.addWidget(self.quitAuto)
        titleLayout.addWidget(self.breakWaitTime)

        self.mainLayout.addLayout(titleLayout)
        
        self.pathListLayout = QVBoxLayout()
        self.setPathList()
        self.mainLayout.addLayout(self.pathListLayout)

        self.addPushButton = QPushButton()
        self.addPushButton.setText('+')
        self.addPushButton.clicked.connect(partial(self.addPath, '', '', False, len(self.pathList), True))
        self.mainLayout.addWidget(self.addPushButton)

        self.buttonFunc.pathList = self.pathList
        self.buttonFunc.windowStart()
    
    def setPathList(self):
        
        for i in range(len(self.model.pathList)):
            path = self.model.pathList[i]
            self.pathList.append(self.addPath(path[0], path[1], path[2], i, False))
        
    def addPath(self, path: str = '', note: str = '', checked: bool = False, index: int = 0, newData: bool = False) -> list:
        if newData:
            self.dataSetFunc.addPath()
        lineLayout = QHBoxLayout()
        pathLineEdit = QLineEdit()
        pathLineEdit.setText(path)
        pathLineEdit.textChanged.connect(partial(self.dataSetFunc.pathEdit, index = index))
        noteLineEdit = QLineEdit()
        noteLineEdit.setText(note)
        noteLineEdit.textChanged.connect(partial(self.dataSetFunc.noteEdit, index = index))
        checkRadioButton = QRadioButton()
        checkRadioButton.setText('不检测')
        checkRadioButton.setChecked(checked)
        startButton = QPushButton()
        startButton.setText('启动')
        startButton.clicked.connect(partial(self.buttonFunc.startButtonClicked, index))
        lineLayout.addWidget(pathLineEdit)
        lineLayout.addWidget(noteLineEdit)
        lineLayout.addWidget(checkRadioButton)
        lineLayout.addWidget(startButton)
        self.pathListLayout.addLayout(lineLayout)
        
        return [pathLineEdit, noteLineEdit, checkRadioButton]

    

    

    


