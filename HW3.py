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
def concatenate_dicts(*dicts):
    final_dict = {}
    for item in dicts:
        final_dict.update(item)
    return final_dict


print("\nQuestion 6:\n", concatenate_dicts({1: 10, 2: 20}, {3: 30, 4: 40}, {5: 50, 6: 60}))


# Question 7:
def count_chars(test_string):
    letters_dict = {}
    for char in test_string.upper():
        letters_dict[char] = letters_dict.get(char, 0) + 1
    return letters_dict


print("\nQuestion 7:\n", count_chars('HANNA'))


# Question 8:
def combine_dict(*diff_dicts):
    uniq_keys = set()
    for dictionary in diff_dicts:
        uniq_keys.update(set(dictionary.keys()))
    combined_dict = {}
    for key in sorted(uniq_keys):
        value = 0
        for dictionary in diff_dicts:
            value += dictionary.get(key, 0)
            combined_dict[key] = value
    return combined_dict


d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}
d3 = {'a': 100, 'b': 100, 'f': 500}
d4 = {'a': 50, 'b': 50, 'f': 50, 'g': 50}
print('\nQuestion 8:\n', combine_dict(d1, d2, d3, d4))


# Challenge 1:
def factorial(num):
    if num == 1:
        return 1
    else:
        return factorial(num - 1) * num


print('\nChallenge 1:\n', factorial(5))


# Challenge 2:
def series_sum(num):
    if num == 0:
        return 0
    return num + series_sum(num-1)


print('\nChallenge 2:\n', series_sum(4))


# Challenge 3:
def exponent(base, power):
    if power == 0:
        return 1
    else:
        return base * exponent(base, power - 1)


print('\nChallenge 3:\n', exponent(2, 10))

