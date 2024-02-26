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
    except IndexError as msg:
        print(msg)
    else:
        return my_list


# print(change_list([1, 2, 3, 4]))
# print(change_list([1, 2, 3, 4, 5]))


# Question 3:
def change_list2(my_list2):
    try:
        assert len(my_list2) > 4, 'The list is too short'
    except AssertionError as msg:
        print(msg)
    else:
        my_list2[4] = '@'
        return my_list2


print(change_list2([1, 2, 3, 4]))
print(change_list2([1, 2, 3, 4, 5]))
