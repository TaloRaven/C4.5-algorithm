from tkinter import E
import decisiontree
from decisiontree.Generatetable import Table, Entropy, Information, Atributes

FILE_NAME='gielda'



if __name__ == "__main__":
    # print(Generatetable(FILE_NAME).occurrences())
    # print(Generatetable(FILE_NAME).num_of_atributes())
    # print(Generatetable(FILE_NAME).probability())
    # print(Generatetable(FILE_NAME).entropy())
    #print(type(Generatetable(FILE_NAME)))
    t1=Table(FILE_NAME).txt_to_tables()
    # print(Entropy(t1).table_to_atributes())
    #print(Entropy(t1).entropy())
    inf1=Information(t1).tabela()
    # atr=Atributes(t1).table_to_atributes()

    print(inf1)
    # print(atr)