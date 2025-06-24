dictionary = {'Rohan': 63, "Mohan":54, "Alice":84}
ask= input("Enter the student's name: ")
if ask in dictionary:
    print(ask+"'s marks:" + str(dictionary[ask]))
else: print("Student not found.")