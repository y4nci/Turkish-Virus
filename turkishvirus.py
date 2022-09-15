import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap

class Window(QtWidgets.QWidget):

    def __init__(self):
        super(Window, self).__init__()

        self.init_ui()

    def init_ui(self):
        error = "Hi, I am a Turkish virus but because of poor technology in my country unfortunately\n" + \
                "I am not able to harm your computer. Please be so kind to delete one of your important\n" + \
                "files yourself and then forward me to other users. Many thanks for your cooperation! Best\n" + \
                "regards, Turkish Virus."
        self.setWindowTitle("Virus Alert!")
        self.setGeometry(0, 0, 640, 220)
        qtRectangle = self.frameGeometry()
        centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        self.error_message = QtWidgets.QLabel(error)
        self.error_image = QtWidgets.QLabel(self)
        self.pixmap = QPixmap('Error_Message_Icon.png')
        self.error_image.setPixmap(self.pixmap.scaled(50, 50))

        layout = QtWidgets.QHBoxLayout()
        layout.addStretch()
        layout.addWidget(self.error_image)
        layout.addWidget(self.error_message)
        layout.addStretch()

        self.setLayout(layout)

        self.show()


app = QtWidgets.QApplication(sys.argv)

window = Window()

sys.exit(app.exec_())
