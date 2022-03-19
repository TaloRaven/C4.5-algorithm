
from decisiontree.TableOperations import TableOperations
from decisiontree.Gain import Gain
from decisiontree.SplitInfo import SplitInfo

class GainRatio(Gain, SplitInfo,TableOperations):
    def __init__(self):
        super().__init__()
    
    def gainratio(self):
            return [(gain / splitinfo) for gain, splitinfo in zip(self.gain(), self.splitinfo())]