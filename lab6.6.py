def get_unique_elements_with_count(input_list):
    # принимает список (input_list) и возвращает словарь,
    # в котором ключи - это уникальные элементы из списка, а значения - количество раз,
    # которое каждый элемент встречается в исходном списке.
    try:
        count_dict = {}
        for item in input_list:
            count_dict[item] = count_dict.get(item, 0) + 1
            # Если item уже присутствует в count_dict, то count_dict.get(item, 0)
            # вернет текущее значение счетчика для item, и к этому значению добавится 1
            # Если item отсутствует в count_dict, то count_dict.get(item, 0) вернет 0, и к этому 0 добавится 1,
            # устанавливая начальное значение счетчика для item равным 1..
        return count_dict
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}

# Example usage:
input_list = [1, 2, 3, 1, 2, 4, 1, 2]
result = get_unique_elements_with_count(input_list)
print(result)