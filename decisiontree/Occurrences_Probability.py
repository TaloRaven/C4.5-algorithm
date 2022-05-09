class TableOperations():
    def __init__(self) -> None:
        pass

    @property
    def table(self):
        return self._table
    @table.setter
    def table(self, table: list):
        self._table=table
    
    def table_to_atributes(self):
        atributes=[[]for _ in range(len(self._table[0]))]
        [[atributes[x].append(j[x]) for x in range(len(self._table[0]))]for i,j in enumerate(self._table)]
        return atributes

    def num_of_atributes(self)-> list:
        atributes=self.table_to_atributes()
        num_of_atributes = [len(set(atributes[x])) for x in range(len(self.table[0]))]
        return  num_of_atributes

    def table_to_decisions(self)->list:
        return [i[-1] for i in self.table]

    def occurrences(self)->list:
        occurrences=[]
        for x in self.table_to_atributes():
            a_dict={}
            for item in x:
                if item not in a_dict:
                    a_dict[item] = 1
                else:
                    a_dict[item] +=1
            occurrences.append(a_dict)
        return occurrences

    def probability(self)->list:
        probability=[]
        for d in self.occurrences():
            p=[]
            [p.append(d[x]/sum(d.values())) for x in d]
            probability.append(p)
        return probability





