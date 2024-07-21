import os

word_file_path = r'C:\Users\steve\Desktop\paper\knee\2021_人工智慧輔助評分\test.docx'
target_directory = os.path.dirname(word_file_path)
excel = r'\test.xlsx'
output = fr'{target_directory + excel}'
print(output)


import os

# 指定要刪除的 Excel 文件的完整路徑
# excel_file_path = r'C:\Users\steve\Desktop\paper\knee\2021_人工智慧輔助評分\excel_file.xlsx'

# 檢查文件是否存在
if os.path.exists(output):
    # 刪除文件
    os.remove(output)
    print(f"Successfully deleted {output}")
else:
    print(f"File not found: {output}")
