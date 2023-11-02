import tkinter
import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", password="admin")
cur = con.cursor(buffered=True)  # need to use buffer otherwise error

try:
    cur.execute("use dataform")
    print("used database successfully")
except:
    cur.execute("create database dataform ")
    cur.execute("use dataform ")

try:
    cur.execute("describe dataform")
except:
    cur.execute("create table user(name VARCHAR(40), age VARCHAR(10), dep VARCHAR(30),gen VARCHAR(10))")

def Register():
    name=t1.get()
    age=t2.get()
    dep=t3.get()
    gen=t4.get()
    cur.execute('INSERT INTO user(name,age,dep,gen)VALUES(%s,%s,%s,%s)',(name,age,dep,gen))
    con.commit()
    con.close()



win = tkinter.Tk()
win.geometry("500x500")
win.title("Login form")
l1 = tkinter.Label(win, text="Name")
l2 = tkinter.Label(win, text="AGE ")
l3 = tkinter.Label(win, text="Department ")
l4 = tkinter.Label(win, text="Gender ")

l3.grid(row=3, column=1)
l2.grid(row=2, column=1)
l1.grid(row=1, column=1)
l4.grid(row=4, column=1)

t1 = tkinter.Entry(win, width=35)
t2 = tkinter.Entry(win, width=35)
t3 = tkinter.Entry(win, width=35)
t4 = tkinter.Entry(win, width=35)
t1.grid(row=1, column=2)
t2.grid(row=2, column=2)
t3.grid(row=3, column=2)
t4.grid(row=4, column=2)
b = tkinter.Button(win, text="submit ", command=Register, bg='black', fg='white', width=10, height=2)
b.grid(row=5, column=2)

win.mainloop()
