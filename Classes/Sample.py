import sqlite3
#from employee import Employee

# conn = sqlite3.connect(':memory:') #memory
conn = sqlite3.connect('employee.db') #database itselft

c = conn.cursor() #cursor 

#DECLARATION OF THE TABLE
# c.execute("""CREATE TABLE employees (
#         first text,
#         last text,
#         pay integer
#         )""")

#DECLARING SOME FUNCTIONS
def insert_emp(emp):
        with conn:
                c.execute("INSERT INTO employees VALUES (?, ?, ?)", (emp.first, emp.last, emp.pay))


def get_emp_by_name(lastname):
        c.execute("SELECT * FROM employees WHERE last = ?", (lastname, ))
        return c.fetchone()

def update_pay(name, surname, pay):
        with conn:
                c.execute("""UPDATE employees SET pay = :pay
                             WHERE first = :first AND last = :last""",
                        {'first':name, 'last':surname, 'pay': pay})

def remove_emp(name, surname):
        with conn:
                c.execute("DELETE FROM employees WHERE first = :first AND last = :last",
                        {'first':name, 'last':surname})

#STUDY AND STATEMENTS LEARNED TO DO THE FUNCTIONS

#c.execute("DELETE FROM employees WHERE first = 'Corey'")
#c.execute("INSERT INTO employees VALUES ('Corey', 'Schafer', 50000)")


#STATEMENTS
# c.execute("INSERT INTO employees VALUES (?, ?, ?)", (emp_1.first, emp_1.last, emp_1.pay))
# conn.commit()

# c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first':emp_2.first, 'last':emp_2.last, 'pay':emp_2.pay})
# conn.commit()

# c.execute("SELECT * FROM employees WHERE last = ?", ('Schafer', ))

# print(c.fetchall())#it returns the row if it exists, and none if it doesnt exist

# c.execute("SELECT * FROM employees WHERE last = :last", {'last': 'Doe'})

# print(c.fetchall())#it returns the row if it exists, and none if it doesnt exist

# conn.commit()

#DECLARING TWO NEW ITEMS TO THE DB
#emp_1 = Employee('Bruno', 'Zimmer', 80000)
# emp_2 = Employee('Jone', 'Doe', 80000)

#insert_emp(emp_1)
# insert_emp(emp_2)

# emps = get_emps_by_name('Doe')
# print(emps)

# update_pay(emp_2, 95000)

# emp1 = get_emp_by_name('Zimmer')
# print(emp1)
# update_pay(emp1[0],emp1[1], 95000)
# emp1 = get_emp_by_name('Zimmer')
# print(emp1)

# conn.close()