from bs4 import BeautifulSoup

def extract_div_text(soup):
    texts = []

    def traverse(element):
        if element.name == 'div':
            for child in element.children:
                traverse(child)
        elif element.string:
            texts.append(element.string.strip())
        else:
            # 如果element不是div且没有直接的文本內容，則遍歷其子元素
            for child in element.children:
                traverse(child)

    traverse(soup)
    return texts

soup = BeautifulSoup(html, 'html.parser')
texts = extract_div_text(soup)

# 输出所有提取到的文本
for text in texts:
    print(text)
