from PyQt5.QtWidgets import *
import sys
import os
import PyQt5.QtCore as Qt


class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(1000, 600)
        self.setWindowTitle("智慧肝脏病理诊断系统V1.0")

        self.imagedirpath = ''
        self.imagefilepath = ''

        self.label_choosefile = QLabel('请选择要处理的图片文件路径：')
        self.button_choosedir = QPushButton(self)
        self.button_choosedir.setObjectName("button_choosefile")
        self.button_choosedir.setText("选择文件夹")
        self.button_chooseimage = QPushButton(self)
        self.button_chooseimage.setObjectName("button_chooseimage")
        self.button_chooseimage.setText("选择文件")
        self.cdir = os.getcwd()

        self.button_choosedir.clicked.connect(self.getfiles)
        self.button_chooseimage.clicked.connect(self.getfile)

        # 全局布局
        # wlayout = QVBoxLayout(self)

        # 选择文件或文件夹路径布局
        layout_selectfile = QVBoxLayout()
        layout_selectfile.addWidget(self.label_choosefile)
        layout_selectfile.addWidget(self.button_choosedir)
        layout_selectfile.addWidget(self.button_chooseimage)

        # widget_selectfile = QWidget()
        # widget_selectfile.setLayout(layout_selectfile)
        #
        # wlayout.addWidget(widget_selectfile)

        # 设置全局布局为主布局
        self.setLayout(layout_selectfile)

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
        print("\n你选择的文件夹为:")
        print(self.imagefilepath)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    menu = Menu()
    menu.show()
    sys.exit(app.exec_())
