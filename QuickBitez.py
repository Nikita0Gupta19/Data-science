import tkinter as tk
from tkinter import messagebox, simpledialog
import random

class RestaurantApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Restaurant App")
        self.geometry("900x500")
        self.config(bg='#BBE2EC')

        self.menu_items = {
            'Pizza': 150,
            'Burger': 80,
            'Coke': 20,
            'Icecream': 150,
            'Paneer Tikka': 210       
        }

        self.customer_orders = []
        self.num_of_tables_available = [1,2,3,4,5,6,7,8,9,10]
        self.num_of_tables_reserved = []  
        self.orders = {} 
        self.table = 0
        self.total_bill = 0

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Welcome to our restaurant!",font=('Algerian',30),bg='#0D9276')
        self.label.pack(pady=15)

        self.menu_button = tk.Button(self, text="View Menu",font=('Aptos',14),width=23,command=self.view_menu)
        self.menu_button.pack(pady=5)

        self.book_table_button = tk.Button(self, text="Book Table",font=('Aptos',14),bg='#637A9F',width=23,command=self.book_table)
        self.book_table_button.pack(pady=5)

        self.order_button = tk.Button(self, text="Place Order", font=('Aptos',14),width=23,command=self.place_order)
        self.order_button.pack(pady=5)

        self.total_bill_label = tk.Label(self, text="Total Bill: $0",font=('Aptos',14),width=23,bg='#637A9F')
        self.total_bill_label.pack(pady=5)

        self.exit_button = tk.Button(self, text="Exit",font=('Aptos',14),width=23,command=self.destroy)
        self.exit_button.pack(pady=5)

    def view_menu(self):
        menu_window = tk.Toplevel(self)
        menu_window.title("Menu")
        menu_window.geometry("400x200")
        menu_window.config(bg="#D2DE32")

        for item, price in self.menu_items.items():
            label = tk.Label(menu_window, text=f"{item}: ${price}",width=15)
            label.pack(pady=5)

    def book_table(self):
        if self.num_of_tables_available:
            table_number = random.choice(self.num_of_tables_available)
            self.num_of_tables_available.remove(table_number)
            self.num_of_tables_reserved.append(table_number)
            messagebox.showinfo("Table Booked", f"Table {table_number} booked successfully!")
        else:
            messagebox.showwarning("No Tables Available", "Sorry, we're fully booked")

    def place_order(self):
        order_window = tk.Toplevel(self)
        order_window.title("Place Order")
        order_window.geometry("300x200")
        order_window.config(bg="#CD8D7A")

        label = tk.Label(order_window, text="What would you like to order?",width=25)
        label.pack(pady=10)

        self.order_entry = tk.Entry(order_window)
        self.order_entry.pack(pady=10)

        self.submit_button = tk.Button(order_window, text="Submit", width=15,command=self.process_order)
        self.submit_button.pack()

    def process_order(self):
        order = self.order_entry.get().capitalize()

        if order in self.menu_items:
            quantity = simpledialog.askinteger("Quantity", f"How many {order} do you want?")
            if quantity:
                total_price = self.menu_items[order] * quantity
                self.customer_orders.append(f"{quantity} {order}(s) - Total: ${total_price}")
                self.total_bill += total_price
                self.total_bill_label.config(text=f"Total Bill: ${self.total_bill}")
                messagebox.showinfo("Order Placed", f"{quantity} {order}(s) added to your order")
        else:
            messagebox.showerror("Invalid Item", "Please select an item from the menu.")

if __name__ == "__main__":
    app = RestaurantApp()
    app.mainloop()



