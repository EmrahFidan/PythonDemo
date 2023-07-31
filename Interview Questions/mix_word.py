def are_words_mixable(word1, word2):
    
    for char in word2:
        if char not in word1:
            return False
    return True

# Test cases
print(are_words_mixable("izmir", "mziri"))  #*  Output: True
print(are_words_mixable("izmir", "mzira"))  #! Output: False


