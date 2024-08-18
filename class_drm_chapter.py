class Chapter:
    def __init__(self, chapter_level : str, chapter_name : str, parent : list, child : list, ruletable : str = None, markdowntext : str = None):
        self.chapter_level  = chapter_level
        self.chapter_name   = chapter_name
        self.parent         = parent
        self.child          = child
        self.ruletable      = ruletable #5 ruletable
        self.markdowntext   = markdowntext #cotent
        self.word_count     = len(markdowntext.strip())
        
    def Get_table(self):
        pass
    def Get_markdowntext(self):
        pass
    def Check_chapter_exist(self, chapter_name):
        pass
    
    def add_child(self, child):
        """添加子章节并设置子章节的父章节"""
        self.child.append(child)
        child.parent.append(self)
    
    def update_content(self, new_content):
        """更新章节内容，并重新计算字数"""
        self.markdowntext = new_content
        self.word_count = len(new_content.strip())
    
    def get_child_names(self):
        """获取所有子章节的名称"""
        return [child.chapter_name for child in self.child]

class DRM:
    def __init__(self, drm : str, version : str, ictype : str, icversion : str):
        self.drm        = drm
        self.version    = version
        self.ictype     = ictype
        self.icversion  = icversion
        self.chapter    = None
        pass
    def Insert_chapter(self, chapter : Chapter):
        pass
    def Get_chapter(self, chapter : Chapter):
        pass


if __name__ == "__main__":
    # filename = 'T000-DJ-DR-005_v0d5_SoIC-X-CF'
    # newdrm = DRM('T000-DJ-DR-005','v0.5','SoIC-X-CF')
    # newdrm.Insert_chapter(Chapter('0', 'Fullbook',[],[]))
    # top_chapter = newdrm.Get_chapter(Chapter)
    # wordfile = []
    # for chapter in wordfile:
    #     this_chapter = Chapter('1', 'Introduction',[],[])   # 一章一章丟
    #     top_chapter.append(this_chapter)


    # chapter1 = Chapter('0', 'Chapter 1', markdowntext = 'This is the content of chapter 1.')
    chapter1 = Chapter('0', 'Chapter 1', [], [], markdowntext = 'This is the content of chapter 1.')
    subchapter1_1 = Chapter('1', 'Subchapter 1.1', [], [], markdowntext = 'This is the content of subchapter 1.1.')
    chapter1.add_child(subchapter1_1)
    subsubchapter1_1_1 = Chapter('2', 'Sub-subchapter 1.1.1', [], [], markdowntext = 'This is the content of sub-subchapter 1.1.1.')
    subchapter1_1.add_child(subsubchapter1_1_1)

    print(f"Chapter Name: {chapter1.chapter_name}")
    print(f"Content: {chapter1.markdowntext}")
    print(f"Word Count: {chapter1.word_count}")
    print(f"Children: {chapter1.get_child_names()}")

    # 修改章节内容
    chapter1.update_content("This is the updated content of chapter 1.")
    print(f"Updated Content: {chapter1.markdowntext}")
    print(f"Updated Word Count: {chapter1.word_count}")

    for child in chapter1.child:
        print(f"Subchapter Name: {child.chapter_name}")
        print(f"Content: {child.markdowntext}")
        print(f"Word Count: {child.word_count}")
        print(f"Children: {child.get_child_names()}")

# {'Chapter 1': {'content': 'This is the content of chapter 1.', 'word_count': 7, 'level': '0', 'parent' : [], 'child' : ['subchapter 1.1']}}
