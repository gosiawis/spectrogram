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
        MainWindow.resize(808, 525)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 811, 491))
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
        self.menubar.setGeometry(QtCore.QRect(0, 0, 808, 21))
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

        self.actionOpen = QtWidgets.QAction(MainWindow, triggered=self.openWav)
        self.actionOpen.setObjectName("actionOpen")

        self.actionPlusX = QtWidgets.QAction(MainWindow, triggered=self.plusX)
        self.actionPlusX.setObjectName("actionPlusX")

        self.actionMinusX = QtWidgets.QAction(MainWindow, triggered=self.minusX)
        self.actionMinusX.setObjectName("actionMinusX")

        self.actionPlusY = QtWidgets.QAction(MainWindow, triggered=self.plusY)
        self.actionPlusY.setObjectName("actionPlusY")

        self.actionMinusY = QtWidgets.QAction(MainWindow, triggered=self.minusY)
        self.actionMinusY.setObjectName("actionMinusY")

        self.actionNarrow = QtWidgets.QAction(MainWindow)
        self.actionNarrow.setObjectName("actionNear")

        self.actionWide = QtWidgets.QAction(MainWindow)
        self.actionWide.setObjectName("actionWide")

        self.actionSaveSpectrogram = QtWidgets.QAction(MainWindow, triggered=self.saveSpectrogram)
        self.actionSaveSpectrogram.setObjectName("actionSaveSpectrogram")

        self.actionSaveAmplitude = QtWidgets.QAction(MainWindow, triggered=self.saveAmplitude)
        self.actionSaveAmplitude.setObjectName("actionSaveAmplitude")

        self.actionSaveBoth = QtWidgets.QAction(MainWindow, triggered=self.saveBoth)
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
        self.plusXTimes = 1
        self.minusXTimes = 1
        self.plusYTimes = 1
        self.minusYTimes = 1
        title = self.actionOpen.text()
        dialog = QtWidgets.QFileDialog()
        filename, _filter = dialog.getOpenFileNames(dialog, title, None, 'wav-files: *.wav')
        self.filePath = str(filename[0])
        self.calculateData()
        self.drawGraph(self.xLeftLimit, self.xRightLimit, self.yBottomLimitAmp, self.yTopLimitAmp)

    def calculateData(self):
        # samplerate -> częstotliwość, data-> wartości amplitudy dla każdej próbki
        self.samplerate, self.data = wavfile.read(self.filePath)
        self.times = np.arange(len(self.data)) / float(self.samplerate)
        self.xLeftLimit = 0
        self.xRightLimit = self.times[-1]
        print(self.data)
        print(self.data.ndim)
        if self.data.ndim == 2:
            self.dataDimension = self.data[:, 0]
        elif self.data.ndim == 1:
            self.dataDimension = self.data
        self.yBottomLimitAmp = min(self.dataDimension)
        self.yTopLimitAmp = max(self.dataDimension)
        self.yBottomLimitSpec = 0
        self.yTopLimitSpec = self.samplerate
        self.yDividedAmp = ((self.yBottomLimitAmp * (-1)) + self.yTopLimitAmp) / 24
        self.xDivided = self.xRightLimit / 24

    def prepareSpectroGraph(self):
        self.spectrGraph.specgram(self.dataDimension, Fs=self.samplerate)
        self.spectrGraph.set_ylabel('Częstotliwość [Hz]')
        self.spectrGraph.set_xlabel('Czas [s]')

    def prepareAmplitudeGraph(self):
        self.ampliGraph.plot(self.times, self.dataDimension)
        # self.ampliGraph.set_xlim(left=self.XLeftLimit, right=self.XRightLimit)
        self.ampliGraph.set_ylabel('Amplituda')
        self.ampliGraph.set_xlabel('Czas [s]')

    def playWav(self):
        pygame.init()
        pygame.mixer.music.load(str(self.filePath))
        pygame.mixer.music.play()

    def drawGraph(self, xLeft, xRight, yLeft, yRight):
        self.figure.clear()
        self.playWav()
        self.spectrGraph = self.figure.add_axes([0.13, 0.57, 0.8, 0.4], xticklabels=[],
                                                ylim=(self.yBottomLimitSpec, self.yTopLimitSpec), xlim=(xLeft, xRight))
        self.ampliGraph = self.figure.add_axes([0.13, 0.095, 0.8, 0.4],
                                               ylim=(yLeft, yRight), xlim=(xLeft, xRight))
        self.prepareAmplitudeGraph()
        self.prepareSpectroGraph()
        self.spectrGraph.draw(renderer=None)
        self.ampliGraph.draw(renderer=None)
        self.canvas.draw()

    def saveSpectrogram(self):
        title = self.actionSaveSpectrogram.text()
        dialog = QtWidgets.QFileDialog()
        filename = dialog.getSaveFileName(dialog, title, None, 'Image Files (*.png *.jpg *.jpeg)')
        self.figure.saveFig(str(filename[0]))

    def saveAmplitude(self):
        title = self.actionSaveAmplitude.text()
        item = self.ampliGraph
        pix = item.grab()
        dialog = QtWidgets.QFileDialog()
        filename = dialog.getSaveFileName(dialog, title, None, 'Image Files (*.png *.jpg *.jpeg)')
        pix.save(str(filename[0]))

    def saveBoth(self):
        self.saveSpectrogram()
        self.saveAmplitude()

    def plusX(self):  # works only for amplitude graph
        self.rightXManipulated = self.xRightLimit - (self.xDivided * self.plusXTimes)
        self.leftXManipulated = self.xLeftLimit + (self.xDivided * self.plusXTimes)
        if self.rightXManipulated == self.leftXManipulated:
            return 0
        if self.plusYTimes == 1 and self.minusYTimes == 1:
            self.drawGraph(self.leftXManipulated, self.rightXManipulated, self.yBottomLimitAmp, self.yTopLimitAmp)
        elif self.plusYTimes != 1 or self.minusYTimes != 1:
            self.drawGraph(self.leftXManipulated, self.rightXManipulated, self.bottomYManipulated, self.topYManipulated)
        self.plusXTimes += 1
        self.minusXTimes -= 1

    def minusX(self):
        if self.minusXTimes != self.plusXTimes:
            self.rightXManipulated = self.xRightLimit + (self.xDivided * self.minusXTimes)
            self.leftXManipulated = self.xLeftLimit - (self.xDivided * self.minusXTimes)
        if self.minusXTimes == self.plusXTimes:
            return 0
        if self.rightXManipulated == self.leftXManipulated:
            return 0
        if self.plusYTimes == 1 and self.minusYTimes == 1:
            self.drawGraph(self.leftXManipulated, self.rightXManipulated, self.yBottomLimitAmp, self.yTopLimitAmp)
        elif self.plusYTimes != 1 or self.minusYTimes != 1:
            self.drawGraph(self.leftXManipulated, self.rightXManipulated, self.bottomYManipulated, self.topYManipulated)
        self.plusXTimes -= 1
        self.minusXTimes += 1

    def plusY(self):
        self.topYManipulated = self.yTopLimitAmp - (self.yDividedAmp * self.plusYTimes)
        self.bottomYManipulated = self.yBottomLimitAmp + (self.yDividedAmp * self.plusYTimes)
        if self.topYManipulated == self.bottomYManipulated:
            return 0
        if self.plusXTimes == 1 and self.minusXTimes == 1:
            self.drawGraph(self.xLeftLimit, self.xRightLimit, self.bottomYManipulated, self.topYManipulated)
        elif self.plusXTimes != 1 or self.minusXTimes != 1:
            self.drawGraph(self.leftXManipulated, self.rightXManipulated, self.bottomYManipulated, self.topYManipulated)
        self.plusYTimes += 1
        self.minusYTimes -= 1

    def minusY(self):
        topY = 0
        bottomY = 0
        if self.minusYTimes != self.plusYTimes:
            self.topYManipulated = self.yTopLimitAmp + (self.yDividedAmp * self.minusYTimes)
            self.bottomYManipulated = self.yBottomLimitAmp - (self.yDividedAmp * self.minusYTimes)
        if self.minusYTimes == self.plusYTimes:
            return 0
        if self.topYManipulated == self.bottomYManipulated:
            return 0
        if self.plusXTimes == 1 and self.minusXTimes == 1:
            self.drawGraph(self.xLeftLimit, self.xRightLimit, self.bottomYManipulated, self.topYManipulated)
        elif self.plusXTimes != 1 or self.minusXTimes != 1:
            self.drawGraph(self.leftXManipulated, self.rightXManipulated, self.bottomYManipulated, self.topYManipulated)
        self.plusYTimes += 1
        self.minusYTimes -= 1
