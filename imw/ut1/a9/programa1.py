import sys


def num_vowels(text):
    vowels = "aeiou"
    count = 0
    lowercase = text.lower()  # si no se hace esto no contará las mayúsculas

    for char in lowercase:
        if char in vowels:
            count += 1
    return count


def num_whitespaces(text):
    count = 0
    for whitespace in text:
        if whitespace == " ":
            count += 1
    return count


def num_digits(text):
    digits = "123456789"
    count = 0
    for num in text:
        if num in digits:
            count += 1
    return count


def num_words(text):
    abecedary = "abcdefghijklmnñopqrstuvwxyz"
    count = 0
    lowercase = text.lower()
    for abc in lowercase:
        if abc in abecedary:
            count += 1
    return count


def reverse(text):
    rev = text[::-1]
    return rev


def length(text):
    size = len(text)
    return size


def halfs(text):
    subtext = int(len(text) / 2)
    subtext1 = text[:int(subtext)]
    subtext2 = text[int(subtext):]
    return subtext1 + "|" + subtext2  # Los + hacen una concatenación


def upper_vowels(text):
    vowels = "aeiou"
    uppvowels = ""
    for char in text:
        if char in vowels:
            uppvowels += char.upper()
        else:
            uppvowels += char
    return uppvowels


def sorted_by_words(text):
    word = text.split()
    wordlist = sorted(word)
    wordlistspaced = " ".join(wordlist)
    return wordlistspaced


def length_of_words(text):
    word = text.split()
    wordlist = list()
    size = len(word)
    for var in range(size):
        value = len(word[var])
        wordlist.append(str(value))
    size_words = " ".join(wordlist)
    return size_words


text = sys.argv[1]
print("Number of vowels: ", num_vowels(text))
print("Number of whitespaces: ", num_whitespaces(text))
print("Number of digits: ", num_digits(text))
print("Number of words: ", num_words(text))
print("Reverse of text: ", reverse(text))
print("Length of text: ", length(text))
print("Halfs of text: ", halfs(text))
print("Text with uppercased vowels: ", upper_vowels(text))
print("Sorted by words: ", sorted_by_words(text))
print("Length of words: ", length_of_words(text))
