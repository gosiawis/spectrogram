import pyqtgraph as pg
from scipy.io import wavfile
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def __init__(self):
        self.times = None
        self.data = None

    def setupUi(self, MainWindow):
        # obliczanie danych
        samplerate, data = wavfile.read("wavfiles//bzyk.wav")
        sekundy = len(data) / float(samplerate)
        print(sekundy)
        times = np.arange(len(data)) / float(samplerate)

        # narysowanie dwoch wykresow
        self.plot = pg.PlotWidget(y=data[:, 0], x=times)
        self.plot2 = pg.PlotWidget(y=data[:, 0], x=times)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.gridLayout.addWidget(self.plot, 0, 0, 1, 1)

        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout.addWidget(self.plot2, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))

        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # dodanie tych paskow do wybierania przedzialu
        self.lr = pg.LinearRegionItem([0, times[-1]])
        self.lr.setZValue(-10)
        self.plot.addItem(self.lr)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
