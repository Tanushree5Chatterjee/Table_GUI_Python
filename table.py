import tkinter as tk        #Importing Tkinter
from tkinter import messagebox

root = tk.Tk()        #Main window

#Pre configurations
root.title('Table')
root.geometry('1000x500')
root.resizable(False, False)


#Widgets
frm_input = tk.Frame()
frm_mainarea = tk.Frame(height = '250', width = '170')
frm_buttons = tk.Frame(height = '50', width = '170' )

lbl_heading = tk.Label(master = frm_input, text = "Table of : ", font = 16)
ent_num = tk.Entry(master = frm_input, width = 10)

def reset():
    ent_num.delete(0, tk.END)
    lbl_l1["text"] = ""
    lbl_l2["text"] = ""
    lbl_l3["text"] = ""
    lbl_l4["text"] = ""
    lbl_l5["text"] = ""
    lbl_l6["text"] = ""
    lbl_l7["text"] = ""
    lbl_l8["text"] = ""
    lbl_l9["text"] = ""
    lbl_l10["text"] = ""
def calculate():
    
    a = int(ent_num.get())
    lbl_l1["text"] = a, "X", 1, "=", 1*a
    lbl_l2["text"] = a, "X", 2, "=", 2*a
    lbl_l3["text"] = a, "X", 3, "=", 3*a
    lbl_l4["text"] = a, "X", 4, "=", 4*a
    lbl_l5["text"] = a, "X", 5, "=", 5*a
    lbl_l6["text"] = a, "X", 6, "=", 6*a
    lbl_l7["text"] = a, "X", 7, "=", 7*a
    lbl_l8["text"] = a, "X", 8, "=", 8*a
    lbl_l9["text"] = a, "X", 9, "=", 9*a
    lbl_l10["text"] = a, "X", 10, "=", 10*a

lbl_l1 = tk.Label(master = frm_mainarea)
lbl_l2 = tk.Label(master = frm_mainarea)
lbl_l3 = tk.Label(master = frm_mainarea)
lbl_l4 = tk.Label(master = frm_mainarea)
lbl_l5 = tk.Label(master = frm_mainarea)
lbl_l6 = tk.Label(master = frm_mainarea)
lbl_l7 = tk.Label(master = frm_mainarea)
lbl_l8 = tk.Label(master = frm_mainarea)
lbl_l9 = tk.Label(master = frm_mainarea)
lbl_l10 = tk.Label(master = frm_mainarea)

btn_reset = tk.Button(master = frm_buttons, text = 'Reset', fg = 'red', command = reset)
btn_calculate = tk.Button(master = frm_buttons, text = 'Calculate', fg = 'red', command = calculate)
btn_quit = tk.Button(master = frm_buttons, text = 'Quit', fg = 'red', command = root.destroy)

#Positions
lbl_heading.grid(row = 0, column = 0, pady = 5, padx = 10) 
ent_num.grid(row = 0, column = 1, pady = 2)

lbl_l1.grid(row = 0, column = 0, pady = 2, padx = 10)
lbl_l2.grid(row = 1, column = 0, pady = 2, padx = 10)
lbl_l3.grid(row = 2, column = 0, pady = 2, padx = 10)
lbl_l4.grid(row = 3, column = 0, pady = 2, padx = 10)
lbl_l5.grid(row = 4, column = 0, pady = 2, padx = 10)
lbl_l6.grid(row = 5, column = 0, pady = 2, padx = 10)
lbl_l7.grid(row = 6, column = 0, pady = 2, padx = 10)
lbl_l8.grid(row = 7, column = 0, pady = 2, padx = 10)
lbl_l9.grid(row = 8, column = 0, pady = 2, padx = 10)
lbl_l10.grid(row = 9, column = 0, pady = 2, padx = 10)

frm_input.grid(row = 1, column = 0, pady = 5, padx = 10)
frm_mainarea.grid(row = 2, column = 0, pady = 5, padx = 10)
frm_buttons.grid(row = 3, column = 0, pady = 5, padx = 10)

btn_reset.grid(row = 0, column = 1, pady = 5, padx = 5) 
btn_calculate.grid(row = 0, column = 2, pady = 5, padx = 5)
btn_quit.grid(row = 0, column = 3, pady = 5, padx = 5)

#Mainloop
root.mainloop()