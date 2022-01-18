import tkinter as tk
# from tkmacosx import Button
from tkinter import  Button
from numpy.lib.function_base import select
from numpy.lib.shape_base import split
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk
import numpy as np
from file_process import *

# file = pd.read_csv('TDCS_M06A_20190830_080000.csv')
# file.columns = [str(i) for i in range(file.shape[1])] 

file = pd.read_csv('TDCS_M06A_20190830_080000.csv')
file.columns = [str(i) for i in range(file.shape[1])] 

fp = processor(file)

di = fp.count_col_content('0').to_dict()
keys = ['Element', 'Number of Element']
element = list(di[keys[0]].values())
number = list(di[keys[1]].values())



def drawfig():
    fig = plt.Figure(figsize=(4, 3))

    # p1 = fig.add_subplot(111)
    # x = np.linspace(0, 8, 100)
    # p1.plot(x, np.sin(x))
    # p1.set_title('test figure')
    # p1.set_xlabel('x')
    # p1.set_ylabel('y') 

    p1 = fig.add_subplot(111)
    
    element = list(di[keys[0]].values())
    number = list(di[keys[1]].values())
    
    
    max_dix = number.index(max(number))
    explode=[0 for _ in range(len(number))]
    explode[max_dix] = 0.2    
    
    p1.pie(number, labels=element, shadow=True, autopct='%.2f%%', explode=explode)
    
    return fig
 

 
class window():
    def __init__(self, root):
        self.root = root
        self.root.config()
        self.root.title('File Read System')
        self.root.geometry('800x600')
        
        initface(self.root)        
                
class initface():
    def __init__(self, root):
        
        self.root = root
        
        self.root.config()  # bg
        #基准界面initface
        self.initface = tk.Frame(self.root)
        
        table_b = Button(self.initface, text='Show tables', command=self.table_)  # , bg='red')
        table_b.place(x=330, y=230,  anchor='w')
        plot_b = Button(self.initface, text='Show plots', command=self.plot_)  # , bg='red')
        plot_b.place(x=330, y =260, anchor='w')
       
        
        self.initface.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
        # self.initface.config(background='green')
        
        
    def table_(self):       
        self.initface.destroy()
        table(self.root)      
        
    def plot_(self):
        self.initface.destroy()
        plot(self.root)
 
 
class table():
    def __init__(self,root):
        
        self.root = root
        # self.root.config(bg='blue')
        self.table = tk.Frame(self.root)
        
        
        self.label_x = 150
        self.label_y = 50
        self.label_dy = 30
        self.labels = []
        self.text = None
        
        self.bar_v = None
        self.bar_h = None
        
        back_main = Button(self.table, text='back', command=self.back)
        back_main.place(x=0, y=30, anchor='w')
        
        clear = Button(self.table, text='clear', command=self.clear)  #, bg='red')
        clear.place(x=650, y=530, anchor='w')
        
        func1 = Button(self.table, text='func1',  command=self.func1) #, bg='red')
        func1.place(x=0, y=80, anchor='w')
        
        show_table_head = Button(self.table, text='show_table_head', command=self.show_table_head) #, bg='red')
        show_table_head.place(x=0, y=120, anchor='w')
        
        describe = Button(self.table, text='describe',  command=self.describe ) #, bg='red')
        describe.place(x=0, y=160, anchor='w')
        
        self.table.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
        # self.table.config(background='blue')
        
    def back(self):
        self.table.destroy()
        initface(self.root)
        
        
    def clear(self):
        for i in range(len(self.labels)):
            self.labels.pop().destroy()
            # l.destroy()
        if self.text is not None:
            self.text.destroy()
        if self.text is not None:
            self.bar_v.destroy()
        if self.text is not None:
            self.bar_h.destroy()
        # self.bar_h.pack_forget()
        


    def func1(self):
        self.clear()
        
            
    def show_table_head(self):
        self.clear()
        content = file.head(10).to_string().split('\n')
        
        
        self.bar_h = tk.Scrollbar(self.table, orient=tk.HORIZONTAL)
        self.bar_h.pack(side=tk.BOTTOM, fill=tk.X)
        
        self.bar_v = tk.Scrollbar(self.table, orient=tk.VERTICAL)
        self.bar_v.pack(side=tk.RIGHT, fill=tk.Y)
        
         
        self.text = tk.Text(self.table, width=70, height=40, wrap = "none") 
        self.text.config(xscrollcommand=self.bar_h.set)
        self.text.config(yscrollcommand=self.bar_v.set)
        # text.pack(expand=tk.YES, fill=tk.BOTH)
        self.text.place(x=self.label_x, y=self.label_y)
        
        for i in range(1, len(content)):
            # tmp = content[i].split(',Y,')
            # temp = tmp[0].strip() + ",Y ," + tmp[-1].strip()
            self.text.insert(f'{i}.0', content[i]+'\n')
        
        self.bar_h.config(command=self.text.xview)
        self.bar_v.config(command=self.text.yview)
        
        
           
            
    def describe(self):
        self.clear()
        content = file.describe().to_string().split('\n') 
        for i in range(len(content)):
            l = tk.Label(self.table, text=content[i].strip())
            l.place(x =self.label_x, y = self.label_y + i*self.label_dy)
            self.labels.append(l)    
            
        
        
class plot():
    def __init__(self, root):
        self.root = root
        # self.root.config(bg='orange')
        self.plot = tk.Frame(self.root)
        
        self.canvas = None             #创建一块显示图形的画布
        self.clear = None
        self.toolbar = None
        
        back_main = Button(self.plot, text='back', command=self.back)
        back_main.place(x=0, y=30, anchor='w')
        
        plot1 = Button(self.plot, text='plot1', command=self.draw) #, bg='red')
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
        self.canvas.get_tk_widget() #.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        # 显示工具条控件
        # self.toolbar = NavigationToolbar2Tk(self.canvas, self.plot)
        # self.toolbar.update()
        
        self.clear = Button(self.plot, text='clear', command=self.clear_plot)
        self.clear.place(x=650, y=530, anchor='w')
        
        self.canvas.get_tk_widget().pack()
    
    def clear_plot(self):
        # for item in self.canvas.get_tk_widget().find_all():
        #     self.canvas.get_tk_widget().delete(item)
        self.canvas.get_tk_widget().pack_forget() 
        self.clear.destroy()


# if __name__ == '__main__':
#     root = tk.Tk()
#     root.columnconfigure(0, weight=1)
#     window(root)
#     root.mainloop()

from collections import Counter, defaultdict
c = Counter(list(file['1'].values.tolist()))

df = pd.DataFrame()
df.insert(df.shape[1], 'Element', list(c.keys()))
df.insert(df.shape[1], 'Number of Element', list(c.values()))

# print(df.to_string(index=False))

# d = defaultdict(str)
# print(d['1'] == '')
# print(df.shape)
# print(df.columns.values.tolist())
# print(str(file['0'].iloc[0]) == '31')
print(file.head())