def words(sentence):
    entries = {}
    list_words = sentence.split()       #Create a list of words in the sentence
    for word in list_words:             
        entries[word] = entries.get(word, 0) + 1 #finds word in the words, assign it count 0 and increment its count by 1

    items_in_words = entries.items()      #get the word, count pair of each  entry listed ie [(word1, countofword1), (word2, countofword2)]
    
    for word, count in items_in_words: #for each word and count pair we have in this list of dict_items...  
        print("%s\t:\t %d" % (word, count))

print(words('just another try of the system atha tthe progmmer deveoped'))