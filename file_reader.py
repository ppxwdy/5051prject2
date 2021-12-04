from os import cpu_count
from tkinter import Label
import pandas as pd
import matplotlib.pyplot as plt
from pandas.core.frame import DataFrame
from file_process import *
from collections import Counter


file = pd.read_csv('TDCS_M06A_20190830_080000.csv')
file.columns = [str(i) for i in range(file.shape[1])] 
# file.columns = ['VehicleType', 'DerectionTime_O', 'GantryID_O', 'DerectionTime_D', 'GantryID_D'
#                 , 'TripLength', 'TripEnd', 'TripInformation']
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
        if isinstance(data, pd.DataFrame):
            split_d = data.to_string().split('\n')
        else:
            split_d = data
        for d in split_d:
            rtn.append(str(d)+'\n')
        return rtn


class searcher(reader):

    def __init__(self, fp):
        super(searcher, self).__init__(fp)
        self.count_key = ['Element', 'Number of Element']

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
        return self.to_string(sorted_col)
    
    def show_col(self, column):
        return self.to_string(self.fp.read_column(column))

    def show_rows(self, number_of_row=5):
        data = self.fp.head(number_of_row)
        return self.to_string(data)

    def show_col_content(self, column):
        # data = self.fp.count_col_content(column).to_dict()
        # keys = ['Element', 'Number of Element']

        data = list(set(self.fp.read_column(column).values.tolist()))
        return self.to_string(data)

    def count_info(self, column):
        df = self.fp.count_col_content(column)
        return self.to_string(df)


class plot(reader):

    def __init__(self, fp):
        super(plot, self).__init__(fp)
        self.fig = plt.Figure(figsize=(4, 3))
        self.count_key = ['Element', 'Number of Element']
        self.p1 = self.fig.add_subplot(111)

    def pie_chart_col(self, col):
        data = self.fp.count_col_content(col).to_dict()
        # p1 = self.fig.add_subplot(111)
        
        element = list(data[self.count_key[0]].values())
        number = list(data[self.count_key[1]].values())
        
        
        max_dix = number.index(max(number))
        explode = [0 for _ in range(len(number))]
        explode[max_dix] = 0.2    
        
        self.p1.pie(number, labels=element, shadow=True, autopct='%.2f%%', explode=explode)

        return self.fig 

    def bar_char_col(self, col):
        data = self.fp.count_col_content(col).to_dict()
        # p1 = self.fig.add_subplot(111)
        
        element = list(data[self.count_key[0]].values())
        number = list(data[self.count_key[1]].values())

        x = [i for i in range(len(element))]
        self.p1.bar(x, number)

        self.p1.set_xticks(x)
        self.p1.set_xticklabels(element)
        self.p1.set_title(f'Bar plot for {col}')
        self.p1.set_xlabel('Element')
        self.p1.set_ylabel('Number')
        
        return self.fig 
    
    def line_col(self, col):
        data = self.fp.count_col_content(col).to_dict()
        # p1 = self.fig.add_subplot(111)
        
        element = list(data[self.count_key[0]].values())
        number = list(data[self.count_key[1]].values())
        x = [i for i in range(len(element))]
        
        self.p1.plot(x, number, '-o')
        
        self.p1.set_xticks(x)
        self.p1.set_xticklabels(element)
        self.p1.set_title(f'Line Chart for {col}')
        self.p1.set_xlabel('Element')
        self.p1.set_ylabel('Number')
        return self.fig 
    
    def scatter_col(self, col):
        data = self.fp.count_col_content(col).to_dict()
        # p1 = self.fig.add_subplot(111)
        
        element = list(data[self.count_key[0]].values())
        number = list(data[self.count_key[1]].values())
        
        x = [i for i in range(len(element))]
        
        self.p1.scatter(x, number)
        
        self.p1.set_xticks(x)
        self.p1.set_xticklabels(element)
        self.p1.set_title(f'Line Chart for {col}')
        self.p1.set_xlabel('Element')
        self.p1.set_ylabel('Number')
        return self.fig 

    def reset(self):
        self.fig.delaxes(self.p1)
        self.p1 = self.fig.add_subplot(111)



##############
# test 

# # table_reader test.
# tr = table_reader(fp)
# col_content = tr.show_col_content('0')
# print(col_content)
# col = tr.show_col('0')
# count_info = tr.count_info('0')
# print(count_info)
# rows = tr.show_rows(10)
# print(rows)

# di = fp.count_col_content('0').to_dict()
# keys = ['Element', 'Number of Element']
# element = list(di[keys[0]].values())
# number = list(di[keys[1]].values())
# print(element)
# print(number)



## test plot_reader

# pie
# max_dix = number.index(max(number))
# explode=[0 for _ in range(len(number))]
# explode[max_dix] = 0.2
# plt.pie(number, labels=element, shadow=True, autopct='%.2f%%', explode=explode)
# plt.show()

# bar
# x = [i for i in range(len(element))]
# plt.plot(x, number)

# plr = plot(fp)

# fig = plr.pie_chart_col('0')
# plt.show()

# print(isinstance(fp.count_col_content('0'), pd.DataFrame))