def get_date_in_format(date):
    try:
        year, month, day = map(int, date.split('.'))
        #преобразует каждую часть в целое число с помощью map(int, ...). Это присваивает три переменные year, month и day соответственно
        formatted_date = f"{day:02d}.{month:02d}.{year}"
        #Форматирует дату, чтобы обеспечить двузначное представление дня и месяца с помощью :02d.
        # #Затем создается новая строка formatted_date в формате "день.месяц.год".
        return formatted_date
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage:
input_date = "2023.10.23"
result = get_date_in_format(input_date)
print(result)