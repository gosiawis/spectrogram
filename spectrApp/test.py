import time
from PyQt5 import QtWidgets
import sys
from PyQt5.QtWidgets import QApplication

from NewMainWindow import Ui_MainWindow


class App:

    def updatePlot(self):
        if time.time() - self.start_time > 2:
            item = self.ui.spectrogramGraph.getPlotItem()
            item.plot(y=self.ui.data, x=self.ui.times)
            self.start_time = time.time()
        self.ui.spectrogramGraph.setXRange(*self.ui.lr.getRegion(), padding=0)

    def updateRegion(self):
        pass

    def __init__(self, appWindow):
        self.start_time = 0.0
        self.ui = Ui_MainWindow()
        self.ui.setupUi(appWindow)
        self.ui.lr.sigRegionChanged.connect(self.updatePlot)
        self.ui.spectrogramGraph.sigXRangeChanged.connect(self.updateRegion)
        self.updatePlot()
        self.ui.openWav.clicked.connect(self.ui.handleOpenButton)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    init = App(window)
    window.show()
    sys.exit(app.exec_())
