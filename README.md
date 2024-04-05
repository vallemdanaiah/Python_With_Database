# Python_With_Database
Ice Cream Management System
This Python program allows users to manage ice cream inventory using a SQLite database.

Features
Add new ice cream flavors with their quantities and prices.
View all ice creams in the inventory.
Simple command-line interface.
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/your_username/icecream-management.git
Navigate to the project directory:

bash
Copy code
cd icecream-management
Install dependencies (ensure you have Python and SQLite3 installed):

Copy code
pip install sqlite3
Usage
Run the program:

Copy code
python icecream_management.py
Follow the on-screen prompts to add new ice creams or view existing ones.

Database Structure
The SQLite database used by the program contains a single table named icecream with the following columns:

id (INTEGER): Primary key auto-incremented.
flavor (TEXT): Flavor of the ice cream.
quantity (INTEGER): Quantity of the ice cream available.
price (REAL): Price of the ice cream.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

