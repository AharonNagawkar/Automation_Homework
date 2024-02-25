# Question 1:
my_info = {
    ('first name', 'last name'): 'Aharon Nagawkar',
    'age': 39,
    'phone number': '0543328507'
}


# Question 2:
def change_list(my_list):
    try:
        my_list[4] = '@'
        return my_list
    except IndexError as msg:
        print(msg)


print(change_list([1, 2, 3, 4]))
print(change_list([1, 2, 3, 4, 5]))
