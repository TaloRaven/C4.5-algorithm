import math
from decisiontree.Occurrences_Probability import TableOperations

class SplitInfo(TableOperations):
    def __init__(self) -> None:
        super().__init__()

    def splitinfo(self)->float:
        return [sum([-(math.log2(i)*i)for i in element ])for element in self.probability()[0:-1]]