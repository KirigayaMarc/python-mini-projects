#Sentence fixer
original_sentence = "python is a great language. i love python."
corrected_sentence = original_sentence.replace("python", "Python")

#Takes the corrected sentence and seperates each word into a list.
word_list = corrected_sentence.split()
print(word_list)