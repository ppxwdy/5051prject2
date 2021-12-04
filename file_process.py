import pandas as pd
from collections import Counter


class processor:

    def __init__(self, file):
        self.file = file

    def __sort(self, data):
        """
        sort algorithm for file
        :param data: the data waiting for sorting
        :return: sorted data
        """
        import collections

        def quick_sort(lis, start, end):
            if end > start:
                pivot = split(lis, start, end)
                quick_sort(lis, start, pivot - 1)
                quick_sort(lis, pivot + 1, end)

        def split(lis, start, end):

            pivot = lis[end]
            cur = start
            for i in range(start, end):
                if lis[i] < pivot:
                    lis[i], lis[cur] = lis[cur], lis[i]
                    cur += 1
            lis[cur], lis[end] = lis[end], lis[cur]
            return cur

        record = collections.Counter(data)
        keys = list(record.keys())

        quick_sort(keys, 0, len(keys) - 1)

        rtn = []
        for k in keys:
            rtn += [k for i in range(record[k])]

        return rtn

    def sort_file(self, file):
        """
        Sort the given data
        :param file:
        :return:
        """
        return self.__sort(file)

    def count_col_content(self, col):
        """
        count the info in the given row of the file
        :return:
        """
        data = list(self.read_column(col).values.tolist())
  
        counter = Counter(data)

        df = pd.DataFrame()
        df.insert(df.shape[1], 'Element', list(counter.keys()))
        df.insert(df.shape[1], 'Number of Element', list(counter.values()))
        return df
        

    def head(self, number_of_row):
        return self.file.head(number_of_row)

    def col_name(self):
        return [c for c in self.file.columns]

    def read_column(self, column):
        return self.file[column]

    def describe(self):
        return self.file.describe()
