def get_num_words(text):
    word_count = 0
    words = text.split()
    for word in words:
        word_count += 1
    return word_count

def get_num_chars(text):
    num_chars = {}
    chars = list(text.lower())
    for char in chars:

        if char not in num_chars:
                num_chars[char] = 1
        else:
            num_chars[char] +=1
    return num_chars

def sort_on(items):
    return items["num"]

def sorted_num_chars(char_number):
    sorted_chars = []
    for key, value in char_number.items():
        sorted_chars.append({"char": key, "num": value})
    sorted_chars.sort(reverse=True, key=sort_on)
    return sorted_chars
    



