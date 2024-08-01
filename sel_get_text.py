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
