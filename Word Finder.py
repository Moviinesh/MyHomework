sentence = input("Enter a sentence: ")
word = input("Enter a word in the sentence: ")

highlighted_sentence = sentence.replace(word, "\033[92m{}\033[0m".format(word.upper()))


print(highlighted_sentence)