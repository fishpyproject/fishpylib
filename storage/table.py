class Table:
  #TODO: class docstring
  
    def __init__(self, data = None):
      #TODO: initializer method docstring
        if data == None:
            self._data = {}
        else:
            #TODO: type(data) validation
            self._data = data
        self._hiden = {}
