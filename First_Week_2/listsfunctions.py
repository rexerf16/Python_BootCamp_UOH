# *5 Lists functions

numbers = [1, 2, 3, 4, 5]
friends = ["Hamood", "Abdullah", "Mohammed", "Hamed", "khalaf"]
friends.extend(numbers)  # combines the lists
print(friends)
friends.append("Talal")  # addiing a value the to the end of the list
print(friends)
friends.insert(1, "Zamil")  # adding a value by index
print(friends)
friends.remove("khalaf")  # removing a given element by string
print(friends)
# friends.clear()  # to remove all elemnets in the list
print(friends)
friends.pop()  # remove the last elemnt is a givin list
print(friends)
print(friends.index("Zamil"))  # to find an elemnt index
# to count how many times the elemnt exists in the list
print(friends.count("Mohammed"))
# print(friends.sort())  # to sort the elemnts in order
print(friends.reverse())  # to reverse the order of a list
friends2 = friends.copy()  # to copy elemnts from one list to an other
print(friends2)
