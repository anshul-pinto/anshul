from Tkinter import * 

form = Tk()
	
	
form.title=("Add New Stock")
	
Label(form , text="Add new Stock" , font = "Lato 20")
	
stock_symbol = Label(form , text= "Stock" , font = "Lato 15" , fg = 'White', bg='Black')
stock_symbol.grid(row=0,column=0)
	
number_of_units = Label(form , text= "Number of stocks" , font = "Lato 15" , fg = 'White', bg='Black')
number_of_units.grid(row=1,column=0)
	
price= Label(form, text="Price per Share" ,font = "Lato 15" , fg = 'White', bg='Black')
price.grid(row=2,column=0)
	
date_purchase= Label(form , text ="Date of Purchase" ,font = "Lato 15" , fg = 'White', bg='Black')
date_purchase.grid(row=3,column=0)
	
form.mainloop()

