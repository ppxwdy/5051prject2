import pandas as pd
from collections import Counter


class processor:

    def __init__(self, file):
        self.file = file
        self.col_names = self.file.columns.values.tolist()
        self.rows, self.cols = self.file.shape

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

    def check_in(self, col, data):
        target_col = list(self.file[col].unique())

        if not isinstance(target_col[0], str):
            for i in range(len(target_col)):
                target_col[i] = str(target_col[i])

        target_col = set(target_col)

        if data not in target_col:

            return False
        else:
            return True

    def check(self, targets):

        temp_lines = []

        for i in range(len(self.col_names) - 1):
            col = self.col_names[i]
            tar = targets[i]

            if tar != '':
                if not self.check_in(col, tar):
                    return ['No record. Please check your input or search something else.']
                if i == 0:
                    for row in range(self.rows):
                        if str(self.file[col].iloc[row]) == tar:
                            temp_lines.append(row)
                else:
                    row = 0
                    while row < len(temp_lines):
                        if str(self.file[col].iloc[i]) != tar:
                            temp_lines.pop(row)
                        else: row += 1

        if len(temp_lines) == 0:
            return ['No record. Please check your input or search something else.']
        dfs = []
        for l in temp_lines:
            s = self.file.iloc[l].values.reshape(1, self.cols)
            dfs.append(pd.DataFrame(s, columns=self.col_names))

        rtn = pd.concat(dfs, ignore_index=True)
        # rtn.columns = self.col_names
        # print(self.file.iloc[temp_lines[0]].values.reshape(1, self.cols))
        print(rtn.head().to_string())
        return rtn
