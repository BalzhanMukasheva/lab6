def get_date_in_format(date):
    try:
        # Assuming the input date is in the format "yyyy.mm.dd"
        year, month, day = map(int, date.split('.'))
        formatted_date = f"{day:02d}.{month:02d}.{year}"
        return formatted_date
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage:
input_date = "2023.10.23"
result = get_date_in_format(input_date)
print(result)