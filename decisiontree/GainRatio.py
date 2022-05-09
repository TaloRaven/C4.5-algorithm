
from decisiontree.Occurrences_Probability import TableOperations
from decisiontree.Gain import Gain
from decisiontree.SplitInfo import SplitInfo

class Gain_Ratio(Gain, SplitInfo,TableOperations):
    def __init__(self):
        super().__init__()
        self.childrens=None
        self.decision=None
    
    def gainratio(self):
        split_info=[]
        for gain, splitinfo in zip(self.gain(), self.splitinfo()):
            try:
                split_info.append(gain / splitinfo)
            except:
                split_info.append(0)
        return split_info
