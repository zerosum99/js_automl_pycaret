
class SearchMeta :
    def __init__(self,schema) :
        self.schema = schema
        self._createEnSchema()
        self._createKrSchema()
     
    def _createEnSchema(self) :
        self.edd = {k:v for k,v in zip(self.schema['LoanStatNew'].values,self.schema['korean_name'].values)} 

    def _createKrSchema(self) :
        self.kdd = {k:v for k,v in zip(self.schema['korean_name'].values,self.schema['LoanStatNew'].values)} 

    def searchEnMeta(self,key) :
        return self.edd.get(key) 

    def searchEnMetaAll(self,keys) :
        return [ self.edd.get(key) for key in keys] 

    def searchKrMeta(self,key) :
        return self.kdd.get(key) 

    def searchKrMetaAll(self,keys) :
        return [ self.kdd.get(key) for key in keys] 

    def searchLable(self,lable) :
        return self.schema[self.schema['Label'] == lable]
