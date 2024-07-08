from docx import Document
import pandas as pd

input_path = r'C:\Users\steve\Desktop\intern_practice\DRMDB\data\only_table.docx'#r'C:\Users\steve\Desktop\intern_practice\DRMDB\data\論文.docx'
document = Document(input_path)
output_path = r'C:\Users\steve\Desktop\intern_practice\DRMDB\data\table.docx'
save_tables = []
for table in document.tables:
    target_header = ['構成要件\n罪名', '身分', '手段要件', '結果要件', '主觀要件']
    #判斷式
    first_row = [cell.text.strip() for cell in table.rows[0].cells]
    if first_row == target_header:
        save_tables.append(table)

# 将表格数据转换为 DataFrame
dfs = []
for table in save_tables:
    data = []
    for row in table.rows:
        row_data = [cell.text.strip() for cell in row.cells]
        data.append(row_data)
    df = pd.DataFrame(data[1:], columns=data[0])  # 假设第一行是表头
    # df.set_index(data[0][0], inplace=True)  # 将第一列设置为索引
    df['section'] = [0] * len(data[1:])

    dfs.append(df)

for i in range(len(dfs)):
    if i == 0:
        temp_df = dfs[0]
    else:
        temp_df = pd.concat([temp_df,dfs[i]], ignore_index=True)

# order = ['section','構成要件\n罪名', '身分', '手段要件', '結果要件', '主觀要件']
temp_df = temp_df[['section','構成要件\n罪名', '身分', '手段要件', '結果要件', '主觀要件']]


temp_df.to_excel('out.xlsx', index=False)
temp_df.to_csv('out.csv', index=False,  encoding='utf_8_sig')
print(temp_df)