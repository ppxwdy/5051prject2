import pandas as pd
import matplotlib.pyplot as plt
import file_process


filename = ''
file = pd.read_csv(filename)
fp = file_process(file)

class reader:

    def __init__(self, file, fp):
        self.file = file
        self.fp = fp

    def to_string(self, data):
        """
        reformat the data into a list of strings
        :param data: original data
        :return: list of strings
        """
        fp.count()
        pass


class searcher(reader):

    def __init__(self, file, fp):
        super(searcher, self).__init__(file, fp)

    def func1(self):
        pass


class table_reader(reader):

    def __init__(self, file, fp):
        """
        :param file:
        """
        super(table_reader, self).__init__(file, fp)

    def func1(self):
        pass


class plot(reader):

    def __init__(self, file, fp):
        super(plot, self).__init__(file, fp)

    def func1(self):
        pass