from tkinter import *

from create_plots import showPlot
from create_table import showTable
from create_table import x
from convert_to_json import convertToJSON

root = Tk()
root.title('РУХ ОСНОВНИХ ЗАСОБІВ')
root.geometry('300x300')
root.resizable(False, False)
root.configure(bg = 'gray22')

def openPlot():
    showPlot()

def openTable():
    showTable()
    root_2 = Tk()
    root_2.geometry('1400x300')
    root_2.title('АНАЛІЗ РУХУ ОСНОВНИХ ЗАСОБІВ')
    lbl = Label(root_2)
    lbl.configure(font = (7), text = x)
    lbl.place(x = 0, y = 0)
    root_2.mainloop()

def createJSON():
    convertToJSON()
    root_3 = Tk()
    root_3.geometry('200x70')
    root_3.resizable(False, False)
    root_3.title('повідомлення')
    lbl = Label(root_3)
    lbl.configure(font = (5), text = 'Файл у форматі \nJSON сформовано')
    lbl.place(x = 4, y = 2)
    root_3.mainloop()

btn1 = Button(root)
btn1.configure(bg = 'gray', fg = 'white', text = 'відкрити графік', command = openPlot)
btn1.place(x = 100, y = 20, width = 110, height = 30)

btn2 = Button(root)
btn2.configure(bg = 'gray', fg = 'white', text = 'відкрити таблицю', command = openTable)
btn2.place(x = 100, y = 50, width = 110, height = 30)

btn3 = Button(root)
btn3.configure(bg = 'gray', fg = 'white', text = 'відкрити файл json', command = createJSON)
btn3.place(x = 100, y = 80, width = 110, height = 30)


root.mainloop()