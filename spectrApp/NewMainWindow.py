import pygame
from PyQt5 import QtCore, QtWidgets
from pyqtgraph import LinearRegionItem
from scipy.io import wavfile
import numpy as np
import pyqtgraph as pg


class Ui_MainWindow(object):
    def __init__(self):
        self.filePath = 'wavfiles/stereo_15bps.wav'
        self.data = [[]]
        self.times = None
        self.getDataForGraph()
        #self.amplitudeRangeGraph = pg.PlotWidget()
        self.amplitudeGraph = pg.PlotWidget()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1304, 607)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 60, 801, 501))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.widget = QtWidgets.QWidget(self.gridLayoutWidget)
        self.widget.setObjectName("widget")

        self.verticalLayoutWidget_1 = QtWidgets.QWidget(self.widget)
        self.verticalLayoutWidget_1.setGeometry(QtCore.QRect(39, 9, 751, 240))
        self.verticalLayoutWidget_1.setObjectName("verticalLayoutWidget_1")

        self.graphWidget = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_1)
        self.graphWidget.setContentsMargins(0, 0, 0, 0)
        self.graphWidget.setObjectName("graphWidget")
        self.graphWidget.addWidget(self.amplitudeGraph)

        # okno do wyboru fragmentu wykresu pionowo
        self.lr = pg.LinearRegionItem([0, self.times[-1]])
        self.lr.setZValue(-10)
        self.amplitudeGraph.addItem(self.lr)

        # okno do wyboru fragmentu wykresu poziomo
        #self.ud = pg.LinearRegionItem([0, 1], LinearRegionItem.Horizontal)
        #self.ud.setZValue(10)
        #self.amplitudeGraph.addItem(self.ud)

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.widget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(40, 260, 751, 240))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")

        self.amplitudeRangeWidget = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.amplitudeRangeWidget.setContentsMargins(0, 0, 0, 0)
        self.amplitudeRangeWidget.setObjectName("spectrogramWidget")
        self.amplitudeRangeWidget.addWidget(self.amplitudeGraph)
        self.gridLayout.addWidget(self.widget, 1, 0, 1, 1)

        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(810, 70, 481, 461))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")

        self.spectrogram = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.spectrogram.setContentsMargins(0, 0, 0, 0)
        self.spectrogram.setObjectName("spectrogram")

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(-1, 0, 801, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.openWav = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.openWav.setObjectName("openWav")
        self.horizontalLayout.addWidget(self.openWav)
        # self.openWav.clicked.connect(self.handleOpenButton)

        self.newWav = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.newWav.setObjectName("newWav")
        self.horizontalLayout.addWidget(self.newWav)

        self.newWav.raise_()
        self.openWav.raise_()

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1304, 22))

        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)

        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Spektrogram - Małgorzata Wiśniewska"))
        self.openWav.setText(_translate("MainWindow", "Otwórz plik .wav"))
        self.newWav.setText(_translate("MainWindow", "Stwórz nowy plik .wav"))

    def handleOpenButton(self):
        title = self.openWav.text()
        dialog = QtWidgets.QFileDialog()
        filename, _filter = dialog.getOpenFileNames(dialog, title, None, 'wav-files: *.wav')
        self.filePath = str(filename[0])
        self.getDataForGraph()
        #self.cleanGraphs()
        self.playWav()
        self.drawNewGraphs()

    def getDataForGraph(self):
        # obliczanie danych
        samplerate, self.data = wavfile.read(str(self.filePath))
        #print(samplerate)
        #print(self.data)
        sekundy = len(self.data) / float(samplerate)
        #print(sekundy)
        self.times = np.arange(len(self.data)) / float(samplerate)
        #print(self.times)

    def cleanGraphs(self):
        self.amplitudeGraph.close()
        #self.amplitudeRangeGraph.close()

    def drawNewGraphs(self):
        item1 = self.amplitudeGraph.getPlotItem()
        #item2 = self.amplitudeRangeGraph.getPlotItem()
        item1.close()
        #item2.close()
        item1.plot(y=self.data[:, 0], x=self.times)
        #item2.plot(y=self.data[:, 0], x=self.times)

    def playWav(self):
        pygame.init()
        pygame.mixer.music.load(str(self.filePath))
        pygame.mixer.music.play()
