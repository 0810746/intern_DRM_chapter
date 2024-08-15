from bs4 import BeautifulSoup
from collections import defaultdict

def add_to_nested_dict(nested_dict, keys, content):
    """ 
    將內容添加到巢狀字典中。
    
    :param nested_dict: 巢狀字典
    :param keys: 章節標題的鍵列表
    :param content: 章節內容字串
    """
    current_level = nested_dict
    for key in keys[:-1]:
        current_level = current_level[key]["subsections"]
    
    last_key = keys[-1]
    current_level[last_key] = {
        "content": content,
        "word_count": len(content.split()),
        "subsections": {}
    }

def extract_content_by_headings(soup):
    """
    根據章節標籤抓取內容並構建巢狀字典。

    :param soup: BeautifulSoup物件
    :return: 巢狀字典
    """
    nested_dict = defaultdict(lambda: {"content": "", "word_count": 0, "subsections": {}})
    headings = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']
    
    # Track the hierarchy level
    current_hierarchy = []

    # Iterate over all heading elements
    for heading in soup.find_all(headings):
        level = int(heading.name[1])  # Get the level number (1, 2, 3, etc.)
        current_hierarchy = current_hierarchy[:level-1]  # Adjust hierarchy to the current level
        current_hierarchy.append(heading.get_text(strip=True))  # Add the current heading to the hierarchy

        # Extract content for this heading
        content = []
        for sibling in heading.find_all_next(['p', 'span', 'br'] + headings, recursive=False):
            if sibling.name in headings:
                break
            content.append(sibling.get_text(separator="\n", strip=True))

        # Add content to the nested dictionary
        add_to_nested_dict(nested_dict, current_hierarchy, "\n".join(content))

    return nested_dict

def print_nested_dict(nested_dict, indent=0):
    """
    打印巢狀字典內容。

    :param nested_dict: 巢狀字典
    :param indent: 縮排層次
    """
    for key, value in nested_dict.items():
        print(f"{' '*indent}{key}:")
        print(f"{' '*(indent+2)}Content: {value['content']}")
        print(f"{' '*(indent+2)}Word Count: {value['word_count']}")
        if value['subsections']:
            print(f"{' '*(indent+2)}Subsections:")
            print_nested_dict(value['subsections'], indent + 4)

def get_content_from_path(nested_dict, path):
    """
    從巢狀字典中根據提供的路徑提取章節內容。

    :param nested_dict: 巢狀字典
    :param path: 章節標題的路徑列表，如 ["Chapter 1", "Subsection 1.1"]
    :return: 該章節的內容字典或None如果未找到
    """
    current_level = nested_dict
    for key in path:
        if key in current_level:
            if key == path[-1]:  # 如果是最后一个key，返回内容
                return {k: v for k, v in current_level[key].items() if k != "subsections"}
            current_level = current_level[key]["subsections"]
        else:
            return None  # 如果路徑不存在，返回None

    # 如果該節點是字典，且包含 "content" 和 "word_count"，則返回它們
    return {k: v for k, v in current_level.items() if k != "subsections"}

def calculate_total_char_count(nested_dict):
    """
    計算巢狀字典中每個章節的總字元數，包括所有子章節。

    :param nested_dict: 巢狀字典
    :return: 字元總數
    """
    total_char_count = nested_dict.get("char_count", 0)
    for subsection in nested_dict.get("subsections", {}).values():
        total_char_count += calculate_total_char_count(subsection)
    return total_char_count
def generate_path(chapter_str):
    """
    根據用戶輸入的章節字符串生成路徑。

    :param chapter_str: 用戶輸入的章節字符串，如 "1.1", "2.1.2"
    :return: 生成的路徑列表
    """
    levels = chapter_str.split('.')
    path = []
    for i, level in enumerate(levels):
        if i == 0:
            path.append(f"Chapter {level}")
        else:
            path.append(f"Subsection {'.'.join(levels[:i+1])}")
    return path
    
def main(html_content, chapter_str):
    soup = BeautifulSoup(html_content, 'html.parser')
    nested_dict = extract_content_by_headings(soup)
    print_nested_dict(nested_dict)

    for k,v in nested_dict.items():
        print(k, v)
    # print(nested_dict)
    # path = ["Chapter 1", "Subsection 1.1"]
    # content = get_content_from_path(nested_dict, path)
    # if content:
    #     print("Subsection 1.1 Content:", content)
    #     print(content['content'])
    # else:
    #     print("not found")

    # path = ["Chapter 2", "Subsection 2.1", "Sub-subsection 2.1.2"]
    # content = get_content_from_path(nested_dict, path)
    # if content:
    #     print("Sub-subsection 2.1.2 Content:", content)
    #     print(content['content'])
    # else:
    #     print("Sub-subsection 2.1.2 not found.")


    # # 自动生成路径
    # path = generate_path(chapter_str)

    # # 获取特定章节的内容
    # chapter_content = get_content_from_path(nested_dict, path)
    # if chapter_content:
    #     total_char_count = calculate_total_char_count(chapter_content)
    #     print(f"Content of {chapter_str}:")
    #     print(f"Text: {chapter_content['content']}")
    #     print(f"Total Characters (including subsections): {total_char_count}")
    # else:
    #     print(f"{chapter_str} not found.")

if __name__ == "__main__":
    # 範例HTML內容
    html_content = """
    <h1>Chapter 1</h1>
    <p>This is the content of chapter 1.</p>
    <h2>Subsection 1.1</h2>
    <p>This is the content of subsection 1.1.</p>
    <h3>Sub-subsection 1.1.1</h3>
    <p>This is the content of sub-subsection 1.1.1.</p>
    <h1>Chapter 2</h1>
    <p>This is the content of chapter 2.</p>
    <h2>Subsection 2.1</h2>
    <p>This is the content of subsection 2.1.</p>
    <h3>Sub-subsection 2.1.1</h3>
    <p>This is the content of sub-subsection 2.1.1.</p>
    <h3>Sub-subsection 2.1.2</h3>
    <p>This is the content of sub-subsection 2.1.2.</p>
    <h2>Subsection 2.2</h2>
    <p>This is the content of subsection 2.2.</p>
    """

    chapter_str = '2.1'
    main(html_content, chapter_str)

    # main(html_content)
