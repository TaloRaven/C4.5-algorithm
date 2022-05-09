from decisiontree.GainRatio import Gain_Ratio

class Node(Gain_Ratio):
    def __init__(self):
        super().__init__()
        self.childrens=None
        self.decision=None
        self.attribute=None
        self.value=None
    def __str__(self) -> str:
        return f'''       Value:{self.value} Atribute: {self.attribute} Childrens:  {self.childrens if self.childrens==None else [str(x) for x in self.childrens ]} decision: {self.decision} '''