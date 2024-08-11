# 使用 BeautifulSoup 解析 HTML
soup = BeautifulSoup(html_content, 'html.parser')

# 存儲最終結果的列表
chapters = []
current_chapter = []

# 迭代所有的元素，查找章節標題和文本內容
for element in soup.find_all(True):  # True 會找到所有標籤
    if element.name in ['h1', 'h2']:
        # 遇到新章節標題時，開始一個新章節
        if current_chapter:
            chapters.append('\n'.join(current_chapter))
            current_chapter = []
        current_chapter.append(element.get_text(strip=True))
    elif element.name == 'br':
        # 處理換行符
        current_chapter.append('\n')
    elif element.name in ['ul', 'ol']:
        # 處理列表
        list_items = [li.get_text(strip=True) for li in element.find_all('li')]
        current_chapter.append('\n'.join(list_items))
    elif element.name == 'table':
        # 處理表格
        rows = element.find_all('tr')
        table_md = []
        for i, row in enumerate(rows):
            cells = row.find_all(['td', 'th'])
            cell_texts = [cell.get_text(strip=True) for cell in cells]
            table_md.append('| ' + ' | '.join(cell_texts) + ' |')
            # 添加表頭與內容的分隔行
            if i == 0:
                table_md.append('| ' + ' | '.join(['---'] * len(cell_texts)) + ' |')
        current_chapter.append('\n'.join(table_md))
    else:
        # 處理其他段落或文本內容
        current_chapter.append(element.get_text(strip=True))

# 添加最後一個章節
if current_chapter:
    chapters.append('\n'.join(current_chapter))

# 輸出結果
for i, chapter in enumerate(chapters, 1):
    print(f"Chapter {i}:\n{chapter}\n{'='*20}\n")

#============================================================================================
# 使用 BeautifulSoup 解析 HTML
soup = BeautifulSoup(html_content, 'html.parser')

# 選擇章節分割的標題層級
chapter_split_level = 'h2'

# 存儲最終結果的列表
chapters = []
current_chapter = []

# 迭代所有的元素，查找章節標題和文本內容
for element in soup.find_all(True):
    if element.name == chapter_split_level:
        # 遇到新的分割標題，開始一個新章節
        if current_chapter:
            chapters.append('\n'.join(current_chapter))
            current_chapter = []
        current_chapter.append(element.get_text(strip=True))
    elif element.name.startswith('h') and element.name != chapter_split_level:
        # 處理其他標題層級，視作段落斷點
        current_chapter.append('\n' + element.get_text(strip=True) + '\n')
    elif element.name == 'br':
        # 處理換行符
        current_chapter.append('\n')
    elif element.name in ['ul', 'ol']:
        # 處理列表
        list_items = [li.get_text(strip=True) for li in element.find_all('li')]
        current_chapter.append('\n'.join(list_items))
    elif element.name == 'table':
        # 處理表格
        rows = element.find_all('tr')
        table_md = []
        for i, row in enumerate(rows):
            cells = row.find_all(['td', 'th'])
            cell_texts = [cell.get_text(strip=True) for cell in cells]
            table_md.append('| ' + ' | '.join(cell_texts) + ' |')
            if i == 0:
                table_md.append('| ' + ' | '.join(['---'] * len(cell_texts)) + ' |')
        current_chapter.append('\n'.join(table_md))
    else:
        # 處理其他段落或文本內容
        current_chapter.append(element.get_text(strip=True))

# 添加最後一個章節
if current_chapter:
    chapters.append('\n'.join(current_chapter))

# 輸出結果
for i, chapter in enumerate(chapters, 1):
    print(f"Chapter {i}:\n{chapter}\n{'='*20}\n")

#===================================================================================
elif element.name == 'table':
    rows = element.find_all('tr')
    table_md = []
    colspans = []  # 用來儲存 colspan 信息
    for i, row in enumerate(rows):
        cells = row.find_all(['td', 'th'])
         #===========
        # 檢查並過濾完全空白的行
        if all(cell.get_text(strip=True) == '' for cell in cells):
            continue
         #===========  
        cell_texts = []
        for j, cell in enumerate(cells):
            # 替換換行符並保留 <br> 標籤
            text = cell.get_text(separator="<br>").replace('\n', ' ')
            #===========
            # 如果單元格為空，插入一個空白字符以保留結構
            if not text:
                text = " "
            #============
            cell_texts.append(text)
            
            # 檢查 colspan 和 rowspan
            colspan = int(cell.get('colspan', 1))
            rowspan = int(cell.get('rowspan', 1))
            
            if colspan > 1:
                colspans.append((j, colspan - 1))
            if rowspan > 1:
                for k in range(1, rowspan):
                    if i + k < len(rows):
                        if len(colspans) <= j:
                            colspans.append((j, 0))
                        colspans[j] = (j, colspans[j][1] + colspan - 1)

        # 處理行內的 colspan
        for index, span in reversed(colspans):
            if span > 0:
                cell_texts.insert(index + 1, ' ' * span)
            colspans[index] = (index, span - 1)
        # 保留那些包含部分空白的列
        if any(cell_texts):  # 如果這一行中有任何單元格非空，保留整行
            table_md.append('| ' + ' | '.join(cell_texts) + ' |')
        # table_md.append('| ' + ' | '.join(cell_texts) + ' |')
        
        # 添加表頭與內容的分隔行
        if i == 0:
            table_md.append('| ' + ' | '.join(['---'] * len(cell_texts)) + ' |')

    current_chapter.append('\n'.join(table_md))



elif element.name in ['ul', 'ol']:
    # 處理列表
    list_type = element.get('type', 'disc')  # 默認為 'disc'，如果沒有設定 'type'
    list_items = []

    for i, li in enumerate(element.find_all('li'), start=1):
        item_text = li.get_text(strip=True)
        
        if list_type == '1':
            # 有序列表，使用數字標記
            list_items.append(f"{i}. {item_text}")
        elif list_type == 'disc':
            # 無序列表，使用黑點標記
            list_items.append(f"• {item_text}")
        else:
            # 處理其他可能的情況（例如 circle, square 等）
            list_items.append(f"- {item_text}")

    current_chapter.append('\n'.join(list_items))
