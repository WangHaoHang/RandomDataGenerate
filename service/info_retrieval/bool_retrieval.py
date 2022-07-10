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

    def input_doc(self, *docs:(Document)):
        self.doc_ids_len = len(docs)
        self.init_value_size = int((self.doc_ids_len - 1) / self.int_len) + 1
        for doc in docs:
            pass
    
    def __init_value(self):
        '''_summary_

        :return: _description_
        :rtype: _type_
        '''
        return [0 for i in range(self.init_value_size)]
        
    
    def __get_value_index(self, doc_index):
        '''_summary_

        :param doc_index: _description_
        :type doc_index: _type_
        :return: _description_
        :rtype: _type_
        '''
        arr_index = int(doc_index / self.int_len) + 1
        bit_index = int(doc_index % self.int_len) + 1
        return arr_index,bit_index
    
if __name__ == '__main__':
    a = 0x1
    print(a<<2)
    