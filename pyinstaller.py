import os
import sys

if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.dirname(os.path.abspath(__file__))

excel_path = os.path.join(base_path, 'data.xlsx')  # 假設文件名為data.xlsx
#================================================================================
import os

home_dir = os.path.expanduser("~")
documents_dir = os.path.join(home_dir, "Documents")
save_path = os.path.join(documents_dir, 'output.xlsx')

# 保存 Excel 文件
df.to_excel(save_path, index=False)

#==================================================================================
pyinstaller --onefile --windowed --add-data="path/to/resource;." your_script.py
