from Tkinter import *
import runpy
master = Tk()
master.geometry("1920x1080") 

def show_entry_fields():
	a = e1.get()
	b = e2.get()
	username='Mrigank'
	password='potty'
	if a==username :
		if b==password :  
		  master.destroy()
		  runpy.run_path("home.py")
		  return
		else :
			print("Wrong password")
	else :
		print("Wrong username")


Label(master, text="Username", font="32").place(x=800, y=500)
Label(master, text="Password", font="32").place(x=800, y=530)

e1 = Entry(master)
e2 = Entry(master, show="*")

e1.place(x=900, y=500)
e2.place(x=900, y=530)

Button(master, text='Quit', pady=4, command=master.quit).place(x=800, y=600)
Button(master, text='Login',pady=4, command=show_entry_fields).place(x=850, y=600)

mainloop( )

