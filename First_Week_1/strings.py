# *6 Dealing with strings
word = "MOHAMMED FARHAN"
print(word.lower())  # converts the given string to lower case
word2 = "mohammed farhan"
print(word2.upper())  # converts the givin string to upper case

print(word.isupper())  # cheeks if the givin string is upper
print(word.islower())  # cheeks if the givin string is lower

print(word2.isupper())  # cheeks if the givin string is upper
print(word2.islower())  # cheeks if the givin string is lower

print(len(word))  # cheeks the number of charechtars in a giving string
print(word[0])  # brings back the given index of a charechtar in a string

# brings back the index of a given charechtar in a string# replaces a string for a givin string
print(word.index("M"))
print(word.replace("MOHAMMED", "KHALID"))
