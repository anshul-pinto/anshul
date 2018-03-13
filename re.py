from Tkinter import *
import os
import runpy

re=Tk()

def open_home():
  re.destroy()
  runpy.run_path("home.py")

def open_mf():
   re.destroy()
   runpy.run_path("stocks.py")
   
def open_stocks():
   re.destroy()
   runpy.run_path("stocks.py")
   
def open_gold():
   re.destroy()
   runpy.run_path("gold.py")
   
def open_cash():
   re.destroy()
   runpy.run_path("cash.py")
   
def open_bonds():
   re.destroy()
   runpy.run_path("bonds.py")
   
def re_form():			#entry form
	inputform = Tk()
	
	
	inputform.title=("Add Real Estate")
	
	Label(inputform , text="Add Real Estate" , font = "Lato 20").grid(row=0)
	
	name_prop = Label(inputform , text= "Name of property" , font = "Lato 15" , fg = 'White', bg='Black', width=20 )
	name_prop.grid(row=1,column=0)
	get_name_prop = Entry(inputform,width=20).grid(row=1 , column=1)
	
	type_prop = Label(inputform , text= "Type of property" , font = "Lato 15" , fg = 'White', bg='Black', width=20 )
	type_prop.grid(row=2 , column =0 )
	get_type_prop = Entry(inputform,width=20).grid(row=2 , column=1)
	
	price= Label(inputform, text="Price of property " ,font = "Lato 15" , fg = 'White', bg='Black',width=20)
	price.grid(row=3,column=0)
	get_price = Entry(inputform).grid(row=3 , column=1)
	
	total_size = Label(inputform , text= "Size of property" , font = "Lato 15" , fg = 'White', bg='Black', width=20 )
	total_size.grid(row=4 , column =0 )
	get_total_size = Entry(inputform,width=20).grid(row=4 , column=1)
	
	
	
	accept = Button(inputform, text="Accept", font = "Lato 15" , fg = 'White' , width=20 , command=lambda:inputform.destroy())
	accept.grid(row=5)
	 
	inputform.mainloop() 

re.title("LIT")
re.geometry("1920x1080")

l1=Label(re,text=" ", font="Lato 20").pack()
l2=Label(re, text="L O N G - T E R M   I N V E S T M E N T   T R A C K E R", font="Lato 30").pack()

top = Frame(re)
top.pack(side=TOP)

l3=Label(re,text="Real Estate", font="Lato 20").pack()

mainoptions = ['Home', 'Stocks', 'Mutual Funds','Real estate','Gold', 'Cash', 'Bonds']
i=0

l1 = Button(re,text=mainoptions[i], font="Lato 20",fg='White',bg='Black', command= open_home)
l1.place(x = 0, y = 200 + i*51, width=200, height=50)
i+=1

l2 = Button(re,text=mainoptions[i], font="Lato 20",fg='White',bg='Black', command=open_stocks)
l2.place(x = 0, y = 200 + i*51, width=200, height=50)
i+=1

l3 = Button(re,text=mainoptions[i], font="Lato 20",fg='White',bg='Black', command=open_mf)
l3.place(x = 0, y = 200 + i*51, width=200, height=50)
i+=1

l4 = Button(re,text=mainoptions[i], font="Lato 20",fg='White',bg='Black')
l4.place(x = 0, y = 200 + i*51, width=200, height=50)
i+=1

l5 = Button(re,text=mainoptions[i], font="Lato 20",fg='White',bg='Black', command=open_gold)
l5.place(x = 0, y = 200 + i*51, width=200, height=50)
i+=1

l6 = Button(re,text=mainoptions[i], font="Lato 20",fg='White',bg='Black', command=open_cash)
l6.place(x = 0, y = 200 + i*51, width=200, height=50)
i+=1

l7 = Button(re,text=mainoptions[i], font="Lato 20",fg='White',bg='Black', command=open_bonds)
l7.place(x = 0, y = 200 + i*51, width=200, height=50)
i+=1

add_entry = Button(re, text="Add an entry", font= "Lato 20" , fg = 'White' , bg ='Black', command=re_form ) #give command
add_entry.place (x= 1600 , y=900 , width=200 , height =50)
mainloop()

