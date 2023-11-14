def get_unique_elements_with_count(input_list):
    try:
        # Using a dictionary to count occurrences of each element
        count_dict = {}
        for item in input_list:
            count_dict[item] = count_dict.get(item, 0) + 1
        return count_dict
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}

# Example usage:
input_list = [1, 2, 3, 1, 2, 4, 1, 2]
result = get_unique_elements_with_count(input_list)
print(result)