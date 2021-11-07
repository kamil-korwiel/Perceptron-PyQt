
from PyQt6.QtWidgets import QPushButton


class MyButton(QPushButton):
    def __init__(self, x, y, bin_data, text='', parent=None):
        super(MyButton, self).__init__(text, parent=parent)
        self.x = x
        self.y = y
        self.bin_data = bin_data

        if(bin_data == 0):
            self.setStyleSheet('QPushButton'
                               "{"
                               "background : red;"
                               'border-style: solid;'
                               'border-width: 1px;'
                               "}"
                               )
        else:
            self.setStyleSheet('QPushButton'
                               "{"
                               "background : white;"
                               'border-style: solid;'
                               'border-width: 1px;'
                               "}"
                               )
