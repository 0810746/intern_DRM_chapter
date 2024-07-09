from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

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

# 定義要查找的表格標題
target_headers = ['要讀的標題1', '要讀的標題2', '要讀的標題3']  # 根據需要調整標題名稱

# 找到所有的表格
tables = driver.find_elements(By.TAG_NAME, "table")

# 儲存符合條件的表格數據和其相應的標題
filtered_data = []

# 遍歷所有表格，篩選具有特定標題的表格
for table in tables:
    try:
        header = table.find_element(By.TAG_NAME, "thead").find_elements(By.TAG_NAME, "td")
        header_texts = [th.find_element(By.TAG_NAME, "span").text.strip() for th in header]
        if set(target_headers).issubset(set(header_texts)):
            # 提取表格前的標題（如h1、h2、h3等）
            heading = table.find_element(By.XPATH, './preceding::h1[1] | ./preceding::h2[1] | ./preceding::h3[1] | ./preceding::h4[1] | ./preceding::h5[1] | ./preceding::h6[1]').text

            # 提取表格數據
            rows = table.find_elements(By.TAG_NAME, "tr")
            table_data = []
            for row in rows:
                cells = row.find_elements(By.TAG_NAME, "td")
                if not cells:
                    cells = row.find_elements(By.TAG_NAME, "th")
                table_data.append([cell.text.strip() for cell in cells])
            
            # 將標題和表格數據一起儲存
            filtered_data.append({"heading": heading, "table_data": table_data})
    except Exception as e:
        print(f"Error processing table: {e}")

# 關閉瀏覽器
driver.quit()

# 將所有表格數據接在一起，並刪除每個表格的標頭
combined_data = []
for item in filtered_data:
    combined_data.extend(item["table_data"][1:])  # 刪除標頭並接在一起

# 將合併的表格數據轉換為 DataFrame
df = pd.DataFrame(combined_data, columns=filtered_data[0]["table_data"][0])  # 使用第一個表格的標頭作為列名

# 保存為 Excel 文件
output_excel = r'C:\Users\steve\Desktop\intern_practice\DRMDB\data\output_tables_combined.xlsx'
df.to_excel(output_excel, index=False)
print(f"Successfully saved combined table to {output_excel}")



#特殊符號讀取xml 大於等於
