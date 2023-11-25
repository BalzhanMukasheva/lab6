def get_keys_with_value_true(input_dict):
    try:
        return [key for key, value in input_dict.items() if value is True]
    #используется для итерации по всем парам ключ-значение в переданном словаре
    #мы проходим по каждой паре ключ-значение в словаре, и если значение равно True
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


# Example usage:
input_dict = {
    "a": True,
    "b": False,
    "c": True
}

result = get_keys_with_value_true(input_dict)
print(result)