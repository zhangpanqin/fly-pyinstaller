import sys
from pathlib import Path

import win32api
from PyQt5.QtWidgets import QApplication

from app.main import DemoWindow

if __name__ == '__main__':
    path_to_dat = Path(__file__).parent.resolve().joinpath("resource/py.txt")
    with open(path_to_dat, 'r', encoding='utf-8') as file:
        content = file.read()

    win32api.MessageBox(None, content, "标题", 0)
    app = QApplication(sys.argv)

    demo = DemoWindow()
    demo.show()

    # 执行应用程序的主循环
    sys.exit(app.exec_())