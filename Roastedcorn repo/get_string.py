def get_string(word):
    if len(word)<2:
        return""
    else:
        return word[:2] + word[-2:]

print( get_string("magdalene"))
