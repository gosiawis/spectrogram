import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from scipy.io import wavfile
from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg


class Ui_MainWindow(object):
    def __init__(self):
        self.times = None
        self.data = None
        self.filePath = None

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

        self.openWav = QtWidgets.QPushButton(self.centralwidget)
        #self.openWav.setGeometry(QtCore.QRect(10, 10, 171, 51))
        self.openWav.setObjectName("openWav")
        self.gridLayout.addWidget(self.openWav, 1, 0.5)
        self.openWav.clicked.connect(self.handleOpenButton)

        self.newWav = QtWidgets.QPushButton(self.centralwidget)
        #self.newWav.setGeometry(QtCore.QRect(184, 10, 191, 51))
        self.gridLayout.addWidget(self.newWav, 0, 0.5)
        self.newWav.setObjectName("newWav")

        self.OXSlider = QtWidgets.QSlider(self.centralwidget)
        #self.OXSlider.setGeometry(QtCore.QRect(40, 260, 741, 22))
        self.gridLayout.addWidget(self.OXSlider)
        self.OXSlider.setOrientation(QtCore.Qt.Horizontal)
        self.OXSlider.setObjectName("OXSlider")

        self.OYSlider = QtWidgets.QSlider(self.centralwidget)
        #self.OYSlider.setGeometry(QtCore.QRect(10, 70, 22, 181))
        self.gridLayout.addWidget(self.OYSlider)
        self.OYSlider.setOrientation(QtCore.Qt.Vertical)
        self.OYSlider.setObjectName("OYSlider")

        self.title = QtWidgets.QWidget(self.centralwidget)
        #self.title.setGeometry(QtCore.QRect(379, 9, 381, 51))
        self.gridLayout.addWidget(self.title, 0, 1)
        font = QtGui.QFont()
        font.setItalic(True)
        self.title.setFont(font)
        self.title.setObjectName("title")

        self.graphWidget = QtWidgets.QWidget(self.centralwidget)
        #self.graphWidget.setGeometry(QtCore.QRect(40, 70, 741, 181))
        self.graphWidget.setObjectName("graphWidget")
        self.gridLayout.addWidget(self.plot,1, 1, 3, 1)

        self.spectrogramWidget = QtWidgets.QWidget(self.centralwidget)
        #self.spectrogramWidget.setGeometry(QtCore.QRect(40, 290, 741, 181))
        self.spectrogramWidget.setObjectName("spectrogramWidget")
        self.gridLayout.addWidget(self.plot2, 0, 1, 3, 1)

        self.newWav.raise_()
        self.OXSlider.raise_()
        self.OYSlider.raise_()
        self.title.raise_()
        self.spectrogramWidget.raise_()
        self.openWav.raise_()
        self.graphWidget.raise_()

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 810, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Spektrogram - Małgorzata Wiśniewska"))
        self.openWav.setText(_translate("MainWindow", "Otwórz plik .wav"))
        self.newWav.setText(_translate("MainWindow", "Stwórz nowy plik .wav"))

    def pick_new(self):
        dialog = QtWidgets.QFileDialog
        folder_path = dialog.getExistingDirectory(None, "Wybierz plik .wav:")
        return folder_path

    def handleOpenButton(self):
        title = self.openWav.text()
        dialog = QtWidgets.QFileDialog
        file_list = dialog.getOpenFileNames(self, title, None, 'wav-files: *.wav')
        self.filePath = str(file_list[0])


