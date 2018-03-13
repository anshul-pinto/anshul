from Tkinter import *
import os
import runpy

cash=Tk()

def open_home():
  cash.destroy()
  runpy.run_path("home.py")

def open_mf():
   cash.destroy()
   runpy.run_path("mf.py")
   
def open_re():
   cash.destroy()
   runpy.run_path("re.py")
   
def open_gold():
   cash.destroy()
   runpy.run_path("gold.py")
   
def open_stocks():
   cash.destroy()
   runpy.run_path("stocks.py")
   
def open_bonds():
   cash.destroy()
   runpy.run_path("bonds.py")
   
def cash_form():			#entry form
	inputform = Tk()
	
	
	inputform.title=("Add New Currency")
	
	Label(inputform , text="Add new Currency" , font = "Lato 20").grid(row=0)
	
	currency = Label(inputform , text= "Currency" , font = "Lato 15" , fg = 'White', bg='Black', width=20 )
	currency.grid(row=1,column=0)
	get_currency = Entry(inputform,width=20).grid(row=1 , column=1)
	
	number_of_units = Label(inputform , text= "Amount" , font = "Lato 15" , fg = 'White', bg='Black', width=20 )
	number_of_units.grid(row=2 , column =0 )
	get_unit = Entry(inputform,width=20).grid(row=2 , column=1)
	
	accept = Button(inputform, text="Accept", font = "Lato 15" , fg = 'White' , width=20 , command=lambda:inputform.destroy())
	accept.grid(row=3)
	 
	inputform.mainloop()
   


cash.title("LIT")
cash.geometry("1920x1080")

l1=Label(cash,text=" ", font="Lato 20").pack()
l2=Label(cash, text="L O N G - T E R M   I N V E S T M E N T   T R A C K E R", font="Lato 30").pack()

top = Frame(cash)
top.pack(side=TOP)

l3=Label(cash,text="Cash", font="Lato 20").pack()

mainoptions = ['Home', 'Stocks', 'Mutual Funds','Real estate','Gold', 'Cash', 'Bonds']
i=0

l1 = Button(cash,text=mainoptions[i], font="Lato 20",fg='White',bg='Black', command= open_home)
l1.place(x = 0, y = 200 + i*51, width=200, height=50)
i+=1

l2 = Button(cash,text=mainoptions[i], font="Lato 20",fg='White',bg='Black', command= open_stocks)
l2.place(x = 0, y = 200 + i*51, width=200, height=50)
i+=1

l3 = Button(cash,text=mainoptions[i], font="Lato 20",fg='White',bg='Black', command=open_mf)
l3.place(x = 0, y = 200 + i*51, width=200, height=50)
i+=1

l4 = Button(cash,text=mainoptions[i], font="Lato 20",fg='White',bg='Black', command=open_re)
l4.place(x = 0, y = 200 + i*51, width=200, height=50)
i+=1

l5 = Button(cash,text=mainoptions[i], font="Lato 20",fg='White',bg='Black', command=open_gold)
l5.place(x = 0, y = 200 + i*51, width=200, height=50)
i+=1

l6 = Button(cash,text=mainoptions[i], font="Lato 20",fg='White',bg='Black')
l6.place(x = 0, y = 200 + i*51, width=200, height=50)
i+=1

l7 = Button(cash,text=mainoptions[i], font="Lato 20",fg='White',bg='Black', command=open_bonds)
l7.place(x = 0, y = 200 + i*51, width=200, height=50)
i+=1

add_entry = Button(cash, text="Add an entry", font= "Lato 20" , fg = 'White' , bg ='Black' , command= cash_form ) #give command
add_entry.place (x= 1600 , y=900 , width=200 , height =50)

mainloop()

