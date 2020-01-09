import pygame
from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
from pyqtgraph import PlotWidget
from scipy import signal, random
from scipy.io import wavfile
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt



class Ui_MainWindow():
    def __init__(self):
        self.filePath = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 791, 551))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.widget = QtWidgets.QWidget(self.gridLayoutWidget)
        self.widget.setObjectName("widget")

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.gridLayout.addWidget(self.canvas)

        self.gridLayout.addWidget(self.widget, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuOX = QtWidgets.QMenu(self.menuView)
        self.menuOX.setObjectName("menuOX")
        self.menuOY = QtWidgets.QMenu(self.menuView)
        self.menuOY.setObjectName("menuOY")
        self.menuPasmo = QtWidgets.QMenu(self.menubar)
        self.menuPasmo.setObjectName("menuPasmo")
        self.menuSave = QtWidgets.QMenu(self.menubar)
        self.menuSave.setObjectName("menuSave")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionOpen = QtWidgets.QAction(MainWindow, triggered=self.drawGraph)
        self.actionOpen.setObjectName("actionOpen")

        self.actionPlusX = QtWidgets.QAction(MainWindow)
        self.actionPlusX.setObjectName("actionPlusX")

        self.actionMinusX = QtWidgets.QAction(MainWindow)
        self.actionMinusX.setObjectName("actionMinusX")

        self.actionPlusY = QtWidgets.QAction(MainWindow)
        self.actionPlusY.setObjectName("actionPlusY")

        self.actionMinusY = QtWidgets.QAction(MainWindow)
        self.actionMinusY.setObjectName("actionMinusY")

        self.actionNarrow = QtWidgets.QAction(MainWindow)
        self.actionNarrow.setObjectName("actionNear")

        self.actionWide = QtWidgets.QAction(MainWindow)
        self.actionWide.setObjectName("actionWide")

        self.actionSaveSpectrogram = QtWidgets.QAction(MainWindow)
        self.actionSaveSpectrogram.setObjectName("actionSaveSpectrogram")

        self.actionSaveAmplitude = QtWidgets.QAction(MainWindow)
        self.actionSaveAmplitude.setObjectName("actionSaveAmplitude")

        self.actionSaveBoth = QtWidgets.QAction(MainWindow)
        self.actionSaveBoth.setObjectName("actionSaveBoth")

        self.actionOkienkowanie = QtWidgets.QAction(MainWindow)
        self.actionOkienkowanie.setObjectName("actionOkienkowanie")

        self.menuFile.addAction(self.actionOpen)
        self.menuSave.addAction(self.actionSaveSpectrogram)
        self.menuSave.addAction(self.actionSaveAmplitude)
        self.menuSave.addAction(self.actionSaveBoth)
        self.menuFile.addAction(self.menuSave.menuAction())
        self.menuOX.addAction(self.actionPlusX)
        self.menuOX.addAction(self.actionMinusX)
        self.menuOY.addAction(self.actionPlusY)
        self.menuOY.addAction(self.actionMinusY)
        self.menuView.addAction(self.menuOX.menuAction())
        self.menuView.addAction(self.menuOY.menuAction())
        self.menuView.addAction(self.actionOkienkowanie)
        self.menuPasmo.addAction(self.actionNarrow)
        self.menuPasmo.addAction(self.actionWide)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuPasmo.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Spektrogram - Małgorzata Wiśniewska"))
        self.menuFile.setTitle(_translate("MainWindow", "Plik"))
        self.menuView.setTitle(_translate("MainWindow", "Wyświetlacz"))
        self.menuOX.setTitle(_translate("MainWindow", "Oś X"))
        self.menuOY.setTitle(_translate("MainWindow", "Oś Y"))
        self.menuPasmo.setTitle(_translate("MainWindow", "Wybór pasma"))
        self.menuSave.setTitle(_translate("MainWindow", "Zapisz wykres"))
        self.actionOpen.setText(_translate("MainWindow", "Otwieranie"))
        self.actionPlusX.setText(_translate("MainWindow", "Przybliż"))
        self.actionMinusX.setText(_translate("MainWindow", "Oddal"))
        self.actionPlusY.setText(_translate("MainWindow", "Przybliż"))
        self.actionMinusY.setText(_translate("MainWindow", "Oddal"))
        self.actionNarrow.setText(_translate("MainWindow", "Wąskopasowy"))
        self.actionWide.setText(_translate("MainWindow", "Szerokopasmowy"))
        self.actionSaveSpectrogram.setText(_translate("MainWindow", "Zapisz spektrogram"))
        self.actionSaveAmplitude.setText(_translate("MainWindow", "Zapisz wykres amplitudy"))
        self.actionSaveBoth.setText(_translate("MainWindow", "Zapisz oba wykresy"))
        self.actionOkienkowanie.setText(_translate("MainWindow", "Okienkowanie"))

    def openWav(self):
        title = self.actionOpen.text()
        dialog = QtWidgets.QFileDialog()
        filename, _filter = dialog.getOpenFileNames(dialog, title, None, 'wav-files: *.wav')
        self.filePath = str(filename[0])

    def calculateData(self):
        self.samplerate, self.data = wavfile.read(
            self.filePath)  # samplerate -> częstotliwość, data-> wartości amplitudy dla każdej próbki
        self.sekundy = len(self.data) / float(self.samplerate)

    def prepareSpectroGraph(self):
        self.spectrGraph.specgram(self.data[:, 0], Fs=self.samplerate)
        self.spectrGraph.set_ylabel('Częstotliwość [Hz]')

    def prepareAmplitudeGraph(self):
        self.ampliGraphax.plot(np.arange(len(self.data)) / float(self.samplerate), self.data[:, 0], )
        self.ampliGraphax.set_xlim(left=0, right=(np.arange(len(self.data)) / float(self.samplerate))[-1])
        self.ampliGraphax.set_ylabel('Amplituda')
        self.ampliGraphax.set_xlabel('Czas [s]')

    def playWav(self):
        pygame.init()
        pygame.mixer.music.load(str(self.filePath))
        pygame.mixer.music.play()

    def drawGraph(self):
        self.openWav()
        self.calculateData()
        self.figure.clear()
        self.playWav()
        self.spectrGraph = self.figure.add_axes([0.1, 0.5, 0.8, 0.4], xticklabels=[], ylim=(-1.2, 1.2))
        self.ampliGraphax = self.figure.add_axes([0.1, 0.1, 0.8, 0.4], ylim=(-100000, 100000))
        self.prepareAmplitudeGraph()
        self.prepareSpectroGraph()
        self.spectrGraph.draw(renderer=None)
        self.ampliGraphax.draw(renderer=None)
        self.canvas.draw()

    '''def saveSpectrogram(self):
        title = self.actionSaveSpectrogram.text()
        item = self.spectrogramWidget
        pix = item.grab()
        dialog = QtWidgets.QFileDialog()
        filename = dialog.getSaveFileName(dialog, title, None, 'Image Files (*.png *.jpg *.jpeg)')
        pix.save(str(filename[0]))

    def saveAmplitude(self):
        title = self.actionSaveAmplitude.text()
        item = self.amplitudeWidget
        pix = item.grab()
        dialog = QtWidgets.QFileDialog()
        filename = dialog.getSaveFileName(dialog, title, None, 'Image Files (*.png *.jpg *.jpeg)')
        pix.save(str(filename[0]))

    def saveBoth(self):
        self.saveSpectrogram()
        self.saveAmplitude()'''
