# *5 Reading/Writing Files
file = open("Second_Week_1\\rwfiles\\names.txt", "r")
print(file.read())  # Reads The whole File
file.close
# ****************************
file = open("Second_Week_1\\rwfiles\\names.txt", "a")
print(file.write("Hamad"))  # adds the givin value to the ednf of the string
file.close
