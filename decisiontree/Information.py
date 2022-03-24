import math
from decisiontree.TableOperations import TableOperations

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