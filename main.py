import sys
from PyQt5.QtWidgets import QApplication
from PriceHandler import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())