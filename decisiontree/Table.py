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