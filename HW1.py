from math import pi

# Exercise 1:
print(
    '''
    Name: Aharon
    Last name: Nagawkar
    Age: 39
    Phone Number: 0543328507
    '''
)


# Exercise 2:
string = "Hello There"

if string[7] == 'a' and string[8] == 'b' and string[9] == 'c':
    print(True)
else:
    print(False)


# Exercise 3:
string_double = input("Type two strings, separated by space:\n")
string1 = string_double.split(" ")[0]
string2 = string_double.split(" ")[1]
print(string2[0:2]+string1[2:] + " " + string1[0:2]+string2[2:])


# Exercise 4:
str_ing_ly = input("Type some string:\n")
if len(str_ing_ly) == 3:
    pass
elif str_ing_ly[-3:] == "ing":
    str_ing_ly += "ly"
print(str_ing_ly)


# Exercise 5:
init_string = input("Insert String:\n")
string_list = list(init_string)
middle = int(len(init_string)/2)
string_list[0] = init_string[middle]
string_list[middle] = init_string[-1]
string_list[-1] = init_string[0]
print("".join(string_list))


# Exercise 6:
spaced_string = input("Insert a string with one space:\n")
added_string = input("Insert a string to add between the space")
new_string = spaced_string.replace(" ", f" {added_string} ")
print(new_string)


# Exercise 7:
unsorted_string = input("Insert your string to sort:\n")
unsorted_list = list(unsorted_string)
unsorted_list.sort()
print(unsorted_list)


# Exercise 8:
print("%.2f" % round(pi, 2))
print("%.2f" % round(12.9999, 2))


# Exercise 9:
long_string = input("Insert your text here:\n")
search_string = input("What word are you looking to count?\n")
print(long_string.count(search_string))
