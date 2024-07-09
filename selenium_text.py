from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# 配置 ChromeDriver 的路徑
chromedriver_path = 'path_to_chromedriver'

# 創建 Chrome 瀏覽器的驅動實例
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service)

# 打開目標網頁
url = 'https://example.com'
driver.get(url)

# 等待頁面加載完成
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

# 獲取頁面源碼
html_content = driver.page_source

# 使用 BeautifulSoup 解析頁面源碼
soup = BeautifulSoup(html_content, 'html.parser')

# 關閉瀏覽器
driver.quit()

# 創建一個空列表來存儲提取的文本
extracted_text = []

# 定義要查找的標題和內文標籤
content_tags = ['h1', 'h2', 'h3', 'span', 'a', 'p', 'ul', 'ol']

def extract_content(element):
    if element.name in content_tags:
        if element.name in ['ul', 'ol']:
            items = element.find_all('li')
            for item in items:
                if item.get_text(strip=True):
                    extracted_text.append(f"- {item.get_text(strip=True)}")
            extracted_text.append("\n")
        else:
            if element.get_text(strip=True):
                if element.name in ['h1', 'h2', 'h3']:
                    extracted_text.append(f"\n\n{element.get_text(strip=True)}\n{'=' * len(element.get_text(strip=True))}\n")
                else:
                    extracted_text.append(f"{element.get_text(strip=True)}\n")

# 遍歷 body 的所有子節點，按順序提取內容
for element in soup.body.descendants:
    if element.name in content_tags:
        extract_content(element)

# 定義輸出文本文件的路徑
output_path = r'C:\Users\steve\Desktop\intern_practice\DRMDB\data\output_text.txt'

# 將提取的文本寫入文本文件
with open(output_path, 'w', encoding='utf-8') as f:
    for line in extracted_text:
        f.write(line + '\n')

print(f"Successfully saved extracted text to {output_path}")
