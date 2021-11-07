from functools import partial
from PyQt6 import QtGui
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPalette
from PyQt6.QtWidgets import QApplication, QGridLayout, QLabel, QLineEdit, QMainWindow, QPushButton, QVBoxLayout, QWidget
import sys
import numpy

from numpy.random.mtrand import permutation
from Perceptror import Perceptron
import matrixes
from GridImg import GridImg
from utilitis import convertMatrixToArray

targets = numpy.array([
[1.0, 0.0, 0.0, 0.0, 0.0 ,0.0 ,0.0 ,0.0, 0.0, 0.0],
[0.0, 1.0, 0.0, 0.0, 0.0 ,0.0 ,0.0 ,0.0, 0.0, 0.0],
[0.0, 0.0, 1.0, 0.0, 0.0 ,0.0 ,0.0 ,0.0, 0.0, 0.0],
[0.0, 0.0, 0.0, 1.0, 0.0 ,0.0 ,0.0 ,0.0, 0.0, 0.0],
[0.0, 0.0, 0.0, 0.0, 1.0 ,0.0 ,0.0 ,0.0, 0.0, 0.0],
[0.0, 0.0, 0.0, 0.0, 0.0 ,1.0 ,0.0 ,0.0, 0.0, 0.0],
[0.0, 0.0, 0.0, 0.0, 0.0 ,0.0 ,1.0 ,0.0, 0.0, 0.0],
[0.0, 0.0, 0.0, 0.0, 0.0 ,0.0 ,0.0 ,1.0, 0.0, 0.0],
[0.0, 0.0, 0.0, 0.0, 0.0 ,0.0 ,0.0 ,0.0, 1.0, 0.0],
[0.0, 0.0, 0.0, 0.0, 0.0 ,0.0 ,0.0 ,0.0, 0.0, 1.0]
])


dataset = [ 
    convertMatrixToArray(matrixes.matrix0),
    convertMatrixToArray(matrixes.matrix1),
    convertMatrixToArray(matrixes.matrix2),
    convertMatrixToArray(matrixes.matrix3),
    convertMatrixToArray(matrixes.matrix4),
    convertMatrixToArray(matrixes.matrix5),
    convertMatrixToArray(matrixes.matrix6),
    convertMatrixToArray(matrixes.matrix7),
    convertMatrixToArray(matrixes.matrix8),
    convertMatrixToArray(matrixes.matrix9)
]

class PyCalcUi(QMainWindow):
    """PyCalc's View (GUI)."""
    def __init__(self):
        """View initializer."""
        super().__init__()
        # Set some main window's properties
        self.setWindowTitle('PyCalc')
        # self.setFixedSize(235, 500)
        # Set the central widget and the general layout
        self.label = QLabel('null')
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        self.gridBinaryWidget = GridImg()
        
        # Create the display and the buttons
        self._createButtons()


    def _createButtons(self):
        """Create the buttons."""
        self.buttons = {}
        buttonsLayout = QGridLayout()
        
        

        # Button text | position on the QGridLayout
        buttons = {'7': (0, 0),
                   '8': (0, 1),
                   '9': (0, 2),
                #   '/': (0, 3),
                   'clean': (2, 3),
                   '4': (1, 0),
                   '5': (1, 1),
                   '6': (1, 2),
                   'rand': (1, 3),
                   'learn': (1, 4),
                   '1': (2, 0),
                   '2': (2, 1),
                   '3': (2, 2),
                #   '-': (2, 3),
                #   ')': (2, 4),
                   '0': (3, 0),
                #    '00': (3, 1),
                #    '.': (3, 2),
                #    '+': (3, 3),
                   'check': (3, 4),
                  }
        # Create the buttons and add them to the grid layout
        for btnText, pos in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(40, 40)
            buttonsLayout.addWidget(self.buttons[btnText], pos[0], pos[1])
        
        # Add buttonsLayout to the general layout
        self.label.setStyleSheet("QLabel { background-color : gray; color : black;border-style: outset; border-width: 2px; border-radius: 10px; border-color: beige; }");
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        buttonsLayout.addWidget(self.label,0,4)
        vLayout = QVBoxLayout()
        # widget1 = QWidget()
        widget2 = QWidget()

        #widget1.setLayout(buttonsBinLayout)
        widget2.setLayout(buttonsLayout)
        vLayout.addWidget(self.gridBinaryWidget)
        vLayout.addWidget(widget2)

        self.generalLayout.addLayout(vLayout)
    

# Create a Controller class to connect the GUI and the model
class PyCalcCtrl:
    """PyCalc's Controller."""
    def __init__(self,view:PyCalcUi):
        """Controller initializer."""
        self._view = view
        self.perceptrons = []
        # Connect signals and slots
        self._connectSignals()
        self._createPerceptrons()

    def _createPerceptrons(self):
        for i in range(10):
            per = Perceptron(len(dataset[i]))
           # print(f"Index {i} , {targets[i]}")
            per.trainWithPocket3(dataset,targets[i])
            # print(f"Index {i} , {per.accuracy(dataset,targets[i])}")
            self.perceptrons.append(per)
    
    def _learn(self):
        i = 0
        for p in self.perceptrons:
            p.trainWithPocket3(dataset,targets[i])
            i += 1

    def _acionCheak(self,input):
        i = 0
        # print("--------------------------")
        print(input)
        for per in self.perceptrons:
            p = per.predict(input)
            print(f"Nr {i} predic value = {p}")
            i += 1
    
    def _cheak(self,d):
        i = 0
        predic_list = []
        # print("--------------------------")
        array = self._view.gridBinaryWidget.array
        # print(array)
        for per in self.perceptrons:
            p = per.predict(array)
            if p == 1.0: predic_list.append(i)
            # print(f"Nr {i} predic value = {p}")
            i += 1
        print(predic_list)
        self._view.label.setText(str(predic_list))

    def test(self):
        print("fuk")
        print(self._view.gridBinaryWidget.array)

    def _connectSignals(self):
        """Connect signals and slots."""
        # for btnText, btn in self._view.buttons_bin.items():
        #     # if btnText not in {'=', 'C'}:
        #     btn.clicked.connect(partial(self._changeButtonColor,btnText))
        self._view.buttons["clean"].clicked.connect(partial(self._view.gridBinaryWidget.setGrid, matrixes.matrix_default))
        self._view.buttons["1"].clicked.connect(partial(self._view.gridBinaryWidget.setGrid, matrixes.matrix1))
        self._view.buttons["2"].clicked.connect(partial(self._view.gridBinaryWidget.setGrid, matrixes.matrix2))
        self._view.buttons["3"].clicked.connect(partial(self._view.gridBinaryWidget.setGrid, matrixes.matrix3))
        self._view.buttons["4"].clicked.connect(partial(self._view.gridBinaryWidget.setGrid, matrixes.matrix4))
        self._view.buttons["5"].clicked.connect(partial(self._view.gridBinaryWidget.setGrid, matrixes.matrix5))
        self._view.buttons["6"].clicked.connect(partial(self._view.gridBinaryWidget.setGrid, matrixes.matrix6))
        self._view.buttons["7"].clicked.connect(partial(self._view.gridBinaryWidget.setGrid, matrixes.matrix7))
        self._view.buttons["8"].clicked.connect(partial(self._view.gridBinaryWidget.setGrid, matrixes.matrix8))
        self._view.buttons["9"].clicked.connect(partial(self._view.gridBinaryWidget.setGrid, matrixes.matrix9))
        self._view.buttons["0"].clicked.connect(partial(self._view.gridBinaryWidget.setGrid, matrixes.matrix0))
        # self._view.buttons["check"].clicked.connect(partial(self._acionCheak,self._view.gridBinaryWidget.array))
        self._view.buttons["check"].clicked.connect(partial(self._cheak,1))
        self._view.buttons["rand"].clicked.connect(self._view.gridBinaryWidget.rand)
        # self._view.buttons["learn"].clicked.connect(self._le)
 



def main():
    """Main function."""
    # Create an instance of QApplication
    pycalc = QApplication(sys.argv)
    # Show the calculator's GUI
    view = PyCalcUi()
    view.setStyleSheet("PyCalcUi {background : black;}")
    view.show()
        # Create instances of the model and the controller
    PyCalcCtrl(view=view)
    # Execute the calculator's main loop
    sys.exit(pycalc.exec())

if __name__ == '__main__':
    main()

