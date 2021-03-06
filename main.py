
import math
import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WeldCalc(object):
    def setupUi(self, WeldCalc):
        WeldCalc.setObjectName("WeldCalc")
        WeldCalc.resize(800, 600)
        WeldCalc.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(WeldCalc)
        self.centralwidget.setObjectName("centralwidget")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(70, 70, 141, 21))
        self.radioButton.setCheckable(True)
        self.radioButton.setChecked(False)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(300, 70, 141, 21))
        self.radioButton_2.setObjectName("radioButton_2")

        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(490, 70, 161, 21))
        self.radioButton_3.setObjectName("radioButton_3")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.select())
        self.pushButton.setGeometry(QtCore.QRect(200, 460, 341, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.pushButton.setObjectName("pushButton")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(480, 130, 201, 201))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(54, 162, 162);")
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.widget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.label_6.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setAutoFillBackground(False)
        self.label_6.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(10, 190, 331, 111))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.widget1.setFont(font)
        self.widget1.setObjectName("widget1")
        self.formLayout = QtWidgets.QFormLayout(self.widget1)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(0, 153, 0);")
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(85, 255, 127);")
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_3 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(0, 153, 0);")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("background-color: rgb(85, 255, 127);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.label_4 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(0, 153, 0);")
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("background-color: rgb(85, 255, 127);")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        WeldCalc.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(WeldCalc)
        self.statusbar.setObjectName("statusbar")
        WeldCalc.setStatusBar(self.statusbar)

        self.retranslateUi(WeldCalc)
        QtCore.QMetaObject.connectSlotsByName(WeldCalc)


    def select(self):
        self.label_6.setText("Enter value")
        if self.radioButton.isChecked():
            a = int(self.lineEdit.text()) * (math.cos(math.radians(45)))
            self.label_6.setText(f"{round(a, 5)}")
        if self.radioButton_2.isChecked():
            a = int(self.lineEdit_3.text())
            self.label_6.setText(f"{round(a, 5)}")
        if self.radioButton_3.isChecked():
            a = int(self.lineEdit.text() + self.lineEdit_3.text()) * (
                math.cos(math.radians(int(self.lineEdit_4.text()))))
            self.label_6.setText(f"{round(a, 5)}")

    def retranslateUi(self, WeldCalc):
        _translate = QtCore.QCoreApplication.translate
        WeldCalc.setWindowTitle(_translate("WeldCalc", "Weld Calculator"))
        self.radioButton.setText(_translate("WeldCalc", "Double Fillet Weld "))
        self.radioButton_2.setText(_translate("WeldCalc", "Double Full Penetration "))
        self.radioButton_3.setText(_translate("WeldCalc", "Double Partial Penetration "))
        self.pushButton.setText(_translate("WeldCalc", "Count"))
        self.label_5.setText(_translate("WeldCalc", "WeldThroatThickness"))
        self.label_6.setText(_translate("WeldCalc", "Result"))
        self.label.setText(_translate("WeldCalc", "Weld Leg Height Horizontal(r)"))
        self.label_3.setText(_translate("WeldCalc", "Penetration Depth(s)"))
        self.label_4.setText(_translate("WeldCalc", "Angle(Alpha)"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    WeldCalc = QtWidgets.QMainWindow()
    ui = Ui_WeldCalc()
    ui.setupUi(WeldCalc)
    WeldCalc.show()
    sys.exit(app.exec_())
