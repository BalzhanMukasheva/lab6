def get_elements_with_no_more_than_two_occurrences(input_list):
    try:
        return [item for item in set(input_list) if input_list.count(item) <= 2]
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Example usage:
input_list = [1, 2, 3, 1, 2, 4]
result = get_elements_with_no_more_than_two_occurrences(input_list)
print(result)