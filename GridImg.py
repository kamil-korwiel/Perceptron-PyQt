from PyQt6.QtWidgets import QGridLayout, QPushButton, QWidget
from functools import partial
from PySide6.QtCore import Slot
import numpy
import matrixes
from utilitis import convertMatrixToArray, convertMatrixToDic


class GridImg(QWidget):

    def __init__(self):
        super().__init__()
        self.gridlayout = QGridLayout()
        self.matrix = matrixes.matrix_default
        self.dictGridData = convertMatrixToDic(self.matrix)
        self.array = convertMatrixToArray(self.matrix)
        self.list_buttons = []
        self._setupGrid()
        self.setLayout(self.gridlayout)

    def rand(self):
        index = 0
        for data in self.array:
            r = numpy.random.randint(0,20)
            # print(r)
            if (r == 5):
                if(data == 1):
                    self.list_buttons[index].setStyleSheet(
                        'QPushButton'
                        "{"
                        "background : white;"
                        'border-style: solid;'
                        'border-width: 1px;'
                        "}"
                    )
                    self.array[index] = 0 
                else:
                    self.list_buttons[index].setStyleSheet(
                        'QPushButton'
                        "{"
                        "background : red;"
                        'border-style: solid;'
                        'border-width: 1px;'
                        "}"
                    )
                    self.array[index] = 1
            index += 1
        # print(self.array)

    def _setupGrid(self):
        m = n = 0
        for vec in self.matrix:
            n = 0
            for i in vec:
                button = QPushButton()
                button.setFixedSize(60, 60)
                if(i == 1):
                    button.setStyleSheet('QPushButton'
                                         "{"
                                         "background : red;"
                                         'border-style: solid;'
                                         'border-width: 1px;'
                                         "}"
                                         )
                else:
                    button.setStyleSheet('QPushButton'
                                         "{"
                                         "background : white;"
                                         'border-style: solid;'
                                         'border-width: 1px;'
                                         "}"
                                         )
                # button.clicked.connect(partial(self.changeVareble, m, n, 5))
                var = 5*m + n
                button.clicked.connect(partial(self.changeVareble2, var))
                self.list_buttons.append(button)
                self.gridlayout.addWidget(button, m, n)
                n += 1
            m += 1

    @Slot()
    def changeVareble(self, m, n, vecsize):
        var = vecsize*m + n
       
        if(self.dictGridData[(m, n)] == 1):
            self.list_buttons[var].setStyleSheet(
                'QPushButton'
                "{"
                "background : white;"
                'border-style: solid;'
                'border-width: 1px;'
                "}"
            )
            self.matrix[m, n] = 0
            self.dictGridData[(m, n)] = 0
        else:
            self.list_buttons[var].setStyleSheet(
                'QPushButton'
                "{"
                "background : red;"
                'border-style: solid;'
                'border-width: 1px;'
                "}"
            )
            self.matrix[m, n] = 1
            self.dictGridData[(m, n)] = 1
    
    @Slot()
    def changeVareble2(self,index):
        #  m = (index - n)/vecsize
        #  n = (index - m)/vecsize
        if(self.array[index] == 1):
            self.list_buttons[index].setStyleSheet(
                'QPushButton'
                "{"
                "background : white;"
                'border-style: solid;'
                'border-width: 1px;'
                "}"
            )
            self.array[index] = 0
        else:
            self.list_buttons[index].setStyleSheet(
                'QPushButton'
                "{"
                "background : red;"
                'border-style: solid;'
                'border-width: 1px;'
                "}"
            )
            self.array[index] = 1

    def setGrid(self, matrix):
        self.matrix = matrix
        self.array = convertMatrixToArray(matrix)
        self.dictGridData = convertMatrixToDic(matrix)
        for button, data in zip(self.list_buttons, self.array):

            if(data == 1):
                button.setStyleSheet(
                    'QPushButton'
                    "{"
                    "background : red;"
                    'border-style: solid;'
                    'border-width: 1px;'
                    "}"
                )
            else:
                button.setStyleSheet(
                    'QPushButton'
                    "{"
                    "background : white;"
                    'border-style: solid;'
                    'border-width: 1px;'
                    "}"
                )
    
    def getArray(self):
        print (self.array)
        return self.array