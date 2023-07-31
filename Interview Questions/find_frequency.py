def find_frequency(word):
   
    compressed_word = ""
    i = 0
    
    while i < len(word):
        char = word[i]
        j = i + 1
        frequency = 1
        
        #? Calculate the frequency of the character
        while j < len(word) and word[j] == char:
            frequency += 1
            j += 1
        
        #?  Compress the character and its frequency
        compressed_word += char + str(frequency)
        
        i = j
    
    return compressed_word


print(find_frequency("nsdkkknnndpsnırıı"))
