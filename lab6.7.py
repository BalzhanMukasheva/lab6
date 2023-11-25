def get_prime_numbers(n):
    # Этот код определяет функцию get_prime_numbers, которая принимает число n и возвращает список простых чисел от 2 до n.
    try:
        def is_prime(num):
            if num < 2:
                # Простые числа, по определению, больше 1, и числа меньше 2 не являются простыми.
                return False
            for i in range(2, int(num**0.5) + 1):
                # если num делится на какое-либо число больше его квадратного корня,
                # то оно также делится на число меньше его квадратного корня.
                if num % i == 0:
                    #Если условие выполняется, то num не является простым числом,
                    #потому что найден делитель отличный от 1 и самого num.
                    return False
            return True

        primes_list = [num for num in range(2, n + 1) if is_prime(num)]
        #простые числа от 2 до n. Используется генератор списка, включающий в список только те числа,
        #для которых функция is_prime() возвращает True.
        return primes_list

    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Example usage:
n = 100
result = get_prime_numbers(n)
print(result)