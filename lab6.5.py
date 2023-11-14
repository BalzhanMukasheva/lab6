def get_words_from_string(input_string):
    try:
        # Split the string into a list of words
        words_list = input_string.split()
        return words_list
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Example usage:
input_string = "This a string with a several words."
result = get_words_from_string(input_string)
print(result)