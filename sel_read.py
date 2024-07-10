from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# 設置 ChromeDriver 路徑
chrome_options = Options()
chrome_options.add_argument("--headless")  # 啟用無頭模式

# 啟動 Chrome 瀏覽器
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# 打開目標網頁
url = "https://example.com"
driver.get(url)

# 擷取網頁中所有非表格和非圖片的文字
# 我們可以先擷取所有文字，然後移除表格和圖片中的文字
body = driver.find_element(By.TAG_NAME, "body")

# 移除表格和圖片
for table in body.find_elements(By.TAG_NAME, "table"):
    table_text = table.text
    body_text = body.text.replace(table_text, '')

for img in body.find_elements(By.TAG_NAME, "img"):
    alt_text = img.get_attribute('alt')
    body_text = body_text.replace(alt_text, '')

# 獲取最終的文字
all_text = body_text

# 輸出結果
print(all_text)

# 關閉瀏覽器
driver.quit()




from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# 設置 ChromeDriver 路徑
chrome_options = Options()
chrome_options.add_argument("--headless")  # 啟用無頭模式

# 啟動 Chrome 瀏覽器
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# 打開目標網頁
url = "https://example.com"
driver.get(url)

# 擷取段落和標題中的文本
elements = driver.find_elements(By.XPATH, "//body//*[not(self::table) and not(self::img)]")
all_text = ""
for element in elements:
    if element.tag_name in ["p", "h1", "h2", "h3", "h4", "h5", "h6"]:
        all_text += element.text + "\n"

# 輸出結果
print(all_text)

# 關閉瀏覽器
driver.quit()
