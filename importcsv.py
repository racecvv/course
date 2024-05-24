import csv
from collections import defaultdict



def read_csv_file(file_path):
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file, delimiter=';')
        return list(csv_reader)

def process_row(row):
    if len(row) >= 8:
        try:
            order_id, date, product_name, category, quantity, unit_price, total_price, *rest = row
            quantity = int(quantity)
            unit_price = float(unit_price)
            total_price = float(total_price)
            return order_id, date, product_name, category, quantity, unit_price, total_price
        except ValueError:
            pass  # Пропускаем строку, если преобразование в число не удалось
    return None

def generate_sales_report(data):
    product_sales = defaultdict(int)
    product_revenue = defaultdict(float)
    
    for row in data:
        if row:
            product_name = row[2]
            quantity = row[4]
            total_price = row[6]
            
            product_sales[product_name] += quantity
            product_revenue[product_name] += total_price
    
    total_revenue = sum(product_revenue.values())
    
    print("Sales Report:")
    print("----------------")
    print(f"Total store revenue: {total_revenue:.2f} rubles")
    print("\nProducts sold the most:")
    most_sold_product = max(product_sales, key=product_sales.get)
    print(f"{most_sold_product}: {product_sales[most_sold_product]} units")
    
    print("\nProducts with the highest revenue:")
    highest_revenue_product = max(product_revenue, key=product_revenue.get)
    print(f"{highest_revenue_product}: {product_revenue[highest_revenue_product]:.2f} rubles")
    
    print("\nDetailed report:")
    for product, quantity in product_sales.items():
        revenue = product_revenue[product]
        print(f"{product} | {quantity} units | {revenue:.2f} rubles")
    
    print("----------------")

def main():
    file_path = 'C:\\code\\sales_data.csv'
    data = read_csv_file(file_path)
    
    processed_data = [process_row(row) for row in data[1:]]  # Пропускаем заголовок
    
    generate_sales_report(processed_data)

if __name__ == "__main__":
    main()