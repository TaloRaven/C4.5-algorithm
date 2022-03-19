import math
from decisiontree.TableOperations import TableOperations


class Entropy(TableOperations):
    def __init__(self):
        super().__init__()

    def entropy(self)->float:
        return sum([-(math.log2(i)*i) for i in self.probability()[-1]])