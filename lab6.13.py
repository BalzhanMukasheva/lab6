def get_words_starting_with_vowel(words):
    try:
        vowel_words = [word for word in words if word[0].lower() in 'aeiou']
        # проходит по каждому слову в списке\добавляет слова в новый список\если первая буква слова гласные буквы
        return vowel_words

    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Example usage:
word_list = ["apple", "banana", "orange", "bear", "cat"]
result_vowel_words = get_words_starting_with_vowel(word_list)
print(result_vowel_words)
