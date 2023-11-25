def get_words_from_string(input_string):
    #принимает строку (input_string) и возвращает список слов, разделенных пробелами.
    try:
        words_list = input_string.split()
        return words_list
    #строки input_string на подстроки (слова), используя пробелы в качестве разделителей.
    #Результат этой операции сохраняется в переменной words_list.
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Example usage:
input_string = "This a string with a several words."
result = get_words_from_string(input_string)
print(result)