import sys  #https://steam.oxxostudio.tw/category/python/pyqt5/qlabel.html
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(605, 370)
        Form.setStyleSheet("border-color: rgb(255, 255, 255);")

        # Add login inputs and button
        self.username_label = QtWidgets.QLabel(Form)
        self.username_label.setGeometry(QtCore.QRect(160, 20, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.username_label.setFont(font)
        self.username_label.setAlignment(QtCore.Qt.AlignCenter)
        self.username_label.setObjectName("username_label")

        self.username_input = QtWidgets.QLineEdit(Form)
        self.username_input.setGeometry(QtCore.QRect(260, 20, 181, 31))
        self.username_input.setObjectName("username_input")

        self.password_label = QtWidgets.QLabel(Form)
        self.password_label.setGeometry(QtCore.QRect(160, 60, 91, 31))
        font.setPointSize(12)
        self.password_label.setFont(font)
        self.password_label.setAlignment(QtCore.Qt.AlignCenter)
        self.password_label.setObjectName("password_label")

        self.password_input = QtWidgets.QLineEdit(Form)
        self.password_input.setGeometry(QtCore.QRect(260, 60, 181, 31))
        self.password_input.setObjectName("password_input")
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)

        self.filename_label = QtWidgets.QLabel(Form)
        self.filename_label.setGeometry(QtCore.QRect(160, 100, 91, 31))
        font.setPointSize(12)
        self.filename_label.setFont(font)
        self.filename_label.setAlignment(QtCore.Qt.AlignCenter)
        self.filename_label.setObjectName("filename_label")

        self.filename_input = QtWidgets.QLineEdit(Form)
        self.filename_input.setGeometry(QtCore.QRect(260, 100, 181, 31))
        self.filename_input.setObjectName("filename_input")

        self.login_button = QtWidgets.QPushButton(Form)
        self.login_button.setGeometry(QtCore.QRect(260, 140, 91, 31))
        font.setPointSize(12)
        self.login_button.setFont(font)
        self.login_button.setObjectName("login_button")

        self.login_status = QtWidgets.QLabel(Form)
        self.login_status.setGeometry(QtCore.QRect(160, 180, 281, 31))
        font.setPointSize(10)
        self.login_status.setFont(font)
        self.login_status.setAlignment(QtCore.Qt.AlignCenter)
        self.login_status.setObjectName("login_status")

        # Upload file button
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(210, 220, 171, 31))
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setVisible(False)  # Hide the upload button initially

        

        # Choose output folder button=====================================================================
        self.outputButton = QtWidgets.QPushButton(Form)
        self.outputButton.setGeometry(QtCore.QRect(360, 220, 171, 31))
        font.setPointSize(12)
        self.outputButton.setFont(font)
        self.outputButton.setObjectName("outputButton")
        self.outputButton.setVisible(False)  # Hide the output button initially



        
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 80, 431, 71))
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setLineWidth(1)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setIndent(-1)
        self.label.setObjectName("label")
        self.label.setVisible(False)  # Hide the upload label initially

        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(160, 340, 261, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setTextVisible(False)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setValue(0)
        self.progressBar.setVisible(False)  # Hide the progress bar initially

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(100, 150, 400, 30))
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_2.setVisible(False)  # Hide the label initially

        #顯示在跑的東西
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(160, 290, 261, 50))
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_3.setWordWrap(True)
        self.label_3.setVisible(False)  # Hide the label initially

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # Connect the button click to the login method
        self.login_button.clicked.connect(self.login)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Get_table"))
        self.username_label.setText(_translate("Form", "Username:"))
        self.password_label.setText(_translate("Form", "Password:"))
        self.filename_label.setText(_translate("Form", "Filename:"))
        self.login_button.setText(_translate("Form", "Login"))
        
        self.outputButton.setText(_translate("Form", "Choose Output Folder"))#-----------
        
        self.login_status.setText(_translate("Form", ""))
        self.pushButton.setText(_translate("Form", "Upload File"))
        self.label.setText(_translate("Form", "Choose word file\n"
                                      "(Security B / system)"))
        self.label_2.setText(_translate("Form", "No file chosen"))

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        filename = self.filename_input.text()

        # Add your authentication logic here
        if username == "your_username" and password == "your_password":  # Replace with your actual logic
            self.login_status.setText("Login successful!")

            # Hide login elements
            self.username_label.setVisible(False)
            self.username_input.setVisible(False)
            self.password_label.setVisible(False)
            self.password_input.setVisible(False)
            self.filename_label.setVisible(False)
            self.filename_input.setVisible(False)
            self.login_button.setVisible(False)
            self.login_status.setVisible(False)

            # Show upload elements
            self.pushButton.setVisible(True)

            self.outputButton.setVisible(True)#----------------
            
            self.label.setVisible(True)
            self.progressBar.setVisible(True)
            self.label_2.setVisible(True)
            self.label_3.setVisible(True)

            self.pushButton.clicked.connect(lambda: self.choose_file(filename))
            self.outputButton.clicked.connect(self.choose_output_folder)#---------------------
        else:
            self.login_status.setText("Incorrect username or password.")

    def choose_file(self, filename):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(None, "Open Word File", "", "Word Files (*.docx);;All Files (*)", options=options)
        if file_path:
            self.label_2.setText(f"File chosen: {file_path}")
            # 這裡可以執行上傳操作或其他處理
            self.handle_file(file_path, filename)

    def handle_file(self, file_path, filename):
        # 在這裡處理文件，例如上傳到網站或其他操作
        self.label_3.setText(f"上傳檔案中 {filename}")
        self.progressBar.setValue(20)
        # print(f"Handling file: {file_path}")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
