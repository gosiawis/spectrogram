import sys
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile

class Window(QDialog):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        # a figure instance to plot on
        self.figure = plt.figure()

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)

        # Just some button connected to `plot` method
        self.button = QPushButton('Plot')
        self.button.clicked.connect(self.plot)

        # set the layout
        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def plot(self): #tutaj trzeba dać spektogram
        ''' plot some random stuff '''
        # random data
        #data = [random.random() for i in range(10)]
        frequencies = np.array(5,105,5)
        samplingFrequency = 400

        s1 = np.empty([0])
        s2 = np.empty([0])

        start = 1
        stop = samplingFrequency+1

        for frequency in frequencies:
            sub1 = np.arange(start, stop, 1)
            sub2 = np.sin(2*np.pi*sub1*frequency*1/samplingFrequency)+np.random.randn(len(sub1))

            s1 = np.append(s1, sub1)
            s2 = np.append(s2, sub2)

            start = stop+1
            stop = start+samplingFrequency

        # instead of ax.hold(False)
        self.figure.clear()

        # create an axis
        ax = self.figure.add_subplot(211)

        # plot data
        ax.plot(s1, s2)
        ax.xlabel('Sample')
        ax.ylabel('Amplitude')

        # refresh canvas
        self.canvas.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    samplerate, data = wavfile.read('wavfiles\\bzyk.wav')
    main = Window()
    main.show()

    sys.exit(app.exec_())