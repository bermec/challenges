lines = int(input())
stop_words = ["i", "a", "about", "an", "and", "are", "as", "at",
              "be", "by", "com", "for", "from", "how", "in", "is",
              "it", "of", "on", "or", "that", "the", "this", "to",
              "was", "what", "when", "where", "who", "will", "with",
              "the"]


def find_alliteration(sentence):
    alliterated_words = []
    words = str(sentence).lower().split(" ")
    words = list(filter(lambda word: word not in stop_words, words))

    letter = ""
    for index, word in enumerate(words):
        print(index, word)
        if word[0] is letter:
            alliterated_words.append(word)
        elif len(words) > index + 1:
            if words[index + 1][0] == word[0]:
                alliterated_words.append(word)
        letter = word[0]

    return alliterated_words

for i in range(lines):
    sentence = input()
    print(find_alliteration(sentence))