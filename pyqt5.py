import sys #https://steam.oxxostudio.tw/category/python/pyqt5/qlabel.html
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(605, 370)
        Form.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(210, 190, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 20, 431, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setLineWidth(1)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setIndent(-1)
        self.label.setObjectName("label")
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(160, 260, 261, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setTextVisible(False)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setValue(0)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(100, 150, 400, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        #顯示在跑的東西
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(160, 290, 261, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_3.setWordWrap(True)



        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # Connect the button click to the choose_file method
        self.pushButton.clicked.connect(self.choose_file)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Get_table"))
        self.pushButton.setText(_translate("Form", "Upload File"))
        self.label.setText(_translate("Form", "Choose word file\n"
                                      "(Security B / system)"))
        self.label_2.setText(_translate("Form", "No file chosen"))

    def choose_file(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(None, "Open Word File", "", "Word Files (*.docx);;All Files (*)", options=options)
        if file_path:
            self.label_2.setText(f"File chosen: {file_path}")
            # 這裡可以執行上傳操作或其他處理
            self.handle_file(file_path)

    def handle_file(self, file_path):
        # 在這裡處理文件，例如上傳到網站或其他操作
        self.label_3.setText(f"上傳檔案中{file_path}")
        self.progressBar.setValue(20)
        #print(f"Handling file: {file_path}")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
