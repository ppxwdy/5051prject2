import tkinter as tk
from tkinter import Button
from typing import Text
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import numpy as np
from file_process import *
from file_reader import *
from functools import partial

back_button_w = 10
func_button_w = 17
other_button_w = 10

back_x, back_y = 0, 530
clear_x, clear_y = 650, 530
title_u_l_x, title_u_l_y = 20, 10


class frame:

    def __init__(self, root, fp):
        self.root = root
        self.col_name = ['VehicleType', 'DerectionTime_O', 'GantryID_O', 'DerectionTime_D', 'GantryID_D'
            , 'TripLength', 'TripEnd', 'TripInformation']
        self.fp = fp
        self.tr = table_reader(self.fp)
        self.sc = searcher(self.fp)
        self.pl = plot(self.fp)


class window:

    def __init__(self, root, fp):
        self.root = root
        self.root.config()
        self.root.title('Inquiry system for Taiwan traffic data')
        self.root.geometry('800x600')
        self.fp = fp

        initface(self.root, self.fp)


class initface(frame):

    def __init__(self, root, fp):
        super(initface, self).__init__(root, fp)
        self.root.config()  # bg
        # 基准界面initface
        self.initface = tk.Frame(self.root)

        self.label = tk.Label(self.initface, text='Inquiry system for Taiwan traffic data', font=("Arial", 25))

        start = Button(self.initface, text='START', width=func_button_w, command=self.start)

        self.label.place(x=200, y=130, anchor='w')
        start.place(x=310, y=230, anchor='w')

        close = Button(self.initface, text='CLOSE', width=func_button_w, command=self.root.destroy)
        close.place(x=310, y=270, anchor='w')

        self.initface.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
        # self.initface.config(background='green')

    def start(self):
        self.initface.destroy()
        table_info(self.root, self.fp)


class table_info(frame):
    def __init__(self, root, fp):
        super(table_info, self).__init__(root, fp)
        self.root.config()  # bg
        # 基准界面initface
        self.table_info = tk.Frame(self.root)
        self.text_x, self.text_y = 150, 50

        self.text = None

        self.bar_v = None
        self.bar_h = None

        label_title = tk.Label(self.table_info, text='Table Info', font=("Arial", 18))
        label_title.place(x=title_u_l_x, y=title_u_l_y)

        back = Button(self.table_info, text='BACK', width=other_button_w, command=self.back)
        back.place(x=back_x, y=back_y)

        clear = Button(self.table_info, text='CLEAR', width=other_button_w, command=self.clear)
        clear.place(x=clear_x, y=clear_y)

        describe_file = Button(self.table_info, text='Describe the Data', width=func_button_w, command=self.describe_file)
        describe_file.place(x=0, y=title_u_l_y+40)

        show_rows = Button(self.table_info, text='Show Rows', width=func_button_w, command=self.show_rows)
        show_rows.place(x=0, y=title_u_l_y+80)

        label_title2 = tk.Label(self.table_info, text='Go to Column', font=("Arial", 18))
        label_title2.place(x=title_u_l_x, y=title_u_l_y+120)

        go_to_col = Button(self.table_info, text='Column Info', width=func_button_w, command=self.go_to_column)
        go_to_col.place(x=0, y=title_u_l_y+160)

        label_title3 = tk.Label(self.table_info, text='Search Data', font=("Arial", 18))
        label_title3.place(x=title_u_l_x, y=title_u_l_y + 200)

        search = Button(self.table_info, text='Search Data', width=func_button_w, command=self.search_table)
        search.place(x=0, y=title_u_l_y+240)

        self.table_info.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
        # self.initface.config(background='green')

    def back(self):
        self.table_info.destroy()
        initface(self.root, self.fp)

    def clear(self):
        if self.text is not None:
            self.text.destroy()
        if self.text is not None:
            self.bar_v.destroy()
        if self.text is not None:
            self.bar_h.destroy()

    def __display(self, data):
        content = data

        self.bar_h = tk.Scrollbar(self.table_info, orient=tk.HORIZONTAL)
        self.bar_h.pack(side=tk.BOTTOM, fill=tk.X)

        self.bar_v = tk.Scrollbar(self.table_info, orient=tk.VERTICAL)
        self.bar_v.pack(side=tk.RIGHT, fill=tk.Y)

        self.text = tk.Text(self.table_info, width=70, height=40, wrap="none")
        self.text.config(xscrollcommand=self.bar_h.set)
        self.text.config(yscrollcommand=self.bar_v.set)
        self.text.place(x=self.text_x, y=self.text_y)

        for i in range(1, len(content)):
            self.text.insert(f'{i}.0', content[i])

        self.bar_h.config(command=self.text.xview)
        self.bar_v.config(command=self.text.yview)

    def describe_file(self):
        self.clear()
        data = self.tr.describe_file()
        self.__display(data)

    def show_rows(self, row=5):
        self.clear()
        data = [''.join(self.col_name)] + self.tr.show_rows()
        self.__display(data)

    def go_to_column(self):
        self.table_info.destroy()
        col_info(self.root, self.fp)

    def search_table(self):
        self.table_info.destroy()
        search_table_info(self.root, self.fp)


class col_info(frame):

    def __init__(self, root, fp):
        super(col_info, self).__init__(root, fp)
        self.root.config()  # bg

        self.col_info = tk.Frame(self.root)

        self.label = tk.Label(self.col_info, text='Select A Column', font=("Arial", 25))
        self.label.place(x=300, y=130, anchor='w')

        back = Button(self.col_info, text='BACK', width=other_button_w, command=self.back)
        back.place(x=back_x, y=back_y)

        clear = Button(self.col_info, text='CLEAR', command=self.clear)
        clear.place(x=clear_x, y=clear_y)

        for i in range(len(self.col_name)):
            col = self.col_name[i]
            Button(self.col_info, text=col.upper(), width=func_button_w, command=partial(self.col, col)).place(x=310, y=180+i*40, anchor='w')

        self.col_info.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

    def col(self, col):
        self.col_info.destroy()
        onecol(self.root, self.fp, col)

    def back(self):
        self.col_info.destroy()
        table_info(self.root, self.fp)

    def clear(self):
        pass


class onecol(frame):

    def __init__(self, root, fp, col):
        super(onecol, self).__init__(root, fp)
        self.root.config()  # bg

        self.onecol = tk.Frame(self.root)
        self.text_x, self.text_y = 170, 50

        self.text = None

        self.bar_v = None
        self.bar_h = None

        self.name = col

        label_title = tk.Label(self.onecol , text=self.name, font=("Arial", 18))
        label_title.place(x=title_u_l_x, y=title_u_l_y)

        show_col = Button(self.onecol, text='SHOW COlUMN', width=func_button_w,command=self.show_col)
        show_col.place(x=0, y=title_u_l_y+40)

        sort_col = Button(self.onecol, text='SORT COLUMN', width=func_button_w, command=self.sort_col)
        sort_col.place(x=0, y=title_u_l_y + 40*2)

        show_col_content = Button(self.onecol, text='SHOW COLUMN CONTENT', width=func_button_w, command=self.show_col_content)
        show_col_content.place(x=0, y=title_u_l_y + 40*3)

        count_info = Button(self.onecol, text='COUNT', width=func_button_w, command=self.count_info)
        count_info.place(x=0, y=title_u_l_y + 40 * 4)

        plot = Button(self.onecol, text='PLOT', width=func_button_w, command=self.plot)
        plot.place(x=0, y=title_u_l_y + 40 * 5)

        search_col = Button(self.onecol, text='SEARCH COLUMN', width=func_button_w, command=self.search_col)
        search_col.place(x=0, y=title_u_l_y + 40 * 6)

        back = Button(self.onecol, text='BACK', width=other_button_w, command=self.back)
        back.place(x=back_x, y=back_y)

        clear = Button(self.onecol, text='CLEAR', command=self.clear)
        clear.place(x=clear_x+10, y=clear_y)

        self.onecol.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)


    def show_col(self):
        self.clear()
        data = self.tr.show_col(self.name)
        self.__display(data)

    def sort_col(self):
        self.clear()
        data = self.tr.sort_column(self.name)
        self.__display(data)

    def show_col_content(self):
        self.clear()
        data = self.tr.show_col_content(self.name)
        self.__display(data)

    def count_info(self):
        self.clear()
        data = self.tr.count_info(self.name)
        self.__display(data)

    def plot(self):
        self.onecol.destroy()
        plot_col(self.root, self.fp, self.name)

    def search_col(self):
        pass

    def back(self):
        self.onecol.destroy()
        col_info(self.root, self.fp)

    def clear(self):
        if self.text is not None:
            self.text.destroy()
        if self.text is not None:
            self.bar_v.destroy()
        if self.text is not None:
            self.bar_h.destroy()

    def __display(self, data):
        content = data

        self.bar_h = tk.Scrollbar(self.onecol, orient=tk.HORIZONTAL)
        self.bar_h.pack(side=tk.BOTTOM, fill=tk.X)

        self.bar_v = tk.Scrollbar(self.onecol, orient=tk.VERTICAL)
        self.bar_v.pack(side=tk.RIGHT, fill=tk.Y)

        self.text = tk.Text(self.onecol, width=70, height=40, wrap="none")
        self.text.config(xscrollcommand=self.bar_h.set)
        self.text.config(yscrollcommand=self.bar_v.set)
        self.text.place(x=self.text_x, y=self.text_y)

        for i in range(len(content)):
            self.text.insert(f'{i}.0', content[i])

        self.bar_h.config(command=self.text.xview)
        self.bar_v.config(command=self.text.yview)


class plot_col(frame):

    def __init__(self, root, fp, name):
        super(plot_col, self).__init__(root, fp)
        self.root.config()  # bg

        self.plot_col = tk.Frame(self.root)

        self.name = name

        self.canvas = None  # 创建一块显示图形的画布
        self.clear = None
        self.toolbar = None


        label_title = tk.Label(self.plot_col, text=self.name, font=("Arial", 18))
        label_title.place(x=title_u_l_x, y=title_u_l_y)

        piechart = Button(self.plot_col, text='PIE CHART', width=func_button_w, command=self.piechart)
        piechart.place(x=0, y=title_u_l_y + 40)

        barchart = Button(self.plot_col, text='BAR CHART', width=func_button_w, command=self.barchart)
        barchart.place(x=0, y=title_u_l_y + 40 * 2)

        plotchart = Button(self.plot_col, text='PLOT CHART', width=func_button_w,
                                  command=self.plotchart)
        plotchart.place(x=0, y=title_u_l_y + 40 * 3)

        scatterchart = Button(self.plot_col, text='SCATTER CHART', width=func_button_w, command=self.scatterchart)
        scatterchart.place(x=0, y=title_u_l_y + 40 * 4)

        back = Button(self.plot_col, text='BACK', width=other_button_w, command=self.back)
        back.place(x=back_x, y=back_y)
        # clear = Button(self.plot_col, text='CLEAR', command=self.clear)
        # clear.place(x=clear_x, y=clear_y)

        self.plot_col.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)



    def piechart(self):

        self.canvas = FigureCanvasTkAgg(self.pl.pie_chart_col(self.name), self.plot_col)
        self.canvas.draw()
        self.canvas.get_tk_widget()  # .pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.clear = Button(self.plot_col, text='clear', command=self.clear_p)
        self.clear.place(x=650, y=530, anchor='w')

        self.canvas.get_tk_widget().pack()

    def barchart(self):

        self.canvas = FigureCanvasTkAgg(self.pl.bar_char_col(self.name), self.plot_col)
        self.canvas.draw()
        self.canvas.get_tk_widget()  # .pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.clear = Button(self.plot_col, text='clear', command=self.clear_p)
        self.clear.place(x=650, y=530, anchor='w')

        self.canvas.get_tk_widget().pack()

    def plotchart(self):

        self.canvas = FigureCanvasTkAgg(self.pl.line_col(self.name), self.plot_col)
        self.canvas.draw()
        self.canvas.get_tk_widget()  # .pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.clear = Button(self.plot_col, text='clear', command=self.clear_p)
        self.clear.place(x=650, y=530, anchor='w')

        self.canvas.get_tk_widget().pack()

    def scatterchart(self):

        self.canvas = FigureCanvasTkAgg(self.pl.scatter_col(self.name), self.plot_col)
        self.canvas.draw()
        self.canvas.get_tk_widget()  # .pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.clear = Button(self.plot_col, text='clear', command=self.clear_p)
        self.clear.place(x=650, y=530, anchor='w')

        self.canvas.get_tk_widget().pack()

    def back(self):
        self.plot_col.destroy()
        onecol(self.root, self.fp, self.name)

    def clear_p(self):
        self.pl.reset()
        self.canvas.get_tk_widget().pack_forget()
        self.clear.destroy()





class search_table_info(frame):

    def __init__(self, root, fp):
        super(search_table_info, self).__init__(self.root, self.fp)
        self.root.config()  # bg
        # 基准界面initface
        self.search_table_info = tk.Frame(self.root)

        self.text_x, self.text_y = 150, 50

        self.text = None

        self.bar_v = None
        self.bar_h = None

        back = Button(self.search_table_info, text='BACK', width=other_button_w, command=self.back)
        back.place(x=back_x, y=back_y)
        clear = Button(self.search_table_info, text='CLEAR', command=self.clear)
        clear.place(x=clear_x, y=clear_y)

        self.search_table_info.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

    def back(self):
        self.search_table_info.destroy()
        col_info(self.root, self.fp)

    def clear(self):
        if self.text is not None:
            self.text.destroy()
        if self.text is not None:
            self.bar_v.destroy()
        if self.text is not None:
            self.bar_h.destroy()

    def __display(self, data):
        content = data

        self.bar_h = tk.Scrollbar(self.onecol, orient=tk.HORIZONTAL)
        self.bar_h.pack(side=tk.BOTTOM, fill=tk.X)

        self.bar_v = tk.Scrollbar(self.self.onecol, orient=tk.VERTICAL)
        self.bar_v.pack(side=tk.RIGHT, fill=tk.Y)

        self.text = tk.Text(self.self.onecol, width=70, height=40, wrap="none")
        self.text.config(xscrollcommand=self.bar_h.set)
        self.text.config(yscrollcommand=self.bar_v.set)
        self.text.place(x=self.text_x, y=self.text_y)

        for i in range(1, len(content)):
            self.text.insert(f'{i}.0', content[i])

        self.bar_h.config(command=self.text.xview)
        self.bar_v.config(command=self.text.yview)


if __name__ == '__main__':
    file = pd.read_csv('TDCS_M06A_20190830_080000.csv')
    # file.columns = [str(i) for i in range(file.shape[1])] 
    col_name = ['VehicleType', 'DerectionTime_O', 'GantryID_O', 'DerectionTime_D', 'GantryID_D'
        , 'TripLength', 'TripEnd', 'TripInformation']
    file.columns = col_name
    fp = processor(file)

    root = tk.Tk()
    window(root, fp)
    root.mainloop()
