from PyQt5.QtWidgets import *
import sys
import os
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QTimer
import myutils
import time


def on_tabWidget_currentChanged(index):
    """选项卡切换槽函数"""
    print("选项卡当前切换为：{}".format(str(index)))


def exit_button():
    QApplication.quit()


class Menu(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(640, 360)
        font = QFont("Microsoft YaHei")
        self.setFont(font)
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
                           "QPushButton{\n"
                           "    font-family:\'Microsoft YaHei\';\n"
                           "    border-radius: 10px;\n"
                           "    border: none;\n"
                           "    background-color: white;\n"
                           "    color: black;\n"
                           "    font-size:17px;\n"
                           "    }\n"
                           "\n"
                           ""
                           "QPushButton:hover{\n"
                           "    background-color: #03f0fc;\n"
                           "    }\n"
                           "\n"
                           ""
                           "QMessageBox {\n"
                           "    border-radius: 10px;\n"
                           "    background-color: #f2f2f2;\n"
                           "    border: 1px solid #ccc;\n"
                           "    font-size: 16px;\n"
                           "    font-weight: bold;\n"
                           "    }\n"
                           "\n"
                           ""
                           "QWidget#centralwidget{\n"
                           "    background:white;\n"
                           "    border-radius:10px;\n"
                           "}\n"
                           "\n"
                           )
        self.imagedirpath = ''
        self.imagefilepath = ''
        self.cdir = os.getcwd()
        self.model_path = '/home/fengkh/桌面/workspace/python/smart_mvi/yolox/model_data/best_epoch_weights.pth'
        self.classes_path = '/home/fengkh/桌面/workspace/python/smart_mvi/yolox/dataset/mvi_classes.txt'

        # 全局布局
        wlayout = QVBoxLayout(self)

        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)

        self.tabwidget = QTabWidget()
        self.tabwidget.setStyleSheet("QTabBar::tab { color: #333; font-size: 16px; }")


        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()

        self.inittab1()
        self.inittab2()
        self.inittab3()
        self.inittab4()
        self.inittab5()

        self.tabwidget.setTabsClosable(False)
        self.tabwidget.setTabPosition(QTabWidget.North)
        self.tabwidget.addTab(self.tab1, "压缩")
        self.tabwidget.addTab(self.tab2, "裁剪")
        self.tabwidget.addTab(self.tab3, "预测")
        self.tabwidget.addTab(self.tab4, "拼接")
        self.tabwidget.addTab(self.tab5, "展示")

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
        button_choosedir.setFixedSize(100, 40)
        button_chooseimage = QPushButton(self)
        button_chooseimage.setFixedSize(100, 40)
        button_chooseimage.setText("选择文件")
        button_crop = QPushButton(self)
        button_crop.setFixedSize(100, 40)
        button_crop.setText("开始压缩")
        button_exit = QPushButton(self)
        button_exit.setFixedSize(100, 40)
        button_exit.setText("退出程序")

        text_dir = QTextEdit()
        text_dir.setText(self.imagedirpath + self.imagefilepath)

        button_choosedir.clicked.connect(self.getfiles)
        button_chooseimage.clicked.connect(self.getfile)
        button_crop.clicked.connect(self.compress)
        button_exit.clicked.connect(exit_button)

        text = QTextEdit(
            '功能说明: 打开病理图片并压缩到当前路径，如待处理图片只有一张请点击-选择文件，'
            '如待处理图片不止一张请预先将所有图片放到一个单独的文件夹并点击-选择文件夹。选择'
            '完成后点击压缩开始工作。')
        text.setReadOnly(True)
        text.setStyleSheet("QTextEdit { \
                                 background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\
                                                             stop: 0 #f6d365, stop: 0.5 #fda085, stop: 1 #f6d365); \
                                font-size: 18px; \
                             }")
        layout.addWidget(text)
        button_layout = QHBoxLayout()
        button_layout.addWidget(button_choosedir, alignment=Qt.AlignVCenter | Qt.AlignCenter)
        button_layout.addWidget(button_chooseimage, alignment=Qt.AlignVCenter | Qt.AlignCenter)
        button_layout.addWidget(button_crop, alignment=Qt.AlignVCenter | Qt.AlignCenter)
        button_layout.addWidget(button_exit, alignment=Qt.AlignVCenter | Qt.AlignCenter)

        temp_ = QWidget()
        temp_.setLayout(button_layout)
        layout.addWidget(temp_)
        # layout.addWidget(text_dir)
        self.tab1.setLayout(layout)

    def inittab2(self):
        layout = QVBoxLayout()
        # label_choosefile = QLabel('请选择要处理的图片文件路径：')
        button_choosedir = QPushButton(self)
        button_choosedir.setText("选择文件夹")
        button_choosedir.setFixedSize(100, 40)
        button_chooseimage = QPushButton(self)
        button_chooseimage.setText("选择文件")
        button_chooseimage.setFixedSize(100, 40)
        button_crop = QPushButton(self)
        button_crop.setText("开始裁剪")
        button_crop.setFixedSize(100, 40)
        button_exit = QPushButton(self)
        button_exit.setText("退出程序")
        button_exit.setFixedSize(100, 40)

        text_dir = QTextEdit()
        text_dir.setText(self.imagedirpath + self.imagefilepath)

        button_choosedir.clicked.connect(self.getfiles)
        button_chooseimage.clicked.connect(self.getfile)
        button_crop.clicked.connect(self.crop)
        button_exit.clicked.connect(exit_button)

        text = QTextEdit(
            '功能说明: 打开病理图片并裁剪到指定路径，如待处理图片只有一张请点击-选择文件，'
            '如待处理图片不止一张请预先将所有图片放到一个单独的文件夹并点击-选择文件夹。选择'
            '完成后点击裁剪开始工作。')
        text.setReadOnly(True)
        text.setStyleSheet("QTextEdit { \
                                         background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\
                                                                     stop: 0 #f6d365, stop: 0.5 #fda085, stop: 1 #f6d365); \
                                        font-size: 18px; \
                                     }")

        layout.addWidget(text)
        button_layout = QHBoxLayout()
        button_layout.addWidget(button_choosedir, alignment=Qt.AlignVCenter | Qt.AlignCenter)
        button_layout.addWidget(button_chooseimage, alignment=Qt.AlignVCenter | Qt.AlignCenter)
        button_layout.addWidget(button_crop, alignment=Qt.AlignVCenter | Qt.AlignCenter)
        button_layout.addWidget(button_exit, alignment=Qt.AlignVCenter | Qt.AlignCenter)

        temp_ = QWidget()
        temp_.setLayout(button_layout)
        layout.addWidget(temp_)
        # layout.addWidget(text_dir)
        self.tab2.setLayout(layout)

    def inittab3(self):
        layout = QVBoxLayout()
        # label_choosefile = QLabel('请选择要处理的图片文件路径：')

        button_choosedir = QPushButton(self)
        button_choosedir.setText("选择文件夹")
        button_choosedir.setFixedSize(100, 40)
        # button_choosemodel = QPushButton(self)
        # button_choosemodel.setText("选择模型")
        # button_setclass = QPushButton(self)
        # button_setclass.setText("选择类文件")
        button_predict = QPushButton(self)
        button_predict.setText("开始预测")
        button_predict.setFixedSize(100, 40)
        button_exit = QPushButton(self)
        button_exit.setText("退出程序")
        button_exit.setFixedSize(100, 40)
        text_dir = QTextEdit()
        text_dir.setText(self.imagedirpath + self.imagefilepath)

        button_choosedir.clicked.connect(self.getfiles)
        button_predict.clicked.connect(self.predict)
        # button_choosemodel.clicked.connect(self.getmodel)
        # button_setclass.clicked.connect(self.getclasses)
        button_exit.clicked.connect(exit_button)

        text = QTextEdit(
            '功能说明: 对裁剪好的小图片进行分别预测，请选择存放裁剪后的小图文件夹路径进行预测操作。')
        text.setReadOnly(True)
        text.setStyleSheet("QTextEdit { \
                                         background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\
                                                                     stop: 0 #f6d365, stop: 0.5 #fda085, stop: 1 #f6d365); \
                                        font-size: 18px; \
                                     }")

        layout.addWidget(text)
        button_layout = QHBoxLayout()
        button_layout.addWidget(button_choosedir, alignment=Qt.AlignVCenter | Qt.AlignCenter)
        # button_layout.addWidget(button_choosemodel, alignment=Qt.AlignVCenter | Qt.AlignCenter)
        # button_layout.addWidget(button_setclass, alignment=Qt.AlignVCenter | Qt.AlignCenter)
        button_layout.addWidget(button_predict, alignment=Qt.AlignVCenter | Qt.AlignCenter)
        button_layout.addWidget(button_exit, alignment=Qt.AlignVCenter | Qt.AlignCenter)

        temp_ = QWidget()
        temp_.setLayout(button_layout)
        layout.addWidget(temp_)
        # layout.addWidget(text_dir)
        self.tab3.setLayout(layout)

    def inittab4(self):
        layout = QVBoxLayout()
        # label_choosefile = QLabel('请选择要处理的图片文件路径：')
        button_choosedir = QPushButton(self)
        button_choosedir.setText("选择文件夹")
        button_choosedir.setFixedSize(100, 40)
        button_stitch = QPushButton(self)
        button_stitch.setText("开始拼接")
        button_stitch.setFixedSize(100, 40)
        button_exit = QPushButton(self)
        button_exit.setText("退出程序")
        button_exit.setFixedSize(100, 40)
        text_dir = QTextEdit()
        text_dir.setText(self.imagedirpath + self.imagefilepath)

        button_choosedir.clicked.connect(self.getfiles)
        button_stitch.clicked.connect(self.stitch)
        button_exit.clicked.connect(exit_button)

        text = QTextEdit(
            '功能说明: 将预测好的单张图片重新拼接成完成的图片，请选择存放预测结果图片的文件夹路径。')
        text.setReadOnly(True)
        text.setStyleSheet("QTextEdit { \
                                         background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\
                                                                     stop: 0 #f6d365, stop: 0.5 #fda085, stop: 1 #f6d365); \
                                        font-size: 18px; \
                                     }")

        layout.addWidget(text)
        button_layout = QHBoxLayout()
        button_layout.addWidget(button_choosedir, alignment=Qt.AlignVCenter | Qt.AlignCenter)
        button_layout.addWidget(button_stitch, alignment=Qt.AlignVCenter | Qt.AlignCenter)
        button_layout.addWidget(button_exit, alignment=Qt.AlignVCenter | Qt.AlignCenter)

        temp_ = QWidget()
        temp_.setLayout(button_layout)
        layout.addWidget(temp_)
        # layout.addWidget(text_dir)
        self.tab4.setLayout(layout)

    def inittab5(self):
        layout = QHBoxLayout()
        text = QTextEdit(
            '功能待定')
        text.setReadOnly(True)
        text.setStyleSheet("QTextEdit { \
                                         background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\
                                                                     stop: 0 #f6d365, stop: 0.5 #fda085, stop: 1 #f6d365); \
                                        font-size: 18px; \
                                     }")

        layout.addWidget(text)
        self.tab5.setLayout(layout)

    def getfiles(self):
        self.imagefilepath = ''
        self.imagedirpath = QFileDialog.getExistingDirectory(self, "选取文件夹", self.cdir)
        if self.imagedirpath == "":
            print("\n取消选择")
            return
        print("\n你选择的文件夹为:")
        print(self.imagedirpath)

    def getfile(self):
        self.imagedirpath = ''
        self.imagefilepath = QFileDialog.getOpenFileName(self, "选取文件", self.cdir)[0]
        if self.imagefilepath == "":
            print("\n取消选择")
            return
        print("\n你选择的文件为:")
        print(self.imagefilepath)

    def getmodel(self):
        self.model_path = ''
        self.model_path = QFileDialog.getOpenFileName(self, "选取文件", self.cdir)[0]
        if self.model_path == "":
            print("\n取消选择")
            return
        print("\n你选择的文件为:")
        print(self.model_path)

    def getclasses(self):
        self.classes_path = ''
        self.classes_path = QFileDialog.getOpenFileName(self, "选取文件", self.cdir)[0]
        if self.classes_path == "":
            print("\n取消选择")
            return
        print("\n你选择的文件为:")
        print(self.classes_path)

    def compress(self):
        compress_path = self.imagedirpath or self.imagefilepath
        try:
            runner_box = QMessageBox()
            runner_box.setText('程序正在运行中，请勿关闭')
            runner_box.setStyleSheet("QLabel{"
                                     "min-width: 200px;"
                                     "min-height: 50px;"
                                     # "align:center;"
                                     "}")
            runner_box.setWindowTitle("提示")
            # runner_box.setStandardButtons(QMessageBox.Ok)
            runner_box.show()
            time.sleep(2)
            myutils.compress(compress_path, 10, 10, self.cdir)
            runner_box.close()
        except ValueError:
            except_box = QMessageBox()
            except_box.setText('输入的路径错误，请重试')
            except_box.setStyleSheet("QLabel{"
                                     "min-width: 200px;"
                                     "min-height: 50px;"
                                     # "align:center;"
                                     "}")
            except_box.setWindowTitle("提示")
            # msg_box.setStyleSheet("QLabel{align:center;} QPushButton{margin-left:150px; margin-right:150px;}")
            except_box.setStandardButtons(QMessageBox.Ok)

            # 显示消息框
            except_box.show()

            # 设置定时器关闭消息框并显示文本
            timer = QTimer()
            timer.singleShot(3000, lambda: [except_box.close(), print("\n路径错误！")])  # 3秒后关闭并显示文本
            return
        except IOError:
            except_box = QMessageBox()
            except_box.setText('请确保路径中只有待处理的病理图片')
            except_box.setStyleSheet("QLabel{"
                                     "min-width: 300px;"
                                     "min-height: 50px;"
                                     # "align:center;"
                                     "}")
            except_box.setWindowTitle("提示")
            # msg_box.setStyleSheet("QLabel{align:center;} QPushButton{margin-left:150px; margin-right:150px;}")
            except_box.setStandardButtons(QMessageBox.Ok)

            # 显示消息框
            except_box.show()

            # 设置定时器关闭消息框并显示文本
            timer = QTimer()
            timer.singleShot(3000, lambda: [except_box.close(), print("\n图片错误！")])  # 3秒后关闭并显示文本
            return
        msg_box = QMessageBox()
        msg_box.setText('完成压缩，进入下一步')
        msg_box.setStyleSheet("QLabel{"
                              "min-width: 200px;"
                              "min-height: 50px;"
                              # "align:center;"
                              "}")
        msg_box.setWindowTitle("提示")
        # msg_box.setStyleSheet("QLabel{align:center;} QPushButton{margin-left:150px; margin-right:150px;}")
        msg_box.setStandardButtons(QMessageBox.Ok)

        # 显示消息框
        msg_box.show()

        # 设置定时器关闭消息框并显示文本
        timer = QTimer()
        timer.singleShot(3000, lambda: [msg_box.close(), print("\n压缩-执行完毕！")])  # 3秒后关闭并显示文本

    def crop(self):
        crop_path = self.imagedirpath or self.imagefilepath
        try:
            runner_box = QMessageBox()
            runner_box.setText('程序正在运行中，请勿关闭')
            runner_box.setStyleSheet("QLabel{"
                                     "min-width: 200px;"
                                     "min-height: 50px;"
                                     # "align:center;"
                                     "}")
            runner_box.setWindowTitle("提示")
            # runner_box.setStandardButtons(QMessageBox.Ok)
            runner_box.show()
            time.sleep(2)
            myutils.crop(crop_path, 1024, self.cdir)
            runner_box.close()
        except ValueError:
            except_box = QMessageBox()
            except_box.setText('输入的路径错误，请重试')
            except_box.setStyleSheet("QLabel{"
                                     "min-width: 200px;"
                                     "min-height: 50px;"
                                     # "align:center;"
                                     "}")
            except_box.setWindowTitle("提示")
            # msg_box.setStyleSheet("QLabel{align:center;} QPushButton{margin-left:150px; margin-right:150px;}")
            except_box.setStandardButtons(QMessageBox.Ok)

            # 显示消息框
            except_box.show()

            # 设置定时器关闭消息框并显示文本
            timer = QTimer()
            timer.singleShot(3000, lambda: [except_box.close(), print("\n路径错误！")])  # 3秒后关闭并显示文本
            return
        except IOError:
            except_box = QMessageBox()
            except_box.setText('请确保路径中只有待处理的病理图片')
            except_box.setStyleSheet("QLabel{"
                                     "min-width: 300px;"
                                     "min-height: 50px;"
                                     # "align:center;"
                                     "}")
            except_box.setWindowTitle("提示")
            # msg_box.setStyleSheet("QLabel{align:center;} QPushButton{margin-left:150px; margin-right:150px;}")
            except_box.setStandardButtons(QMessageBox.Ok)

            # 显示消息框
            except_box.show()

            # 设置定时器关闭消息框并显示文本
            timer = QTimer()
            timer.singleShot(3000, lambda: [except_box.close(), print("\n图片错误！")])  # 3秒后关闭并显示文本
            return
        msg_box = QMessageBox()
        msg_box.setText('完成裁剪，进入下一步')
        msg_box.setStyleSheet("QLabel{"
                              "min-width: 200px;"
                              "min-height: 50px;"
                              # "align:center;"
                              "}")
        msg_box.setWindowTitle("提示")
        # msg_box.setStyleSheet("QLabel{align:center;} QPushButton{margin-left:150px; margin-right:150px;}")
        msg_box.setStandardButtons(QMessageBox.Ok)

        # 显示消息框
        msg_box.show()

        # 设置定时器关闭消息框并显示文本
        timer = QTimer()
        timer.singleShot(3000, lambda: [msg_box.close(), print("\n裁剪-执行完毕！")])  # 3秒后关闭并显示文本

    def predict(self):
        predict_path = self.imagedirpath
        try:
            runner_box = QMessageBox()
            runner_box.setText('程序正在运行中，请勿关闭')
            runner_box.setStyleSheet("QLabel{"
                                     "min-width: 200px;"
                                     "min-height: 50px;"
                                     # "align:center;"
                                     "}")
            runner_box.setWindowTitle("提示")
            # runner_box.setStandardButtons(QMessageBox.Ok)
            runner_box.show()
            time.sleep(2)
            myutils.predict(predict_path, self.cdir)
            runner_box.close()
        except ValueError:
            except_box = QMessageBox()
            except_box.setText('输入的路径错误，请重试')
            except_box.setStyleSheet("QLabel{"
                                     "min-width: 200px;"
                                     "min-height: 50px;"
                                     # "align:center;"
                                     "}")
            except_box.setWindowTitle("提示")
            # msg_box.setStyleSheet("QLabel{align:center;} QPushButton{margin-left:150px; margin-right:150px;}")
            except_box.setStandardButtons(QMessageBox.Ok)

            # 显示消息框
            except_box.show()

            # 设置定时器关闭消息框并显示文本
            timer = QTimer()
            timer.singleShot(3000, lambda: [except_box.close(), print("\n路径错误！")])  # 3秒后关闭并显示文本
            return
        except IOError:
            except_box = QMessageBox()
            except_box.setText('请确保路径中只有待处理的病理图片')
            except_box.setStyleSheet("QLabel{"
                                     "min-width: 300px;"
                                     "min-height: 50px;"
                                     # "align:center;"
                                     "}")
            except_box.setWindowTitle("提示")
            # msg_box.setStyleSheet("QLabel{align:center;} QPushButton{margin-left:150px; margin-right:150px;}")
            except_box.setStandardButtons(QMessageBox.Ok)

            # 显示消息框
            except_box.show()

            # 设置定时器关闭消息框并显示文本
            timer = QTimer()
            timer.singleShot(3000, lambda: [except_box.close(), print("\n图片错误！")])  # 3秒后关闭并显示文本
            return
        msg_box = QMessageBox()
        msg_box.setText('完成预测，进入下一步')
        msg_box.setStyleSheet("QLabel{"
                              "min-width: 200px;"
                              "min-height: 50px;"
                              # "align:center;"
                              "}")
        msg_box.setWindowTitle("提示")
        # msg_box.setStyleSheet("QLabel{align:center;} QPushButton{margin-left:150px; margin-right:150px;}")
        msg_box.setStandardButtons(QMessageBox.Ok)

        # 显示消息框
        msg_box.show()

        # 设置定时器关闭消息框并显示文本
        timer = QTimer()
        timer.singleShot(3000, lambda: [msg_box.close(), print("\n预测-执行完毕！")])  # 3秒后关闭并显示文本

    def stitch(self):
        stitch_path = self.imagedirpath
        try:
            runner_box = QMessageBox()
            runner_box.setText('程序正在运行中，请勿关闭')
            runner_box.setStyleSheet("QLabel{"
                                     "min-width: 200px;"
                                     "min-height: 50px;"
                                     # "align:center;"
                                     "}")
            runner_box.setWindowTitle("提示")
            runner_box.setStandardButtons(QMessageBox.Ok)
            runner_box.show()
            time.sleep(2)
            myutils.stitch(stitch_path, self.cdir)
            runner_box.close()
        except ValueError:
            except_box = QMessageBox()
            except_box.setText('输入的路径错误，请重试')
            except_box.setStyleSheet("QLabel{"
                                     "min-width: 200px;"
                                     "min-height: 50px;"
                                     # "align:center;"
                                     "}")
            except_box.setWindowTitle("提示")
            # msg_box.setStyleSheet("QLabel{align:center;} QPushButton{margin-left:150px; margin-right:150px;}")
            except_box.setStandardButtons(QMessageBox.Ok)

            # 显示消息框
            except_box.show()

            # 设置定时器关闭消息框并显示文本
            timer = QTimer()
            timer.singleShot(3000, lambda: [except_box.close(), print("\n路径错误！")])  # 3秒后关闭并显示文本
            return
        except IOError:
            except_box = QMessageBox()
            except_box.setText('请确保路径中只有待处理的病理图片')
            except_box.setStyleSheet("QLabel{"
                                     "min-width: 300px;"
                                     "min-height: 50px;"
                                     # "align:center;"
                                     "}")
            except_box.setWindowTitle("提示")
            # msg_box.setStyleSheet("QLabel{align:center;} QPushButton{margin-left:150px; margin-right:150px;}")
            # except_box.setStandardButtons(QMessageBox.Ok)

            # 显示消息框
            except_box.show()

            # 设置定时器关闭消息框并显示文本
            timer = QTimer()
            timer.singleShot(3000, lambda: [except_box.close(), print("\n图片错误！")])  # 3秒后关闭并显示文本
            return
        msg_box = QMessageBox()
        msg_box.setText('完成拼接，进入下一步')
        msg_box.setStyleSheet("QLabel{"
                              "min-width: 200px;"
                              "min-height: 50px;"
                              # "align:center;"
                              "}")
        msg_box.setWindowTitle("提示")
        # msg_box.setStyleSheet("QLabel{align:center;} QPushButton{margin-left:150px; margin-right:150px;}")
        msg_box.setStandardButtons(QMessageBox.Ok)

        # 显示消息框
        msg_box.show()

        # 设置定时器关闭消息框并显示文本
        timer = QTimer()
        timer.singleShot(3000, lambda: [msg_box.close(), print("\n拼接-执行完毕！")])  # 3秒后关闭并显示文本


if __name__ == '__main__':
    app = QApplication(sys.argv)
    menu = Menu()
    menu.show()
    sys.exit(app.exec_())
