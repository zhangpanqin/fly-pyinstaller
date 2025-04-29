from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox


class DemoWindow(QWidget):
    def __init__(self):
        super().__init__()

        # 设置窗口标题
        self.setWindowTitle('PyQt5 Demo')

        # 设置窗口大小
        self.setGeometry(100, 100, 300, 200)

        # 创建按钮并设置其属性
        self.button = QPushButton('点击我', self)
        self.button.setToolTip('这是一个按钮')
        self.button.resize(self.button.sizeHint())
        self.button.move(100, 80)

        # 连接按钮点击事件到槽函数
        self.button.clicked.connect(self.show_popup)

    def show_popup(self):
        """显示消息框"""
        QMessageBox.information(self, '信息', '你点击了按钮！',
                                QMessageBox.Ok, QMessageBox.Ok)
