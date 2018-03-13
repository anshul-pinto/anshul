from Tkinter import *
import os
import runpy

stocks=Tk()

def open_home():
  stocks.destroy()
  runpy.run_path("home.py")

def open_mf():
   stocks.destroy()
   runpy.run_path("mf.py")
   
def open_re():
   stocks.destroy()
   runpy.run_path("re.py")
   
def open_gold():
   stocks.destroy()
   runpy.run_path("gold.py")
   
def open_cash():
   stocks.destroy()
   runpy.run_path("cash.py")
   
def open_bonds():
   stocks.destroy()
   runpy.run_path("bonds.py")

def stock_form():			#entry form
	inputform = Tk()
	
	
	inputform.title=("Add New Stock")
	
	Label(inputform , text="Add new Stock" , font = "Lato 20").grid(row=0)
	
	stock_symbol = Label(inputform , text= "Stock" , font = "Lato 15" , fg = 'White', bg='Black', width=20)
	stock_symbol.grid(row=1,column=0)
	get_stock = Entry(inputform).grid(row=1 , column=1)
	
	number_of_units = Label(inputform , text= "Number of stocks" , font = "Lato 15" , fg = 'White', bg='Black', width=20)
	number_of_units.grid(row=2,column=0)
	get_number = Entry(inputform).grid(row=2 , column=1)
	
	price= Label(inputform, text="Price per Share" ,font = "Lato 15" , fg = 'White', bg='Black',width=20)
	price.grid(row=3,column=0)
	get_price = Entry(inputform).grid(row=3 , column=1)
	
	date_purchase= Label(inputform , text ="Date of Purchase" ,font = "Lato 15" , fg = 'White', bg='Black',width=20)
	date_purchase.grid(row=4,column=0)
	get_date = Entry(inputform).grid(row=4 , column=1)
	
	accept = Button(inputform, text="Accept", font = "Lato 15" , fg = 'Black' , width=40,command=lambda:inputform.destroy())
	accept.grid(row=5)
	 
	inputform.mainloop()

#stocks page

stocks.title("LIT")
stocks.geometry("1920x1080")

l1=Label(stocks,text=" ", font="Lato 20").pack()
l2=Label(stocks, text="L O N G - T E R M   I N V E S T M E N T   T R A C K E R", font="Lato 30").pack()

top = Frame(stocks)
top.pack(side=TOP)

l3=Label(stocks,text="Stocks", font="Lato 20").pack()

mainoptions = ['Home', 'Stocks', 'Mutual Funds','Real estate','Gold', 'Cash', 'Bonds']
i=0

l1 = Button(stocks,text=mainoptions[i], font="Lato 20",fg='White',bg='Black', command= open_home)
l1.place(x = 0, y = 200 + i*51, width=200, height=50)
i+=1

l2 = Button(stocks,text=mainoptions[i], font="Lato 20",fg='White',bg='Black')
l2.place(x = 0, y = 200 + i*51, width=200, height=50)
i+=1

l3 = Button(stocks,text=mainoptions[i], font="Lato 20",fg='White',bg='Black', command=open_mf)
l3.place(x = 0, y = 200 + i*51, width=200, height=50)
i+=1

l4 = Button(stocks,text=mainoptions[i], font="Lato 20",fg='White',bg='Black', command=open_re)
l4.place(x = 0, y = 200 + i*51, width=200, height=50)
i+=1

l5 = Button(stocks,text=mainoptions[i], font="Lato 20",fg='White',bg='Black', command=open_gold)
l5.place(x = 0, y = 200 + i*51, width=200, height=50)
i+=1

l6 = Button(stocks,text=mainoptions[i], font="Lato 20",fg='White',bg='Black', command=open_cash)
l6.place(x = 0, y = 200 + i*51, width=200, height=50)
i+=1

l7 = Button(stocks,text=mainoptions[i], font="Lato 20",fg='White',bg='Black', command=open_bonds)
l7.place(x = 0, y = 200 + i*51, width=200, height=50)
i+=1

add_entry = Button(stocks, text="Add an entry", font= "Lato 20" , fg = 'White' , bg ='Black' ,command=stock_form ) #give command
add_entry.place (x= 1600 , y=900 , width=200 , height =50)


	
	
	

stocks.mainloop()

