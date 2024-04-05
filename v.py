import sqlite3
# Function to create a table in the database
def create_table():
    conn = sqlite3.connect('icecream.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS icecream
                 (id INTEGER PRIMARY KEY,
                 flavor TEXT,
                 quantity INTEGER,
                 price REAL)''')
    conn.commit()
    conn.close()

# Function to insert data into the database
def insert_data(flavor, quantity, price):
    conn = sqlite3.connect('icecream.db')
    c = conn.cursor()
    c.execute('''INSERT INTO icecream (flavor, quantity, price)
                 VALUES (?, ?, ?)''', (flavor, quantity, price))
    conn.commit()
    conn.close()

# Function to retrieve data from the database
def retrieve_data():
    conn = sqlite3.connect('icecream.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM icecream''')
    data = c.fetchall()
    conn.close()
    return data

# Frontend interface
def main():
    create_table()

    while True:
        print("\n1. Add new ice cream")
        print("2. View all ice creams")
        print("3. Exit")

        choice = input("Please Enter your choice: ")

        if choice == '1':
            flavor = input("Enter flavor: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: "))
            insert_data(flavor, quantity, price)
            print("Ice cream added successfully!")
        elif choice == '2':
            data = retrieve_data()
            if len(data) == 0:
                print("No ice creams available.")
            else:
                print("\nID\tFlavor\tQuantity\tPrice")
                for row in data:
                    print(f"{row[0]}\t{row[1]}\t{row[2]}\t\t{row[3]}")
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
 main()
 