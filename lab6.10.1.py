def get_perfect_numbers(input_list):
    try:
        def is_perfect(num):
            divisors = [i for i in range(1, num) if num % i == 0]
            return sum(divisors) == num

        perfect_numbers = [num for num in input_list if is_perfect(num)]
        return perfect_numbers

    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Example usage:
input_list = [6, 28, 12, 8, 16]
result_perfect_numbers = get_perfect_numbers(input_list)
print(result_perfect_numbers)