def get_prime_numbers(n):
    try:
        # Function to check if a number is prime
        def is_prime(num):
            if num < 2:
                return False
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    return False
            return True

        # Generate a list of prime numbers from 2 to n
        primes_list = [num for num in range(2, n + 1) if is_prime(num)]
        return primes_list

    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Example usage:
n = 100
result = get_prime_numbers(n)
print(result)