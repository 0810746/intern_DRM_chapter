from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 設置 Chrome 瀏覽器的無頭模式
chrome_options = Options()
chrome_options.add_argument("--headless")  # 啟用無頭模式
chrome_options.add_argument("--disable-gpu")  # 如果在 Windows 上，禁用 GPU 加速可以防止一些崩潰

# 指定 ChromeDriver 路徑（可選）
chrome_driver_path = 'path_to_chromedriver'  # 將此替換為實際的 ChromeDriver 路徑
service = Service(chrome_driver_path)

# 啟動瀏覽器
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("http://example.com")

# 等待按鈕可點擊並點擊按鈕
wait = WebDriverWait(driver, 10)
confirm_button = wait.until(EC.element_to_be_clickable((By.ID, 'confirm_button_id')))
confirm_button.click()

# 等待特定文字出現
try:
    success_text = wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), '成功')]")))
    print("成功: 已出現成功訊息")
except:
    try:
        failure_text = wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), '失敗')]")))
        print("失敗: 已出現失敗訊息")
    except:
        print("未偵測到特定訊息")

# 關閉瀏覽器
driver.quit()
