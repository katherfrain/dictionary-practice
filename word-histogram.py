def word_histogram(sentence):
    wordhistogram = {}
    for word in sentence:
        if word == " ":
            del wordhistogram[word]
        elif word not in wordhistogram:
            wordhistogram[word] = 1
        else:
            wordhistogram[word] = wordhistogram[word] + 1
    return wordhistogram

histogram = input("Please enter a sentence for the word histogrammer: ")
histogramlist = histogram.split(" ")
print(word_histogram(histogramlist))