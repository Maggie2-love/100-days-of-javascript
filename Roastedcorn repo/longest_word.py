def longest_word(words):
    longest = ""
    for word in words:
        if len(word)>len(longest):
            longest = word
    return longest, len(longest)
words=["welcome", "out", "weather", "mobile", "breakfast", "journey"]
print(longest_word(words))

