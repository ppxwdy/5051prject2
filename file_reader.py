import pandas as pd
import matplotlib.pyplot as plt
from file_process import *
from collections import Counter

filename = ''
file = pd.read_csv(filename)
fp = processor(file)


class reader:

    def __init__(self, fp):
        """
        :param fp: file_processor
        """
        self.fp = fp

    def to_string(self, data):
        """
        reformat the data into a list of strings
        :param data: original data (dataframe)
        :return: list of strings
        """
        rtn = []
        split_d = data.to_srting().split('\n')
        for d in split_d:
            rtn.append(d+'\n')
        return rtn


class searcher(reader):

    def __init__(self, fp):
        super(searcher, self).__init__(fp)

    def func1(self):
        pass


class table_reader(reader):

    def __init__(self, fp):
        super(table_reader, self).__init__(fp)

    def describe_file(self):
        file_info = self.fp.describe()
        return self.to_string(file_info)

    def sort_column(self, column):
        col_content = self.fp.read_column(column).to_list()
        sorted_col = self.fp.sort_file(col_content)
        return sorted_col

    def show_rows(self, number_of_row):
        data = self.fp.head(number_of_row)
        return self.to_string(data)

    def show_col_content(self, column):
        data = list(set(self.fp.read_column(column).values.tolist()))
        rtn = []
        for d in data:
            rtn.append(str(d)+'\n')
        return rtn

    def count_info(self,column):
        data = list(set(self.fp.read_column(column).values.tolist()))
        counter = Counter(data)
        df = pd.DataFrame()
        df.insert(df.shape[1], 'Element', list(counter.keys()))
        df.insert(df.shape[1], 'Number of Element', list(counter.values()))
        return self.to_string(df)


class plot(reader):

    def __init__(self, fp):
        super(plot, self).__init__(fp)
        self.fig = plt.Figure(figsize=(10, 8))

    def func1(self):
        pass
