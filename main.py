from telnetlib import GA
from tkinter import E

from decisiontree.Table import Table
from decisiontree.GainRatio import Gain_Ratio
from decisiontree.Node import Node
from functions import *
import os
cwd=os.getcwd()

def txt_to_tables(txt_name):
    table = []
    with open('{}/data/{}'.format(cwd,txt_name), 'r') as f:
        [table.append(list(map(str, line.strip().split(',')))) for line in f]
    f.close()
    return table

def main():
    '''
    data
    testowaTabDec.txt', 'test.txt', 'test2.txt', gielda.txt, gieldaLiczby.txt ,beast-cancer.txt,
     breast-cancer.DATA'''

    ## Load data
    FILE_NAME='breast-cancer.DATA'
    # FILE_NAME = 'gielda.txt'
    # FILE_NAME = 'test2.txt'
    # FILE_NAME='testowaTabDec.txt'

    rows=txt_to_tables(FILE_NAME)
    # print(len(rows)/2)
    # rows=rows[:int(len(rows)/2)]
    print('\nTABLE: ',FILE_NAME,'\n')
    [print(x) for x in rows]

    ## Root_node  init split
    root_node=Node()
    root_node.table=rows
    root_node.childrens,atribut_index, max_gain=split_node_to_childrens(root_node)
    root_node.childrens=make_decision_for_nodes(root_node,atribut_index, max_gain)
    root_node.attribute=atribut_index

    # Rest node splits
    root_node=get_node(root_node)

    # Print output
    # [print(x) for x in root_node.childrens]
    print('\nTREE: ',FILE_NAME,'\n')
    showtree(root_node,0)

if __name__ == "__main__":
    main()