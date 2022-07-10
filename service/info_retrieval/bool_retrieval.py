import logging
from reverse_index import Reverse_Index
from document import Document


class Bool_Index(Reverse_Index):
    '''布尔索引

    :param Revese_Index: _description_
    :type Revese_Index: _type_
    '''
    def __init__(self) -> None:
        super(Bool_Index,self).__init__()
        self.indexs = []
        self.index_bool_value= []
        self.doc_ids = []
        self.doc_ids_len = 0
        self.int_len = 32
        self.init_value_size = 0

    def input_doc(self, docs):
        self.doc_ids_len = len(docs)
        print(self.doc_ids_len)
        self.init_value_size = int((self.doc_ids_len - 1) / self.int_len) + 1
        doc_index = 0
        for doc in docs:
            arr_index,bit_index = self.__get_value_index(doc_index=doc_index)
            self.doc_ids.append(doc.doc_id)
            for word in doc.doc_words:
                index = 0
                if self.index_map.get(word) == None:
                    index = len(self.indexs)
                    self.index_map[word] = index
                    self.indexs.append(word)
                    self.index_bool_value.append(self.__init_value())
                else:
                    index = self.index_map.get(word)
                self.__set_value_1(index=index,arr_index=arr_index,bit_index=bit_index)
            doc_index += 1
    
    def get_docId_by_word(self,word:str):
        if self.index_map.get(word) == None:
            return None
        else:
            index = self.index_map.get(word)
            bool_value = self.index_bool_value[index]
        return self.__get_docId_by_bool_value(bool_value=bool_value)
    
    def __get_docId_by_bool_value(self,bool_value):
        index = 0
        docIdIndexs = []
        docIds = []
        for value in bool_value:
            result = self.__bit_index(value)
            for r in result:
                docIdIndexs.append(r+index)
            index += 32
        for docIdIndex in docIdIndexs:
            docIds.append(self.doc_ids[docIdIndex])
        return docIds
    
    def __bit_index(self, value):
        result = []
        for i in range(32):
            if value % 2 == 1:
                result.append(i)
            value = value >> 1
        return result
    
    def __init_value(self):
        '''_summary_

        :return: _description_
        :rtype: _type_
        '''
        return [0 for i in range(self.init_value_size)]
        
    
    def __get_value_index(self, doc_index:int):
        '''_summary_

        :param doc_index: _description_
        :type doc_index: int
        :return: _description_
        :rtype: _type_
        '''
        arr_index = int(doc_index / self.int_len) 
        bit_index = int(doc_index % self.int_len)
        return arr_index,bit_index
    
    def __set_value_1(self,index:int,arr_index:int,bit_index:int):
        flag = True
        try:
            self.index_bool_value[index][arr_index] |= 1 << (bit_index)
        except Exception as e:
            logging.error(e)
            flag = False
        return flag
        
    def __set_value_0(self,index,arr_index,bit_index):
        flag = True
        try:
            self.index_bool_value[index][arr_index] &=  ((1 << (bit_index))^0xffffffff)
        except Exception as e:
            logging.error(e)
            flag = False
        return flag
    
    def __and_value(self, *indexs):
        result = self.__init_value()
        result_len = len(result)
        for i in range(result_len):
            result[i] ^= 0xffffffff
        for index in indexs:
            for i in range(result_len):
                result[i] &= self.index_bool_value[index][i]
        return result
    
    def __or_value(self, *indexs):
        result = self.__init_value()
        result_len = len(result)
        for index in indexs:
            for i in range(result_len):
                result[i] |= self.index_bool_value[index][i]
        return result
    
        
        
if __name__ == '__main__':
    docs = []
    for i in range(33):
        doc1 = Document()
        doc1.set_doc_id(i)
        doc1.set_doc_strs("hello world"+" "+str(i))
        docs.append(doc1)
        
    # doc1 = Document()
    # doc1.set_doc_id(0)
    # doc1.set_doc_strs("hello world")
    
    # doc2 = Document()
    # doc2.set_doc_id(1)
    # doc2.set_doc_strs('world thank')
    
    bool_retri = Bool_Index()
    bool_retri.input_doc(docs)
    print('doc_ids:',bool_retri.doc_ids)
    print('indexs:',bool_retri.indexs)
    print('bool_values:',bool_retri.index_bool_value)
    print(bool_retri.get_docId_by_word('world'))
    print(bool_retri.get_docId_by_word('hello'))
    print(bool_retri.get_docId_by_word('thank'))