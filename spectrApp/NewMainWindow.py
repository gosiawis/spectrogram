from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QSlider
from scipy.io import wavfile
import numpy as np
import pyqtgraph as pg


class Ui_MainWindow(object):
    def __init__(self):
        self.times = None
        self.data = None
        self.filePath = None

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

        # obliczanie danych
        samplerate, data = wavfile.read("wavfiles//bzyk.wav")
        print(samplerate)
        print(data)
        sekundy = len(data) / float(samplerate)
        print(sekundy)
        times = np.arange(len(data)) / float(samplerate)
        print(times)

        # narysowanie dwoch wykresow
        self.amplitudeGraph = pg.PlotWidget(y=data[:, 0], x=times)
        self.spectrogramGraph = pg.PlotWidget(y=data[:, 0], x=times)

        self.verticalLayoutWidget_1 = QtWidgets.QWidget(self.widget)
        self.verticalLayoutWidget_1.setGeometry(QtCore.QRect(39, 9, 751, 240))
        self.verticalLayoutWidget_1.setObjectName("verticalLayoutWidget_1")

        self.graphWidget = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_1)
        self.graphWidget.setContentsMargins(0, 0, 0, 0)
        self.graphWidget.setObjectName("graphWidget")
        self.graphWidget.addWidget(self.amplitudeGraph)

        # okno do wyboru fragmentu wykresu
        self.lr = pg.LinearRegionItem([0, times[-1]])
        self.lr.setZValue(-10)
        self.amplitudeGraph.addItem(self.lr)

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.widget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(40, 260, 751, 240))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")

        self.spectrogramWidget = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.spectrogramWidget.setContentsMargins(0, 0, 0, 0)
        self.spectrogramWidget.setObjectName("spectrogramWidget")
        self.spectrogramWidget.addWidget(self.spectrogramGraph)
        self.gridLayout.addWidget(self.widget, 1, 0, 1, 1)

        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(810, 70, 481, 461))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")

        self.spectrogram = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.spectrogram.setContentsMargins(0, 0, 0, 0)
        self.spectrogram.setObjectName("spectrogram")

        # przesuwanie po osi X
        # self.OXSlider = QtWidgets.QSlider(self.widget)
        # self.OXSlider.setGeometry(QtCore.QRect(40, 230, 751, 22))
        # self.OXSlider.setOrientation(QtCore.Qt.Horizontal)
        # self.OXSlider.setObjectName("OXSlider")
        # self.OXSlider.setMinimum(1)
        # self.OXSlider.setMaximum(99)
        # self.OXSlider.setValue(25)
        # self.OXSlider.setTickInterval(10)
        # self.OXSlider.setTickPosition(QSlider.TicksAbove)

        ## przesuwanie po osi X
        # self.OYSlider = QtWidgets.QSlider(self.widget)
        # self.OYSlider.setGeometry(QtCore.QRect(10, 10, 22, 211))
        # self.OYSlider.setOrientation(QtCore.Qt.Vertical)
        # self.OYSlider.setObjectName("OYSlider")

        self.gridLayout.addWidget(self.widget, 1, 0, 1, 1)

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
        # self.OXSlider.raise_()
        # self.OYSlider.raise_()

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
        file_list = dialog.getOpenFileNames(dialog, title, None, 'wav-files: *.wav')
        self.filePath = str(file_list[0])
        print(self.filePath)
        self.getData()

    def getData(self):
        # obliczanie danych
        samplerate, data = wavfile.read('C:/Users/malgo/Desktop/STUDIA/sem_5/sygnały/spectrogram/spectrApp/wavfiles/baran.wav')
        print(samplerate)
        print(data)
        sekundy = len(data) / float(samplerate)
        print(sekundy)
        times = np.arange(len(data)) / float(samplerate)
        print(times)
        
