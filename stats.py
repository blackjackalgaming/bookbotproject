def get_num_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    text = text.lower()
    char_counts = {}

    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts
    
def count_words(text):
    text = text.lower()
    words = text.split()

    word_counts = {}

    for word in words:
        word = word.strip(".,!?;:\"()[]")

        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts
    
def get_top_words(word_counts, n=10):
    word_list = []

    for word in word_counts:
        word_list.append({
            "word": word,
            "num": word_counts[word]
        })

    word_list.sort(reverse=True, key=lambda item: item["num"])

    return word_list[:n]

def sort_characters(char_counts):
    char_list = []

    for char in char_counts:
        if char.isalpha():
            char_list.append({
                "char": char,
                "num": char_counts[char]
            })

    char_list.sort(reverse=True, key=sort_on)
    return char_list


def sort_on(item):
    return item["num"]