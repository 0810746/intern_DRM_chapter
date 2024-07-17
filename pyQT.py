#https://steam.oxxostudio.tw/category/python/pyqt5/qfiledialog.html
import sys
import base64
import time
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt, QUrl
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class DragDropWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Drag and Drop Window")
        self.setGeometry(100, 100, 400, 300)

        self.label = QLabel("Drag and Drop a Word file here", self)
        self.label.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        for url in event.mimeData().urls():
            file_path = url.toLocalFile()
            if file_path.endswith(".docx"):
                self.label.setText(f"File dropped: {file_path}")
                self.upload_file_to_website(file_path)
            else:
                self.label.setText("Please drop a Word (.docx) file")

    def upload_file_to_website(self, file_path):
        # 使用 Selenium 進行文件上傳模擬操作
        chrome_driver_path = r'path_to_chromedriver'  # 替換為實際的 chromedriver 路徑

        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")

        driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)

        url = 'https://example.com'  # 替換為實際的網站 URL
        driver.get(url)

        time.sleep(5)  # 等待網頁加載

        drop_area = driver.find_element(By.ID, 'drop_area_id')  # 替換為實際的拖拽區域 ID

        with open(file_path, 'rb') as file:
            base64_file = base64.b64encode(file.read()).decode()

        driver.execute_script("""
        var dropArea = arguments[0];
        var dataTransfer = new DataTransfer();

        dataTransfer.items.add(new File([new Uint8Array(atob(arguments[1]).split('').map(c => c.charCodeAt(0)))], 'example.docx'));

        var event = new DragEvent('drop', {
            dataTransfer: dataTransfer,
            bubbles: true,
            cancelable: true,
            composed: true
        });

        dropArea.dispatchEvent(event);
        """, drop_area, base64_file)

        time.sleep(5)  # 等待上傳完成
        driver.quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DragDropWindow()
    window.show()
    sys.exit(app.exec_())
