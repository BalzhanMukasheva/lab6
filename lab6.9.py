from datetime import datetime

def get_difference_between_dates(date1, date2):
    try:
        date1_obj = datetime.strptime(date1, "%Y.%m.%d")
        #Формат строки "%Y.%m.%d" указывает, как должна быть представлена дата в строке.
        date2_obj = datetime.strptime(date2, "%Y.%m.%d")
        date_difference = (date2_obj - date1_obj).days
        #Рассчитывает разницу между двумя датами в виде объекта
        return abs(date_difference)

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage:
date1 = "2023.10.23"
date2 = "2023.10.24"
result = get_difference_between_dates(date1, date2)
print(result)