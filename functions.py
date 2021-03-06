from telnetlib import GA
from tkinter import E

from decisiontree.Table import Table
from decisiontree.GainRatio import Gain_Ratio
from decisiontree.Node import Node


def split_node_to_childrens(node: Node):

    gain_ratio=node.gainratio()
    rows=node.table
    max_value = max(gain_ratio)
    max_index = gain_ratio.index(max_value)

    uniq_rows=[row[max_index] for row in rows]
    new_uniq_rows=[]
    for element in uniq_rows:
        if element not in new_uniq_rows:
            new_uniq_rows.append(element)

    # uniq_rows = list(set([row[max_index] for row in rows]))
    uniq_rows=new_uniq_rows

    next_floor = []
    for element in uniq_rows:
        new_branch = []
        for row in rows:
            if row[max_index] == element:
                new_branch.append(row)

        next_floor.append(new_branch)

    return next_floor, max_index ,max_value

def make_decision_for_nodes(node: Node, atribut_index, max_gain):

    new_nodes=[]
    for index, children_rows in enumerate(node.childrens):
        new_node = Node()
        new_node.table = children_rows
        decisions=[row[-1] for row in children_rows]
        if max_gain ==0:
            new_node.decision=decisions[0]
            # print(children_rows)

            new_node.value=children_rows[0][atribut_index]

            # print(atribut_index)
            new_nodes.append(new_node)
        else:
            new_node.attribute= atribut_index
            new_node.value = children_rows[0][atribut_index]
            # print(new_node.attribute)
            new_nodes.append(new_node)
            #TODO set atribut to n number for this node
            # fix atronute count

    return new_nodes


def get_node(node):
    new_children_node=[]
    node.childrens,atribut_index, max_gain=split_node_to_childrens(node)
    node.childrens=make_decision_for_nodes(node,atribut_index,max_gain)
    node.attribute=atribut_index


    for index, children_node in enumerate(node.childrens):
        if children_node.decision is None:
            children_node.childrens,atribut_index, max_gain=split_node_to_childrens(children_node)
            children_node.childrens = make_decision_for_nodes(children_node,atribut_index, max_gain)
            node.childrens[index]=get_node(children_node)
            # new_children_node.append(children_node)
        else:
            new_children_node.append(children_node)
    # node.childrens=new_children_node
    return node

def showtree(node: Node,przesuniecie):
    if node.attribute!=None:
        print(" "*przesuniecie,end="")
        if node.decision:
            print(node.decision,end=" -> ")
        if node.value:
            print(node.value,"->","Atrybut",node.attribute)
        if node.value==None:
            print("Atrybut", node.attribute)
        for p in node.childrens:
            showtree(p,przesuniecie+7)
    else:
        print(" "*przesuniecie,end="")
        print(node.value, "->" ,node.decision)
