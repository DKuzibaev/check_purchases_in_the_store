# Можно изменить на API CRM
purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]

def total_revenue(arr):
    total = 0
    for i in range(0, len(arr)):
        total += arr[i]['price'] * arr[i]['quantity']
    return total

def items_by_category(arr):
    items_category = {}
    for item in arr:
        category = item['category']
        name = item['item']
        if category not in items_category:
            items_category[category] = []
        if name not in items_category[category]:
            items_category[category].append(name)
    return items_category

def expensive_purchases(arr, min_price):
    expensive = []
    for item in arr:
        item_price = item['price']
        if item_price >= min_price:
            expensive.append(item)
    return expensive

def average_price_by_category(arr):
    category_totals = {}
    category_counts = {}
    for item in arr:
        category = item['category']
        price = item['price']
        if category not in category_totals:
            category_totals[category] = 0
            category_counts[category] = 0
        category_totals[category] += price
        category_counts[category] += 1

    average_prices = {}
    for category in category_totals:
        average = category_totals[category] / category_counts[category]
        average_prices[category] = round(average, 2)

    return average_prices

def most_frequent_category(arr):
    categories = {}

    for item in arr:
        category = item['category']
        quantity = item['quantity']
        categories[category] = categories.get(category, 0) + quantity

    return max(categories, key=categories.get)

def show_report():
    print(f"Общая выручка: {total_revenue(purchases)}")
    print(f"Товары по категориям: {items_by_category(purchases)}")
    print(f"Покупки дороже 1.0: {expensive_purchases(purchases, 1.0)}")
    print(f"Средняя цена по категориям: {average_price_by_category(purchases)}")
    print(f"Категория с наибольшим количеством проданных товаров: {most_frequent_category(purchases)}")

report_data = [
    {"metric": "Общая выручка", "value": str(total_revenue(purchases))},
    {"metric": "Товары по категориям", "value": str(items_by_category(purchases))},
    {"metric": "Покупки дороже 1.0", "value": str(expensive_purchases(purchases, 1.0))},
    {"metric": "Средняя цена по категориям", "value": str(average_price_by_category(purchases))},
    {"metric": "Самая частая категория", "value": str(most_frequent_category(purchases))},
]

show_report()
