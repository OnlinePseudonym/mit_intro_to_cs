class myDict(object):
    """ Implements a dictionary without using a dictionary """
    def __init__(self):
        self.keys = []
        self.values = []
        
    def assign(self, k, v):
        """ k (the key) and v (the value), immutable objects  """
        if k not in self.keys:
            self.keys.append(k)
            self.values.append(v)
        else:
            self.values[self.keys.index(k)] = v
        
    def getval(self, k):
        """ k, immutable object  """
        if k not in self.keys:
            raise KeyError         
        return self.values[self.keys.index(k)]
        
    def delete(self, k):
        """ k, immutable object """
        if k not in self.keys:
            raise KeyError   
        index = self.keys.index(k)
        del self.keys[index]
        del self.values[index]