def get_perfect_squares(input_list):
    try:
        def is_perfect_square(num):
            return num > 0 and int(num**0.5)**2 == num

        perfect_squares = [num for num in input_list if is_perfect_square(num)]
        return perfect_squares

    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Example usage:
input_list = [4, 25, 81, 5, 16]
result_perfect_squares = get_perfect_squares(input_list)
print(result_perfect_squares)