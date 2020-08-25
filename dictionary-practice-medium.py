def letter_histogram(strang):
    strang.lower()
    strang.strip()
    letterhistogram = {}

    for letter in strang:
        if letter not in letterhistogram: 
            #now make this the unique letter so we can see if there's only one of it
            letterhistogram[letter] = 1
        else:
            #but if the letter and the 'unique' letter are the same, add to the lettercounter
            letterhistogram[letter] = letterhistogram[letter] + 1
    return letterhistogram
        
stringaling = input("What would you like to put into the histogram today? ")
print(letter_histogram(stringaling))