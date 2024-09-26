from tkinter import*
from tkinter import messagebox
import mysql.connector

conn = mysql.connector.connect(host = "localhost", user = "Nonhlanhla",password = "Mbube123@",database = "cbi")
c = conn.cursor()


root = Tk()

employee_id = Entry(root)
employee_id.grid(row=1,column=0)
first_name = Entry(root)
first_name.grid(row=1,column=1)
surname = Entry(root)
surname.grid(row=1,column=2)
salary = Entry(root)
salary.grid(row=1,column=3)

mylabel1 = Label(root,text="Enter employee iD: ")
mylabel1.grid(row=0,column=0)
mylabel2 = Label(root,text="Enter first name")
mylabel2.grid(row=0,column=1)
mylabel3 = Label(root,text="Enter surname")
mylabel3.grid(row=0,column=2)
mylabel4 = Label(root,text="Enter salary")
mylabel4.grid(row=0,column=3)

def add_employees():
    iD = employee_id.get()
    name = first_name.get()
    surnm = surname.get()
    salry = salary.get()
    query = "insert into employees(first_name,Surname,Salary)values(%s,%s,%s)"
    c.execute(query,(iD,name,surnm,salry))
    conn.commit()
    messagebox.showinfo("","Eployee has been added successfully")


def view_employees():
    query ="SELECT * FROM employees"
    c.execute(query)
    result = c.fetchall()
    for row in result:
       messagebox.showinfo("", f"employee_id{row[0]}, first_name{row[1]},Surname{row[2]},Salary{row[3]} ")

def update_employees():
    iD = employee_id.get()
    name = first_name.get()
    surnm = surname.get()
    salry = salary.get()


    if name:
        query = "update employees set first_name = %s where employees_id = %s"
        c.execute(query,(name,iD))

    if surnm :
        query= "update employees set Surname = %s where employee_id = %s"
        c.execute(query,(surnm,iD))

    if salry:
        query = " update employees set Salary = %s where employee_id = %s"
        c.execute(query,(salry,iD))
    conn.commit()


def del_employee():
    iD = employee_id.get()
    name = first_name.get()
    surnm = surname.get()
    salry = salary.get()

    query = "Delete from employees where employee_id = %s"
    c.execute(query,[iD])
    messagebox.showinfo("","deleted successfully")
    conn.commit()


mybutton1 = Button(root,text="Add",command= add_employees)
mybutton1.grid(row=3,column=0)
mybutton2 = Button(root,text="Delete",command=del_employee)
mybutton2.grid(row=3,column=1)
mybutton3 = Button(root,text="Display",command=view_employees)
mybutton3.grid(row=3,column=2)
mybutton4 = Button(root,text="Update",command=update_employees)
mybutton4.grid(row=3,column=3)


root.mainloop()