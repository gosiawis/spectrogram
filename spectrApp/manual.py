import time
from pom import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDial


class Apka:
    
    start_time: float
    start_time = time.time()

    def updatePlot(self):
        if time.time() - self.start_time > 2:
            item = self.ui.plot2.getPlotItem()
            item.plot(y=self.ui.data, x=self.ui.times)
            self.start_time = time.time()
        self.ui.plot2.setXRange(*self.ui.lr.getRegion(), padding=0)

    def updateRegion(self):
        pass

    # self.ui.lr.setRegion(self.ui.plot2.getViewBox().viewRange()[0])
    def __init__(self, window):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(window)
        self.ui.lr.sigRegionChanged.connect(self.updatePlot)
        self.ui.plot2.sigXRangeChanged.connect(self.updateRegion)
        self.updatePlot()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    inic = Apka(window)
    window.show()
    sys.exit(app.exec_())
