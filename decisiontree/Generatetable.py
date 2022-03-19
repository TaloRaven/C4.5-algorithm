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


class Atributes():
    def __init__(self, table):
        self.table=table
    def table_to_atributes(self):
        atributes=[[]for _ in range(len(self.table[0]))]
        [[atributes[x].append(j[x]) for x in range(len(self.table[0]))]for i,j in enumerate(self.table)]
        return atributes


class Num_atributes(Atributes):
    def __init__(self, table):
        super().__init__(table)

    def num_of_atributes(self)-> list:
        atributes=self.table_to_atributes()
        num_of_atributes = [len(set(atributes[x])) for x in range(len(self.table[0]))]
        return  num_of_atributes



class Entropy():
    def __init__(self,table):
       self.table=table

    def table_to_atributes(self):
        atributes=[[]for x in range(len(self.table[0]))]
        [[atributes[x].append(j[x]) for x in range(len(self.table[0]))]for i,j in enumerate(self.table)]
        return atributes

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

    def entropy(self)->float:
        return sum([-(math.log2(i)*i) for i in self.probability()[-1]])






class Information(Entropy):
    def __init__(self, table):
        super().__init__(table)

    def num_of_atributes(self)-> list:
        atributes=self.table_to_atributes()
        num_of_atributes = [len(set(atributes[x])) for x in range(len(self.table[0]))]
        return  num_of_atributes

    def tabela(self,table=None):
        if table == None:
            table=self.table
        occurance=self.occurrences()
        atributes=[]
        for i in occurance:
            variables=[]
            for j in i:
                variables.append(j)
            atributes.append(variables)

        mini_tables_age=[]
        
        for variables in atributes:    
            for atrybut in variables:
                new_table=[]   
                for x in table:
                    if atrybut in x:
                        new_table.append(x[-1])
                    else:
                        continue
                mini_tables_age.append((new_table))
        #self.num_of_atributes()
         
        return mini_tables_age

    
