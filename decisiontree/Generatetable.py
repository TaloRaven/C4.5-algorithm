import math


class Table():
    def __init__(self,txt_name):
        self.txt_name=txt_name

    def txt_to_tables(self):
        table = []
        with open('./data/{}.txt'.format(self.txt_name), 'r') as f:
            [table.append(list(map(str,line.strip().split(',')))) for line in f]
        f.close()
        return table

    def __str__(self) -> str:
        return f'{self.txt_to_tables()}'

class TableOperations():
    def __init__(self) -> None:
        self._table=0
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

    def __str__(self) -> str:
        return f'''
        Table of decisions: {self.table_to_decisions()}\n
        Table of atributes: {self.table_to_atributes()}\n
        Number of variables for atributes: {self.num_of_atributes()}\n
        Occurrences: {self.occurrences()}\n
        Propability: {self.probability()}
        '''


class Entropy(TableOperations):
    def __init__(self):
        super().__init__()

    def entropy(self)->float:
        return sum([-(math.log2(i)*i) for i in self.probability()[-1]])

class Information(TableOperations):
    def __init__(self):
        super().__init__()

    def tabela(self):
        atributes=[]
        for i in self.occurrences():
            atribut=[]
            for j in i:
                atribut.append(j)
            atributes.append(atribut)

        # print(atributes)
        mini_tables_age=[]
        for i, x in enumerate(atributes):
            for j in x:
                new_table=[] 
                for y in self._table:
                    
                    if j == y[i]:
                        new_table.append(y[-1])
                    else:
                        continue
                mini_tables_age.append((new_table))   
        return mini_tables_age

    def info(self):
        occurrences=[]

        for x in self.tabela():
            a_dict={}
            for item in x:
                if item not in a_dict:
                    a_dict[item] = 1
                else:
                    a_dict[item] +=1
            occurrences.append(a_dict)

        probs=[]
        for d in occurrences:
            p=[]
            [p.append(d[x]/sum(d.values())) for x in d]
            probs.append(p)

        entropies = [sum(x) for x in [[-(math.log2(j)*j)for j in i ]for i in probs]]

        i = 0
        entropies_grouped = []
        for l in self.num_of_atributes():
            entropies_grouped.append(entropies[i:i+l])
            i += l

        informations=[]
        for i in range(len(entropies_grouped)):
            info = [x*y for x,y in zip(self.probability()[i],entropies_grouped[i])]
            informations.append(sum(info))
        informations=informations[:-1]

        return informations  
         
    def __str__(self) -> str:
        return  f'''Information for an: {self.info()}
                    
                     '''   

    
