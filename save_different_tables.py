import pandas as pd
import os

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

    # 检查输出目录是否存在，不存在则创建
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 遍历分类后的表格并将它们保存到不同的 Excel 文件中
    for key, table_list in classified_tables.items():
        # 将列名作为文件名的一部分
        filename = os.path.join(output_dir, f"tables_{'_'.join(key)}.xlsx")

        # 使用 Pandas 的 ExcelWriter 保存多个表格到一个 Excel 文件中
        with pd.ExcelWriter(filename, engine='openpyxl') as writer:
            for i, table in enumerate(table_list):
                table.to_excel(writer, sheet_name=f'Table_{i+1}', index=False)

    print(f"Successfully saved classified tables to {output_dir}")

# 示例用法
if __name__ == "__main__":
    # 假设我们有多个 DataFrame 表格
    tables = [
        pd.DataFrame({'A': [1, 2], 'B': [3, 4]}),
        pd.DataFrame({'A': [5, 6], 'B': [7, 8]}),
        pd.DataFrame({'C': [9, 10], 'D': [11, 12]}),
        pd.DataFrame({'A': [13, 14], 'B': [15, 16], 'E': [17, 18]})
    ]

    # 指定输出目录
    output_dir = r'C:\Users\steve\Desktop\intern_practice\DRMDB\data\only_table'

    # 调用函数
    classify_and_save_tables(tables, output_dir)
