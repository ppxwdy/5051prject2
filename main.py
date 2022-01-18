import tkinter as tk
from file_reader import *
from GUI2 import window

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