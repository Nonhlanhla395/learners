from tkinter import *
from tkinter import messagebox
import mysql.connector

# Database connection
conn = mysql.connector.connect(host="localhost", user="Nonhlanhla", password="Mbube123@", database="cbi")
c = conn.cursor()

root = Tk()

# Entry fields for employee data
employee_id = Entry(root)
employee_id.grid(row=1, column=0)
first_name = Entry(root)
first_name.grid(row=1, column=1)
surname = Entry(root)
surname.grid(row=1, column=2)
salary = Entry(root)
salary.grid(row=1, column=3)

# Labels for the entry fields
Label(root, text="Enter employee ID:").grid(row=0, column=0)
Label(root, text="Enter first name:").grid(row=0, column=1)
Label(root, text="Enter surname:").grid(row=0, column=2)
Label(root, text="Enter salary:").grid(row=0, column=3)

def add_employees():
    emp_id = employee_id.get()
    name = first_name.get()
    surnm = surname.get()
    salry = salary.get()

    if not emp_id or not name or not surnm or not salry:
        messagebox.showwarning("Input Error", "Please fill all fields.")
        return

    try:
        query = "INSERT INTO employees (employee_id, first_name, surname, salary) VALUES (%s, %s, %s, %s)"
        c.execute(query, (emp_id, name, surnm, salry))
        conn.commit()
        messagebox.showinfo("", "Employee has been added successfully")
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", str(err))

def view_employees():
    try:
        query = "SELECT * FROM employees"
        c.execute(query)
        result = c.fetchall()
        if result:
            for row in result:
                messagebox.showinfo("", f"ID: {row[0]}, Name: {row[1]}, Surname: {row[2]}, Salary: {row[3]}")
        else:
            messagebox.showinfo("", "No employees found.")
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", str(err))

def update_employees():
    emp_id = employee_id.get()
    name = first_name.get()
    surnm = surname.get()
    salry = salary.get()

    try:
        if name:
            c.execute("UPDATE employees SET first_name = %s WHERE employee_id = %s", (name, emp_id))
        if surnm:
            c.execute("UPDATE employees SET surname = %s WHERE employee_id = %s", (surnm, emp_id))
        if salry:
            c.execute("UPDATE employees SET salary = %s WHERE employee_id = %s", (salry, emp_id))
        conn.commit()
        messagebox.showinfo("", "Employee updated successfully")
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", str(err))

def del_employee():
    emp_id = employee_id.get()

    if not emp_id:
        messagebox.showwarning("Input Error", "Please enter an employee ID.")
        return

    try:
        c.execute("DELETE FROM employees WHERE employee_id = %s", (emp_id,))
        conn.commit()
        messagebox.showinfo("", "Deleted successfully")
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", str(err))

# Buttons for actions
Button(root, text="Add", command=add_employees).grid(row=3, column=0)
Button(root, text="Delete", command=del_employee).grid(row=3, column=1)
Button(root, text="Display", command=view_employees).grid(row=3, column=2)
Button(root, text="Update", command=update_employees).grid(row=3, column=3)

root.mainloop()
