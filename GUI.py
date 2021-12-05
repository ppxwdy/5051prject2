import tkinter as tk
from tkinter import Button
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk
import numpy as np
from file_process import *
from file_reader import *


back_button_w = 10
func_button_w = 15
clear_button_w = 10



class frame:

    def __init__(self, root):
        self.root = root
        self.col_name = ['VehicleType', 'DerectionTime_O', 'GantryID_O', 'DerectionTime_D', 'GantryID_D'
                , 'TripLength', 'TripEnd', 'TripInformation']

class window:

    def __init__(self, root):
        self.root = root
        self.root.config()
        self.root.title('File Read System')
        self.root.geometry('800x600')

        initface(self.root)


class initface(frame):

    def __init__(self, root):
        super(initface, self).__init__(root)
        self.root.config()  # bg
        # 基准界面initface
        self.initface = tk.Frame(self.root)

        table_b = Button(self.initface, text='Show tables', width=func_button_w, command=self.table_)  # , bg='red')
        table_b.place(x=310, y=230, anchor='w')

        plot_b = Button(self.initface, text='Show plots', width=func_button_w, command=self.plot_)  # , bg='red')
        plot_b.place(x=310, y=260, anchor='w')

        search_b = Button(self.initface, text='Search', width=func_button_w, command=self.search_)
        search_b.place(x=310, y=290, anchor='w')

        self.initface.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
        # self.initface.config(background='green')

    def table_(self):
        self.initface.destroy()
        table(self.root)

    def plot_(self):
        self.initface.destroy()
        plot(self.root)

    def search_(self):
        self.initface.destroy()
        search(self.root)


class table(frame):

    def __init__(self, root):
        super(table, self).__init__(root)
        self.table = tk.Frame(self.root)

        self.label_x = 150
        self.label_y = 50
        self.label_dy = 30
        self.labels = []

        self.text = None
        self.bar_v = None
        self.bar_h = None

        back_main = Button(self.table, text='back', width=back_button_w, command=self.back)
        back_main.place(x=0, y=30, anchor='w')

        clear = Button(self.table, text='clear', width=clear_button_w, command=self.clear)  # , bg='red')
        clear.place(x=650, y=530, anchor='w')

        func1 = Button(self.table, text='func1', width=func_button_w, command=self.func1)  # , bg='red')
        func1.place(x=0, y=80, anchor='w')

        show_table_head = Button(self.table, text='show_table_head', width=func_button_w, command=self.show_table_head)  # , bg='red')
        show_table_head.place(x=0, y=120, anchor='w')

        describe = Button(self.table, text='describe', width=func_button_w, command=self.describe)  # , bg='red')
        describe.place(x=0, y=160, anchor='w')

        self.table.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
        # self.table.config(background='blue')

    def back(self):
        self.table.destroy()
        initface(self.root)

    def clear(self):
        for i in range(len(self.labels)):
            self.labels.pop().destroy()

        if self.text is not None:
            self.text.destroy()
        if self.text is not None:
            self.bar_v.destroy()
        if self.text is not None:
            self.bar_h.destroy()


    def func1(self):
        self.clear()

    def show_table_head(self):
        self.clear()

    def describe(self):
        self.clear()


def drawfig():
    pass


class plot(frame):

    def __init__(self, root):
        super(plot, self).__init__(root)
        self.plot = tk.Frame(self.root)

        self.canvas = None  # 创建一块显示图形的画布
        self.clear = None
        self.toolbar = None

        back_main = Button(self.plot, text='back', width=back_button_w, command=self.back)
        back_main.place(x=0, y=30, anchor='w')

        plot1 = Button(self.plot, text='plot1', width=func_button_w, command=self.draw)  # , bg='red')
        plot1.place(x=0, y=70, anchor='w')

        self.plot.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
        # self.plot.config(background='orange')

    def back(self):
        self.plot.destroy()
        initface(self.root)

    def draw(self):
        # fig = drawfig()
        self.canvas = FigureCanvasTkAgg(drawfig(), self.plot)
        self.canvas.draw()
        self.canvas.get_tk_widget()  # .pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        # 显示工具条控件
        # self.toolbar = NavigationToolbar2Tk(self.canvas, self.plot)
        # self.toolbar.update()

        self.clear = Button(self.plot, text='clear', width=clear_button_w, command=self.clear_plot)
        self.clear.place(x=650, y=570, anchor='w')

        self.canvas.get_tk_widget().pack()

    def clear_plot(self):
        # for item in self.canvas.get_tk_widget().find_all():
        #     self.canvas.get_tk_widget().delete(item)
        self.canvas.get_tk_widget().pack_forget()
        self.clear.destroy()


class search(frame):

    def __init__(self, root):
        super(search, self).__init__(root)
        self.search = tk.Frame(self.root)

        self.labels = []

        clear_b = Button(self.search, text='Clear', width=clear_button_w, command=self.clear)
        clear_b.place(x=650, y=570, anchor='w')

        back_b = Button(self.search, text='Back', width=back_button_w, command=self.back)
        back_b.place(x=0, y=30, anchor='w')

        self.col_name_intro = tk.Label(self.search, text='Which column do you want to search?')
        self.col_name_intro.place(x=300, y=200, anchor='w')
        self.col_name = tk.StringVar()
        self.col_name_entry = tk.Entry(self.search, width=func_button_w, textvariable=self.col_name)
        self.col_name_entry.place(x=300, y=230, anchor='w')

        self.target_intro = tk.Label(self.search, text='What do you want to search?')
        self.target_intro.place(x=300, y=260, anchor='w')
        self.target = tk.StringVar()
        self.target_entry = tk.Entry(self.search, width=func_button_w, textvariable=self.target)
        self.target_entry.place(x=300, y=290, anchor='w')

        self.search_b = Button(self.search, text='Search', width=func_button_w, command=self.search_)
        self.search_b.place(x=350, y=320)

        self.search.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

    def clear(self):
        for i in range(len(self.labels)):
            self.labels.pop().destroy()
        self.col_name_intro = tk.Label(self.search, text='Which column do you want to search?')
        self.col_name_intro.place(x=300, y=200, anchor='w')
        self.col_name = tk.StringVar()
        self.col_name_entry = tk.Entry(self.search, width=func_button_w, textvariable=self.col_name)
        self.col_name_entry.place(x=300, y=230, anchor='w')

        self.target_intro = tk.Label(self.search, text='What do you want to search?')
        self.target_intro.place(x=300, y=260, anchor='w')
        self.target = tk.StringVar()
        self.target_entry = tk.Entry(self.search, width=func_button_w, textvariable=self.target)
        self.target_entry.place(x=300, y=290, anchor='w')

        self.search_b = Button(self.search, text='Search', width=func_button_w, command=self.search_)
        self.search_b.place(x=350, y=320)

    def back(self):
        self.search.destroy()
        initface(self.root)

    def search_(self):
        self.col_name_intro.destroy()
        self.col_name_entry.destroy()

        self.target_intro.destroy()
        self.target_entry.destroy()
        self.search_b.destroy()

        label0 = tk.Label(self.search, text=f'The results for {self.target.get()} in column {self.col_name.get()} are as follows:')
        label0.pack()
        self.labels.append(label0)


if __name__ == '__main__':
    
    file = pd.read_csv('TDCS_M06A_20190830_080000.csv')
    # file.columns = [str(i) for i in range(file.shape[1])] 
    col_name = ['VehicleType', 'DerectionTime_O', 'GantryID_O', 'DerectionTime_D', 'GantryID_D'
                , 'TripLength', 'TripEnd', 'TripInformation']
    file.columns = col_name
    
    
    
    
    
    root = tk.Tk()
    window(root)
    root.mainloop()
