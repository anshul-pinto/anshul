from Tkinter import *
import os
import runpy

home=Tk()

def open_stocks():
   home.destroy()
   runpy.run_path("stocks.py")

def open_mf():
   home.destroy()
   runpy.run_path("mf.py")
   
def open_re():
   home.destroy()
   runpy.run_path("re.py")
   
def open_gold():
   home.destroy()
   runpy.run_path("gold.py")
   
def open_cash():
   home.destroy()
   runpy.run_path("cash.py")
   
def open_bonds():
   home.destroy()
   runpy.run_path("bonds.py")

home.title("LIT")
home.geometry("1920x1080")
l1=Label(home,text=" ", font="Lato 20").pack()
l2=Label(home,text="L O N G - T E R M   I N V E S T M E N T   T R A C K E R", font="Lato 30").pack()

top = Frame(home)
top.pack(side=TOP)

l3=Label(home, text="Home", font="Lato 20").pack()

mainoptions = ['Home', 'Stocks', 'Mutual Funds','Real estate','Gold', 'Cash', 'Bonds']

i=0 #tracks main option

l1 = Button(home,text=mainoptions[i], font="Lato 20",fg='White',bg='Black')
l1.place(x = 0, y = 200 + i*51, width=200, height=50)
i+=1

l2 = Button(home,text=mainoptions[i], font="Lato 20",fg='White',bg='Black', command= open_stocks)
l2.place(x = 0, y = 200 + i*51, width=200, height=50)
i+=1

l3 = Button(home,text=mainoptions[i], font="Lato 20",fg='White',bg='Black', command=open_mf)
l3.place(x = 0, y = 200 + i*51, width=200, height=50)
i+=1

l4 = Button(home,text=mainoptions[i], font="Lato 20",fg='White',bg='Black', command=open_re)
l4.place(x = 0, y = 200 + i*51, width=200, height=50)
i+=1

l5 = Button(home,text=mainoptions[i], font="Lato 20",fg='White',bg='Black', command=open_gold)
l5.place(x = 0, y = 200 + i*51, width=200, height=50)
i+=1

l6 = Button(home,text=mainoptions[i], font="Lato 20",fg='White',bg='Black', command=open_cash)
l6.place(x = 0, y = 200 + i*51, width=200, height=50)
i+=1

l7 = Button(home,text=mainoptions[i], font="Lato 20",fg='White',bg='Black', command=open_bonds)
l7.place(x = 0, y = 200 + i*51, width=200, height=50)
i+=1

exit_button = Button(home, text="Exit", font= "Lato 20" , fg = 'White' , bg ='Black' ,command= lambda:home.destroy() ) #give command
exit_button.place (x= 1600 , y=900 , width=200 , height =50)

mainloop()
