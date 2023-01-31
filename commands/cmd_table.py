from prettytable import PrettyTable


class CLITable:
    def __init__(self,table_column_name:list):
        self.table = PrettyTable()
        self.table.field_names = table_column_name

   
    def add_data(self, value_list:list):
        self.table.add_rows(value_list)

    def print_all(self):
        return self.table