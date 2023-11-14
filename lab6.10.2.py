def get_decimal_number_from_binary_string(binary_string):
    try:
        decimal_number = int(binary_string, 2)
        return decimal_number

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage:
binary_string = "10110011"
result_decimal_number = get_decimal_number_from_binary_string(binary_string)
print(result_decimal_number)