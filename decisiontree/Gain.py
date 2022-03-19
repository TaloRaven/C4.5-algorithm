
from decisiontree.Entropy import Entropy
from decisiontree.Information import Information

class Gain(Entropy, Information):
    def __init__(self):
        super().__init__()
    
    def gain(self):
        return  [self.entropy() - an for an in self.info()]