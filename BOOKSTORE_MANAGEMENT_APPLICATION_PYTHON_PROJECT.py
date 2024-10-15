# Bookstore Management Application
# Data structure to store book and customer information
books = []
customers = []
sales = []
# Dummy user credentials
valid_username = "admin"
valid_password = "007"
# Function for user authentication 
def authenticate_user(username, password):
    return username == valid_username and password == valid_password
# Function to add a book
def add_book():
    book = {
        "id": input("Enter book ID: "),
        "name": input("Enter book name: "),
        "author": input("Enter book author: "),
        "price": float(input("Enter book price: ")),
        "quantity": int(input("Enter book quantity: "))
    }
    books.append(book)
    print_box_message("Book added successfully!")
# Function to remove a book
def remove_book():
    book_id = input("Enter the book ID to remove: ")
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            print_box_message("Book removed successfully!")
            return
    print_box_message("Book not found!")
# Function to add a customer
def add_customer():
    customer = {
        "name": input("Enter customer's name: "),
        "phone": input("Enter customer's phone number: "),
        "city": input("Enter customer's city: ")
    }
    customers.append(customer)
    print_box_message("Customer added successfully!")
# Function to view customer records
def view_customer_records():
    print("|" + "-"*63 + "|")
    print(f"|{'Name':<20}|{'Phone':<20}|{'City':<20}|")
    print("|" + "-"*63 + "|")
    for customer in customers:
        print(f"|{customer['name']:<20}|{customer['phone']:<20}|{customer['city']:<20}|")
    print("|" + "-"*63 + "|")
    print_box_message("Customer records displayed!")
# Function to display books
def display_books():
    print("|" + "-"*87 + "|")
    print(f"|{'ID':<10}|{'Name':<20}|{'Author':<20}|{'Price':<10}|{'Quantity':<10}|")
    print("|" + "-"*87 + "|")
    for book in books:
        print(f"|{book['id']:<10}|{book['name']:<20}|{book['author']:<20}|{book['price']:<10}|{book['quantity']:<10}|")
    print("|" + "-"*87 + "|")
    print_box_message("Books displayed!")
# Function to update a book's details
def update_book():
    book_id = input("Enter the book ID to update: ")
    for book in books:
        if book["id"] == book_id:
            book["name"] = input("Enter new book name: ")
            book["author"] = input("Enter new book author: ")
            book["price"] = float(input("Enter new book price: "))
            book["quantity"] = int(input("Enter new book quantity: "))
            print_box_message("Book updated successfully!")
            return
    print_box_message("Book not found!")
# Function to buy a book
def buy_books():
    book_id = input("Enter the book ID to buy: ")
    for book in books:
        if book["id"] == book_id:
            while True:
                quantity = int(input("Enter quantity to buy: "))
                if book["quantity"] >= quantity:
                    book["quantity"] -= quantity
                    sale = {
                                                "book_id": book["id"],
                        "book_name": book["name"],
                        "quantity": quantity,
                        "total_price": quantity * book["price"]
                    }
                    sales.append(sale)
                    print_box_message(f"{quantity} copies of {book['name']} bought successfully!")
                    break
                else:
                    print(f"Stock of books is less than you asked. Only {book['quantity']} copies available.")
            return
    print_box_message("Book not found!")
# Function to display sales report
def display_sales_report():
    print("|" + "-"*53 + "|")
    print(f"|{'Book ID':<10}|{'Book Name':<20}|{'Quantity':<10}|{'Total Price':<10}|")
    print("|" + "-"*53 + "|")
    for sale in sales:
        print(f"|{sale['book_id']:<10}|{sale['book_name']:<20}|{sale['quantity']:<10}|{sale['total_price']:<10}|")
    print("|" + "-"*53 + "|")
    print_box_message("Sales report displayed!")
# Helper function to print boxed messages
def print_box_message(message):
    message_length = len(message)
    print("|" + "-" * (message_length + 4) + "|")
    print(f"|  {message}  |")
    print("|" + "-" * (message_length + 4) + "|")
# Main function
def main():
    username = input("Enter username: ")
    password = input("Enter password: ")

    if authenticate_user(username, password):
        while True:
            print("Choose an option:")
            print("1) Add Book")
            print("2) Remove Book")
            print("3) Add Customer")
            print("4) View Customer Records")
            print("5) Display Books")
            print("6) Update Book")
            print("7) Buy Books")
            print("8) Display Sales Report")
            print("9) Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                add_book()
            elif choice == 2:
                remove_book()
            elif choice == 3:
                add_customer()
            elif choice == 4:
                view_customer_records()
            elif choice == 5:
                display_books()
            elif choice == 6:
                update_book()
            elif choice == 7:
                buy_books()
            elif choice == 8:
                                display_sales_report()
            elif choice == 9:
                break
            else:
                print_box_message("Invalid choice. Please try again.")
    else:
        print_box_message("Invalid username or password. Access denied!")
if __name__ == "__main__":
    main()
    

    
