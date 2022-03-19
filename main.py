from telnetlib import GA
from tkinter import E

from decisiontree.Table import Table
from decisiontree.GainRatio import GainRatio

def main():
    files='testowaTabDec', 'test', 'test2', 'gielda', 'gieldaLiczby'
    FILE_NAME='testowaTabDec'
    t1=Table(FILE_NAME).txt_to_tables()
    gratio=GainRatio()
    gratio.table=t1
    print(gratio.gainratio())

if __name__ == "__main__":
    main()