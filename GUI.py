from tkinter import *
from tkcalendar import Calendar 

root = Tk()

def apply():
    pass 

def add():
    add_window = Tk()
    value_option = ["Transportation" , "Food" , "purchase" , "Fun" , "other"]
    add_window.title("add Expanses")
    lbl_title = Label(add_window , text="title of Expanses")
    lbl_title.pack()
    lbl_category = Label(add_window , text = "category")
    lbl_category.pack()
    lbl_amount = Label(add_window  , text = "amount")
    lbl_amount.pack()
    lbl_date = Label(add_window , text="date")
    lbl_date.pack()
    amount_entry = Entry(add_window)
    amount_entry.pack()
    title_entry = Entry (add_window)
    title_entry.pack()
    value_inside = StringVar(add_window)
    category_menu = OptionMenu(add_window ,value_inside , *value_option)
    value_inside.set("select a category")
    category_menu.pack()
    cal = Calendar(add_window , selectmode = "day" , year = 2025 , month = 11 , day = 27 )
    cal.pack(pady=20)
    
    mainloop()
    

apply_btn = Button(root , text= "apply" , command=apply) 
apply_btn.pack()
add_btn = Button(root , text = "add " , command= add)
add_btn.pack()




mainloop()