def sort_by_price(shopping_list):
    try:
        sorted_list = sorted(shopping_list, key=lambda x: x['price'])
        return sorted_list

    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Example usage:
shopping_list = [
    {"name": "Apple", "price": 100},
    {"name": "Banana", "price": 50},
    {"name": "Orange", "price": 20}
]

result_sorted_list = sort_by_price(shopping_list)
print(result_sorted_list)