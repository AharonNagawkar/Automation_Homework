# Question 1:
my_info = {
    ('first name', 'last name'): 'Aharon Nagawkar',
    'age': 39,
    'phone number': '0543328507'
}
print('Question 1:\n', my_info)


# Question 2:
def change_list(my_list):
    try:
        my_list[4] = '@'
    except IndexError as msg:
        print(msg)
    else:
        return my_list


print('\nQuestion2:')
print(change_list([1, 2, 3, 4]))
print(change_list([1, 2, 3, 4, 5]))


# Question 3:
def change_list2(my_list2):
    try:
        assert len(my_list2) > 4, 'The list is too short'
    except AssertionError as msg:
        print(msg)
    else:
        my_list2[4] = '@'
        return my_list2


print('\nQuestion3:')
print(change_list2([1, 2, 3, 4]))
print(change_list2([1, 2, 3, 4, 5]))


# Question 4:
def update_dict(c_dict, new_key, new_value):
    c_dict[new_key] = new_value
    return c_dict


print('\nQuestion4:')
print(update_dict({1: 'one', 2: 'two', 3: 'three'}, 4, 'four'))


# Question 5:
n = 5
ordered_dict = {x: x + 3 for x in range(1, n + 1)}
print('\nQuestion 5:\n', ordered_dict)


# Question 6:
