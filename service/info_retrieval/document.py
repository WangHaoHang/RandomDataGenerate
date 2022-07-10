class Document(object):
    '''Document 结构体
    :param object: _description_
    :type object: _type_
    '''
    
    def __init__(self) -> None:
        self.doc_id = 0
        self.doc_words = []
    
    def set_doc_id(self,doc_id):
        '''_summary_
            设置 docId
        :param doc_id: docId
        :type doc_id: int
        '''
        self.doc_id = doc_id
        
    def set_doc_words(self,doc_words):
        '''设置document结构体中存储文件字符串

        :param doc_words: 文件字符串
        :type doc_words: array[str]
        '''
        self.doc_words = doc_words
    
    def set_doc_strs(self,word_line:str):
        '''输入字符串，从而获取doc_words

        :param word_line: 文档整个字符串
        :type word_line: str
        '''
        lines = word_line.split('\n')
        for line in lines:
            words = line.split(' ')
            for word in words:
                self.doc_words.append(word.strip())
        
    def __str__(self) -> str:
        print('doc_id:',self.doc_id)
        print('doc_words:',self.doc_words)
        return ''


    
if __name__ == '__main__':
    print('Document test')
    doc = Document()
    doc.set_doc_id(0)
    doc.set_doc_strs("hello world \n my name is hang")
    print(doc)
    