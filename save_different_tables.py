import pandas as pd
# from openpyxl.utils.dataframe import dataframe_to_rows

def classify_and_save_tables(tables, output_dir):
    # 创建一个字典来存储分类后的表格
    classified_tables = {}

    # 遍历所有表格
    for table in tables:
        # 获取表格的列名作为键
        key = tuple(table.columns)
        if key not in classified_tables:
            classified_tables[key] = []
        classified_tables[key].append(table)

    # 遍历分类后的表格并将它们保存到不同的 Excel 文件中
    for key, table_list in classified_tables.items():
        # 将表格连接在一起
        combined_table = pd.concat(table_list, ignore_index=True)
        
        # 将列名作为文件名的一部分
        filename = output_dir + f'\\{"_".join(key)}.xlsx'

        combined_table.to_excel(filename, index=False, engine='openpyxl')
        # 使用 Pandas 的 ExcelWriter 保存表格到 Excel 文件中
        # with pd.ExcelWriter(filename, engine='openpyxl') as writer:
        #     combined_table.to_excel(writer, index=False)

    print(f"Successfully saved classified tables to {output_dir}")

# 示例用法
if __name__ == "__main__":
    # 假设我们有多个 DataFrame 表格
    tables = [
        pd.DataFrame({'C': [9, 10], 'D': [11, 12]}),
        pd.DataFrame({'A': [5, 6], 'B': [7, 8]}),
        pd.DataFrame({'A': [1, 2, 'g'], 'B': [3, 4, 'r']}),
        pd.DataFrame({'C': [9, 10], 'D': [11, 12]}),
        pd.DataFrame({'': [5], 'A': ['A'], 'B': [5], 'E': [1]}),
        pd.DataFrame({'': [2, 'g'], 'A': [13, 14], 'B': [15, 16], 'E': [17, 18]})
    ]

    # 指定输出目录
    output_dir = r'C:\Users\steve\Desktop\intern_practice\DRMDB\data\only_table'

    # 调用函数
    classify_and_save_tables(tables, output_dir)





import pandas as pd
from docx import Document
import os
import numpy as np


def read_tables_from_docx(docx_path):
    doc = Document(docx_path)
    tables = []
    for table in doc.tables:
        data = []
        for row in table.rows:
            data.append([cell.text for cell in row.cells])
        tables.append(pd.DataFrame(data))
    return tables

def classify_and_save_tables(tables, output_dir):
    classified_tables = {}

    for table in tables:
        key = (table.shape[1], tuple(table.iloc[0]))  # Use number of columns and first row as key
        if key not in classified_tables:
            classified_tables[key] = []
        classified_tables[key].append(table)
    
    for key, table_list in classified_tables.items():
        num_columns, first_row = key
        print(key,len(table_list))
        print('^^^^^^^')
        filename = os.path.join(output_dir, f'tables_{num_columns}_columns.xlsx')
        
        with pd.ExcelWriter(filename, engine='openpyxl') as writer:
            print('__________')
        #     print(table)
        #     print('__________')
            for i, table in enumerate(table_list):
                table.to_excel(writer, index=False, header=False, sheet_name=f'Table_{first_row,i}')

input_dir = r'C:\Users\ccc55\Desktop\瑞\source2.docx'
output_dir = 'path_to_save_excel_files'
os.makedirs(output_dir, exist_ok=True)

all_tables = []

tables = read_tables_from_docx(input_dir)
all_tables.extend(tables)

classify_and_save_tables(all_tables, output_dir)


