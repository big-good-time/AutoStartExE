from PySide6.QtWidgets import *
from PySide6.QtGui import Qt, QIntValidator
from model import Model

class View():
    def __init__(self, widget: QWidget, model: Model):
        self.mainWidget = widget
        self.model = model

    def setupUi(self):
        # 设置整体布局
        self.mainLayout = QVBoxLayout(self.mainWidget)

        self.scrollArea = QScrollArea(self.mainWidget)
        self.scrollArea.setWidgetResizable(True)

        self.container = QWidget()
        self.containerLayout = QVBoxLayout(self.container)

        self.setupTop()
        self.setupCenter()
        self.setupBottom()

        self.scrollArea.setWidget(self.container)

        self.mainLayout.addWidget(self.scrollArea)

        self.mainWidget.setLayout(self.mainLayout)
        
        

    def setupTop(self):
        """设置顶部控件"""
        topLayout = QHBoxLayout()

        self.waitTimeLabel = QLabel()
        self.waitTimeLabel.setText('前置时间')

        self.waitTimeLineEdit = QLineEdit()
        self.waitTimeLineEdit.setValidator(QIntValidator()) # 设置 QIntValidator，只允许输入整数
        
        self.spaceTimeLabel = QLabel()
        self.spaceTimeLabel.setText('启动间隔')

        self.spaceTimeLineEdit = QLineEdit()
        self.spaceTimeLineEdit.setValidator(QIntValidator())

        self.manualButton = QPushButton()
        self.manualButton.setText('手动开始')

        self.quitAutoButton = QPushButton()
        self.quitAutoButton.setText('退出自动')

        self.quitWaitButton = QPushButton()
        self.quitWaitButton.setText('跳出等待')

        topLayout.addWidget(self.waitTimeLabel)
        topLayout.addWidget(self.waitTimeLineEdit)
        topLayout.addWidget(self.spaceTimeLabel)
        topLayout.addWidget(self.spaceTimeLineEdit)
        topLayout.addWidget(self.manualButton)
        topLayout.addWidget(self.quitAutoButton)
        topLayout.addWidget(self.quitWaitButton)

        self.containerLayout.addLayout(topLayout)
    
    def setupCenter(self):
        """设置中间的启动列表"""
        layout = QVBoxLayout()
        for i in range(len(self.model.pathList)):
            path = self.model.pathList[i][0]
            note = self.model.pathList[i][1]
            flag = self.model.pathList[i][2]
            line = self.createPath(path, note, flag)
            layout.addLayout(line[-1])
        self.containerLayout.addLayout(layout)


    def createPath(self, path: str = '', note: str = '', flag: bool = False) -> list:
        """创建一行启动列表"""
        layout = QHBoxLayout()

        pathLineEdit = QLineEdit()
        pathLineEdit.setText(path)

        noteLineEdit = QLineEdit()
        noteLineEdit.setText(note)

        group = QButtonGroup()
        isCheck = QRadioButton()
        isCheck.setCheckable(flag)
        isCheck.setText('不检测')
        group.addButton(isCheck)

        startButton = QPushButton()
        startButton.setText('启动')

        layout.addWidget(pathLineEdit)
        layout.addWidget(noteLineEdit)
        layout.addWidget(isCheck)
        layout.addWidget(startButton)

        return [pathLineEdit, noteLineEdit, isCheck, layout]
    
    def setupBottom(self):
        layout = QHBoxLayout()

        createButton = QPushButton()
        createButton.setText('+')

        deleteButton = QPushButton()
        deleteButton.setText('-')

        layout.addWidget(createButton)
        layout.addWidget(deleteButton)

        self.containerLayout.addLayout(layout)


        
        
                