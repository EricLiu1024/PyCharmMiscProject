class restaurant():
    def __init__(self):
        self.menu_item = {}
        self.book_table = []
        self.customer_orders = []
    def Add_Menu_Item(self,item,price):
        self.menu_item[item] = price
    def Book_Table(self,table_number,customer_number):
        reservation = {'table_number':table_number,'customer_number':customer_number}
        self.book_table.append(reservation)
    def Take_Customer_Order(self,customer_name,item_name,quantity):
        order={'customer_name':customer_name,'item_name':item_name,'quantity':quantity,'total_price':quantity * self.menu_item[item_name]}
        self.customer_orders.append(order)
def main():
    A = restaurant()
    A.Add_Menu_Item('Cheeseburger',14.50)
    A.Add_Menu_Item('Margherita Pizza', 18.00)
    A.Add_Menu_Item('Caesar Salad', 12.00)
    A.Book_Table(5,'Alice Smith')
    A.Book_Table(12, 'Bob Jonson')
    A.Take_Customer_Order("Alice Smith", "Cheeseburger", 2)
    A.Take_Customer_Order("Bob Johnson", "Margherita Pizza", 1)
    A.Take_Customer_Order("Alice Smith", "Caesar Salad", 1)
    print(A.menu_item)
    print(A.book_table)
    print(A.customer_orders)
main()






#menu_items: A dictionary to store menu items with their prices.
#book_table: A list to store table reservations.
#customer_orders: A list to store customer orders.
#Add_Menu_Item: Adds a menu item with item_name and item_price.
#Book_Table: Reserves a table using table_number and customer_name.
#Take_Customer_Order: Records an order with customer_name, item_name, and quantity, calculating total_price based on item price and quantity



