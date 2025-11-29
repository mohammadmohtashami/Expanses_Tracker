from tkinter import *
from tkcalendar import Calendar 
from tkinter import ttk
root = Tk()

def apply():
    pass 
def add():
    # define a new window 
    add_window = Tk()
    # define the objects 
    value_option = ["Transportation" , "Food" , "purchase" , "Fun" , "other"]
    add_window.title("add Expanses")
    lbl_title = Label(add_window , text="title of Expanses")
    lbl_category = Label(add_window , text = "category")
    lbl_amount = Label(add_window  , text = "amount")
    lbl_date = Label(add_window , text="date")
    amount_entry = Entry(add_window)
    title_entry = Entry (add_window)
    value_inside = StringVar(add_window)
    category_menu = OptionMenu(add_window ,value_inside , *value_option)
    value_inside.set("select a category")
    cal = Calendar(add_window , selectmode = "day" , year = 2025 , month = 11 , day = 27 )
    submit_btn = Button(add_window , text="submit" , command= lambda:submit())
    quit_btn = Button(add_window , text= "Quit" , command=add_window.destroy)
    # arrangement the objects 
    lbl_title.grid(row=0 , column=0)
    lbl_category.grid(row=1,column=0)
    lbl_amount.grid(row=2 , column=0)
    lbl_date.grid(row=3 , column=0)
    amount_entry.grid(row=2 , column=1)
    title_entry.grid(row=0 , column=1)
    category_menu.grid(row=1 , column=1)
    cal.grid(row= 3 , column=1)
    submit_btn.grid(row=4 ,column=1)
    quit_btn.grid(row=5 , column=1)
    
    def submit():
        title= title_entry.get()
        category = value_inside.get()
        amount = amount_entry.get()
        date = cal.get_date()

        return title , category , amount , date  
    mainloop()

def filter_page():
    
    filter_window = Tk()
    filter_option = ["Transportation" , "Food" , "purchase" , "Fun" , "other"]

    filter_title_lbl = Label(filter_window , text = "add a topic to filter the title expanses")
    filter_amount_lbl = Label(filter_window , text="add upper and lower limit ")
    filter_date_lbl = Label(filter_window , text = "add a date to filter expanses")
    filter_category_lbl = Label(filter_window , text= "add a category to filter the expanses ")
    value_inside = StringVar(filter_window)
    category_menu_filter = OptionMenu(filter_window,value_inside , *filter_option)
    value_inside.set("select a category")
    title_filter_entry = Entry(filter_window)
    upper_amount_entry = Entry(filter_window)
    lower_amount_entry = Entry(filter_window)
    start_date_filter_entry = Entry (filter_window)
    end_date_filter_entry = Entry(filter_window)
    submit_filter_btn = Button(filter_window , text ="submit" , command= lambda:filter_submit())
    
    # arrange the objects     
    filter_title_lbl.grid (row = 1 , column= 1 )
    filter_amount_lbl.grid(row=3 , column=1)
    filter_date_lbl.grid (row =4 , column=1 )
    filter_category_lbl.grid(row = 2  ,column = 1)
    title_filter_entry.grid(row=1 , column=2)
    category_menu_filter.grid(row=2 , column=2)
    upper_amount_entry.grid(row=3 , column=3)
    lower_amount_entry.grid(row=3 , column=2)
    start_date_filter_entry.grid (row = 4 , column=2)
    end_date_filter_entry.grid(row=4 , column=3)
    submit_filter_btn.grid (row=5 , column = 2 )
    def filter_submit():
        category_filter = value_inside.get()
        title_filter = title_filter_entry.get()
        upper_amount_filter = upper_amount_entry.get()
        lower_amount_filter = lower_amount_entry.get()
        start_date_filter= start_date_filter_entry.get()
        end_date_filter = end_date_filter_entry.get()
        filter_window.destroy()
        return  category_filter , title_filter , upper_amount_filter  , lower_amount_filter , start_date_filter , end_date_filter
    mainloop()
def edit(item):
    pass

def delete(item):
    treeview.delete(item)
    

# define the objects of the root window 
filter_btn = Button(root , text = "filter page" , command= filter_page)
apply_btn = Button(root , text= "apply" , command=apply) 
add_btn = Button(root , text = "add " , command= add)
# arragement the objects 
filter_btn.grid(row=2  , column= 1)
apply_btn.grid(row = 0  ,column= 1 )
add_btn.grid(row=1  ,column=1)
edit_btn = Button(root , text = "edit" , command = lambda : edit(treeview.selection()))
edit_btn.grid(row = 3 , column = 1)
delete_btn = Button(root , text="delete" , command = lambda:delete(treeview.selection()))
delete_btn.grid(row = 4 , column =1)
treeview = ttk.Treeview(columns=("category" , "amount" , "date"))
treeview.grid(row = 6 , columnspan=3 , column=1)
treeview.heading("#0" , text="Expanses title")
treeview.heading("category" ,text="Expanses category")
treeview.heading("amount" , text="Expanses amount")
treeview.heading("date" ,text="Expanses date")

# how to insert a vlue in treeview 
# treeview.insert("" , tk.END , text="Item 1")
mainloop()