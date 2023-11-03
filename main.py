import sys
from PyQt5.QtWidgets import QApplication
from PriceHandler import MainWindow, RestAPI_dns

def start_interface():
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
    
def test_rest_dns():
    pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())