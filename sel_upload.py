from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# 設置 ChromeDriver 的路徑
chrome_driver_path = r'path_to_chromedriver'

# 設置 Chrome 瀏覽器選項
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

# 初始化 WebDriver
driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)

# 打開目標網站
url = 'https://example.com'  # 替換為實際的網站 URL
driver.get(url)

# 等待網頁加載完成（視情況可調整等待時間）
time.sleep(5)

# 定位並點擊上傳按鈕（根據實際情況修改選擇器）
upload_button = driver.find_element(By.ID, 'upload_button_id')  # 替換為實際的上傳按鈕 ID
upload_button.click()

# 等待上傳窗口彈出（視情況可調整等待時間）
time.sleep(2)

# 定位並上傳 Word 檔案（根據實際情況修改選擇器）
file_input = driver.find_element(By.NAME, 'file_input_name')  # 替換為實際的文件輸入框名稱
file_path = r'C:\path_to_word_file\example.docx'  # 替換為實際的 Word 檔案路徑
file_input.send_keys(file_path)

# 提交上傳（根據實際情況修改選擇器）
submit_button = driver.find_element(By.ID, 'submit_button_id')  # 替換為實際的提交按鈕 ID
submit_button.click()

# 等待上傳完成（視情況可調整等待時間）
time.sleep(5)

# 關閉瀏覽器
driver.quit()
=============================================================================================
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import base64

# 設置 ChromeDriver 的路徑
chrome_driver_path = r'path_to_chromedriver'

# 設置 Chrome 瀏覽器選項
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

# 初始化 WebDriver
driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)

# 打開目標網站
url = 'https://example.com'  # 替換為實際的網站 URL
driver.get(url)

# 等待網頁加載完成（視情況可調整等待時間）
time.sleep(5)

# 定位文件拖拽的目標位置（根據實際情況修改選擇器）
drop_area = driver.find_element(By.ID, 'drop_area_id')  # 替換為實際的拖拽區域 ID

# 模擬文件拖拽操作
file_path = r'C:\path_to_word_file\example.docx'  # 替換為實際的 Word 檔案路徑

# 使用 Base64 編碼文件內容
with open(file_path, 'rb') as file:
    base64_file = base64.b64encode(file.read()).decode()

# 使用 JavaScript 模擬拖拽操作
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

# 等待上傳完成（視情況可調整等待時間）
time.sleep(5)

# 關閉瀏覽器
driver.quit()
