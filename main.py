from PyQt5.QtWidgets import *
import sys
import os
from PyQt5.QtCore import Qt


def on_tabWidget_currentChanged(index):
    """选项卡切换槽函数"""
    print("选项卡当前切换为：{}".format(str(index)))


class Menu(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(640, 360)
        self.setWindowTitle("智慧肝脏病理诊断系统V1.0")
        # self.setWindowFlags(Qt.FramelessWindowHint)
        # self.setAttribute(Qt.WA_TranslucentBackground)
        # self.close_pushButton.clicked.connect(self.close)
        # self.hidden_pushButton.clicked.connect(self.showMinimized)
        self.setStyleSheet("QLabel{\n"
                           "    text-align:right;\n"
                           "    font-family:\'Microsoft YaHei\';\n"
                           "    font-size:20px;\n"
                           "    font-weight:bold;\n"
                           "    }\n"
                           "\n"
                           ""
                           "QTextEdit{\n"
                           "    text-align:right;\n"
                           "    font-family:\'Microsoft YaHei\';\n"
                           "    font-size:18px;\n"
                           "    }\n"
                           "\n"
                           ""
                           )
        self.imagedirpath = ''
        self.imagefilepath = ''
        self.cdir = os.getcwd()

        # 全局布局
        wlayout = QVBoxLayout(self)

        self.tabwidget = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()

        self.inittab1()
        self.inittab2()
        self.inittab3()
        self.inittab4()

        self.tabwidget.setTabsClosable(False)
        self.tabwidget.setTabPosition(QTabWidget.North)
        self.tabwidget.addTab(self.tab1, "Crop")
        self.tabwidget.addTab(self.tab2, "Predict")
        self.tabwidget.addTab(self.tab3, "Stitch")
        self.tabwidget.addTab(self.tab4, "Show")

        self.tabwidget.setCurrentIndex(0)
        # 选择文件或文件夹路径布局

        self.tabwidget.currentChanged.connect(on_tabWidget_currentChanged)

        wlayout.addWidget(self.tabwidget)

        # 设置全局布局为主布局
        self.setLayout(wlayout)

    def inittab1(self):
        layout = QVBoxLayout()
        # label_choosefile = QLabel('请选择要处理的图片文件路径：')
        button_choosedir = QPushButton(self)
        button_choosedir.setText("选择文件夹")
        button_chooseimage = QPushButton(self)
        button_chooseimage.setText("选择文件")
        text_dir = QTextEdit()
        text_dir.setText(self.imagedirpath + self.imagefilepath)

        button_choosedir.clicked.connect(self.getfiles)
        button_chooseimage.clicked.connect(self.getfile)

        layout.addWidget(QTextEdit(
            '功能说明:\n打开病理图片并裁剪到指定路径，如待处理图片只有一张请点击-选择文件，如待处理图片不止一张请预先将所有图片放到一个单独的文件夹并点击-选择文件夹。'))
        # layout.addWidget(label_choosefile)
        button_layout = QHBoxLayout()
        button_layout.addWidget(button_choosedir, alignment=Qt.AlignVCenter | Qt.AlignCenter)
        button_layout.addWidget(button_chooseimage, alignment=Qt.AlignVCenter | Qt.AlignCenter)
        temp_ = QWidget()
        temp_.setLayout(button_layout)
        layout.addWidget(temp_)
        # layout.addWidget(text_dir)
        self.tab1.setLayout(layout)

    def inittab2(self):
        layout = QHBoxLayout()

        self.tab1.setLayout(layout)

    def inittab3(self):
        layout = QHBoxLayout()

        self.tab1.setLayout(layout)

    def inittab4(self):
        layout = QHBoxLayout()

        self.tab1.setLayout(layout)

    def getfiles(self):
        self.imagedirpath = QFileDialog.getExistingDirectory(self, "选取文件夹", self.cdir)
        if self.imagedirpath == "":
            print("\n取消选择")
            return
        print("\n你选择的文件夹为:")
        print(self.imagedirpath)

    def getfile(self):
        self.imagefilepath = QFileDialog.getOpenFileName(self, "选取文件", self.cdir)
        if self.imagefilepath == "":
            print("\n取消选择")
            return
        print("\n你选择的文件为:")
        print(self.imagefilepath)

    def crop(self):
        if self.imagedirpath != '':


if __name__ == '__main__':
    app = QApplication(sys.argv)
    menu = Menu()
    menu.show()
    sys.exit(app.exec_())
