from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title("Dropdown Menu")
root.iconbitmap('imagens/icon.ico')

# Databases

# Create a database or connect to one
conn = sqlite3.connect('address_book.db')

# Create cursor
c = conn.cursor()

# Create Table
# c.execute("""CREATE TABLE addresses (
#     first_name text,
#     last_name text,
#     address text,
#     city text,
#     state text,
#     zipcode integer
#     )""")

# Create Submit Function for database
def submit():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')

    # Create cursor
    c = conn.cursor()

    # Insert Into Table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
              {
                  'f_name': f_name.get(),
                  'l_name': last_name.get(),
                  'address': address.get(),
                  'city': city.get(),
                  'state': state.get(),
                  'zipcode': zipcode.get()
              })

    # Commit Changes
    conn.commit()

    # Close connection
    conn.close()

    f_name.delete(0, END)
    last_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

# Create a Query Function
def query():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')

    # Create cursor
    c = conn.cursor()

    # Query the database
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall() #fetchmany, fetchone
    print(records)
    print_records =  ''

    # Loop Thru Results
    for record in records:
        print_records += str(record[6]) + " | " + str(record[0]) + " " + str(record[1])  +"\n"

    query_label = Label(root, text=print_records).grid(row=8,column=0, columnspan=2)

    # Commit Changes
    conn.commit()

    # Close connection
    conn.close()

# Delete Function
def delete():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')

    # Create cursor
    c = conn.cursor()

    # Delete Record
    c.execute("DELETE FROM addresses WHERE oid=PLACEHOLDER")

    # Commit Changes
    conn.commit()

    # Close connection
    conn.close()

# Create Text Boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10,0))

last_name = Entry(root, width=30)
last_name.grid(row=1, column=1, padx=20)

address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20)

city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)

state = Entry(root, width=30)
state.grid(row=4, column=1, padx=20)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=20)

delete_input = Entry(root, width=30)
delete_input.grid(row=10,column=1)

# Create Text Boxes Labels
f_name_label = Label(root, text="First Name").grid(row=0,column=0, pady=(10,0))
last_name_label = Label(root, text="Last Name").grid(row=1,column=0)
address_label = Label(root, text="Address").grid(row=2,column=0)
city_label = Label(root, text="City").grid(row=3,column=0)
state_label = Label(root, text="State").grid(row=4,column=0)
zipcode_label = Label(root, text="Zipcde").grid(row=5,column=0)
delete_label = Label(root, text="Delete ID").grid(row=10,column=0, pady=(0,10))

# Create Submit Button
submit = Button(root, text="Add Record to Database", command=submit).grid(row=6,column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create a Query Button
query = Button(root,text="Show Records", command=query).grid(row=7,column=0, columnspan=2, pady=10, padx=10, ipadx=126)

# Delete a Query Button
delete = Button(root,text="Delete this ID", command=delete).grid(row=11,column=0, columnspan=2, pady=(0,10), padx=10, ipadx=126)



# Commit Changes
conn.commit()

# Close connection
conn.close()


root.mainloop()