def get_prime_numbers_in_list(input_list):
    try:
        # Function to check if a number is prime
        def is_prime(num):
            if num < 2:
                return False
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    return False
            return True

        # Filter prime numbers from the input list
        primes_list = [num for num in input_list if is_prime(num)]
        #Создается новый список primes_list, который содержит только те элементы из input_list,
        # для которых функция is_prime() возвращает True.
        # Это достигается с использованием генератора списка и условия if is_prime(num).
        return primes_list

    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Example usage:
input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 27, 36, 48, 54, 67, 71, 73, 75, 83, 89, 99]
result = get_prime_numbers_in_list(input_list)
print(result)