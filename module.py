import pandas as pd
import matplotlib.pyplot as plt

def load_csv(file_path):
    try:
        data_frame = pd.read_csv(file_path)
        return data_frame
    except FileNotFoundError:
        print("File not found.")
    except Exception as error:
        print(f"Error: {error}")

def save_csv(file_path, data_frame):
    try:
        data_frame.to_csv(file_path, index=False)
    except Exception as error:
        print(f"Error: {error}")

def add_order(data_frame, client_name, order_id, order_date, order_total, order_status):
    new_entry = {"name": client_name, "order_number": order_id, "order_date": order_date, "order_price": order_total, "status": order_status}
    data_frame = data_frame._append(new_entry, ignore_index=True)
    return data_frame

def update_order(data_frame, client_name, updated_values):
    if client_name in data_frame["name"].values:
        data_frame.loc[data_frame["name"] == client_name, list(updated_values.key())] = list(updated_values.values())
        return data_frame
    else:
        print("Name not found")
        return data_frame

def remove_order(data_frame, client_name):
    if client_name in data_frame["name"].values:
        return data_frame.loc[data_frame["name"] != client_name]
    else:
        print("Name not found")
        return data_frame

def show_orders(data_frame):
    print(data_frame)

def analyze_data(order_data):
    total_orders = len(order_data)
    total_amount = order_data['order_price'].sum()
    print(f"Total count of orders: {total_orders}")
    print(f"Total price of orders: {total_amount:.2f} грн")

    status_summary = order_data['status'].value_counts()
    print("\nCount of orders by status:")
    print(status_summary)

    largest_order = order_data.loc[order_data['order_price'].idxmax()]
    print(f"\nLargest order:\n{largest_order}")

def visualize_data(order_data):
    status_summary = order_data['status'].value_counts()
    plt.figure(figsize=(6, 6))
    plt.pie(status_summary, labels=status_summary.index, autopct='%1.1f%%', startangle=140)
    plt.title("Diagram of statuses")
    plt.show()

    order_data['order_date'] = pd.to_datetime(order_data['order_date'])
    plt.figure(figsize=(10, 6))
    plt.hist(order_data['order_date'].dt.date, bins=10)
    plt.title("Diagram of orders by dates")
    plt.xlabel("Date")
    plt.ylabel("Count of orders")
    plt.xticks(rotation=45)
    plt.show()

def main_menu():
    print('-' * 25, "Menu", '-' * 25)
    print("1. Load data")
    print("2. Add order")
    print("3. Update order")
    print("4. Remove order")
    print("5. Show orders")
    print("6. Analyze data")
    print("0. Exit")

    while True:
        user_choice = input("Choise: ")

        if user_choice == '1':
            file_name = input("Choose file name: ")
            data_frame = load_csv(file_name)

            if data_frame is not None:
                print("Downloaded")
            else:
                print("Error")

        elif user_choice == '2':
            client_name = input("Enter name: ")
            try:
                order_id = int(input("Enter order number: "))
            except ValueError as error:
                print(f"Error: {error}")
                continue
            order_date = input("Enter order date: ")
            try:
                order_total = float(input("Enter order price: "))
            except ValueError as error:
                print(f"Error: {error}")
                continue
            order_status = input("Enter order status: ")
            if order_status not in ['done', 'in process']:
                print("Invalid input")
                continue
            data_frame = add_order(data_frame, client_name, order_id, order_date, order_total, order_status)
            print("Order added")

main_menu()
