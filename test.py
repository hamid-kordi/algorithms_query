class person:
    def __init__(self,name):
        self._name =  name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        if not isinstance(value,str):
            raise ValueError('zer nazan')
        self._name = value
    
    @name.deleter
    def name(self):
        self._name = None

obj = person('salam')
print(obj.name)
del obj.name
print(obj.name)

    