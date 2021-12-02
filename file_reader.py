import pandas as pd
import matplotlib.pyplot as plt


class reader:

    def  __init__(self, file):
        self.file = file

    def to_string(self, data):
        """
        reformat the data into a list of strings
        :param data: original data
        :return: list of strings
        """
        pass


class searcher(reader):

    def __init__(self, file):
        super(searcher, self).__init__(file)

    def func1(self):
        pass


class table_reader(reader):

    def __init__(self, file):
        super(table_reader, self).__init__(file)

    def func1(self):
        pass


class plot(reader):

    def __init__(self, file):
        super(plot, self).__init__(file)

    def func1(self):
        pass