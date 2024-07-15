from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

# 初始化 WebDriver
driver = webdriver.Chrome()  # 確保你已經安裝了 ChromeDriver

# 打開目標網頁
url = '你的目標網址'
driver.get(url)

# 找到所有的 <tr> 元素
rows = driver.find_elements(By.TAG_NAME, 'tr')

# 初始化列表來存儲表格數據
table_data = []

# 迭代每一行
for row in rows:
    cells = row.find_elements(By.XPATH, ".//td|.//th")
    row_data = []
    for cell in cells:
        cell_text = cell.text.strip()
        rowspan = int(cell.get_attribute('rowspan') or 1)
        colspan = int(cell.get_attribute('colspan') or 1)
        for _ in range(rowspan):
            for _ in range(colspan):
                row_data.append(cell_text)
    table_data.append(row_data)

# 將數據轉換為 DataFrame
df = pd.DataFrame(table_data)

# 迭代處理合併的儲存格
for i, row in df.iterrows():
    for j, cell in enumerate(row):
        if cell != "":
            colspan = int(rows[i].find_elements(By.XPATH, ".//td|.//th")[j].get_attribute('colspan') or 1)
            rowspan = int(rows[i].find_elements(By.XPATH, ".//td|.//th")[j].get_attribute('rowspan') or 1)
            for k in range(1, colspan):
                df.iat[i, j + k] = cell
            for l in range(1, rowspan):
                df.iat[i + l, j] = cell

# 將 DataFrame 保存到 Excel 文件
output_file = 'output.xlsx'
df.to_excel(output_file, index=False, header=False)

print(f"Successfully saved table data to {output_file}")
