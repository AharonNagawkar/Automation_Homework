# Question 1
my_info_list = ['Aharon', 'Nagawkar', 39, 'Ramat Gan']
for detail in my_info_list:
    print(detail)

# Question 2
list1 = [1, 2, 3, 4, 5]
list2 = [5, 4, 3, 2, 1]

if len(list1) != len(list2):
    raise Exception("List are not in the same length")

new_list = []

for i in range(len(list1)):
    new_list.append(max(list1[i], list2[i]))

print(new_list)

# Question 3
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# num_list = [1, 2, 3, 4, "Oops", 6, 7, 8, 9]
even_count = 0

for num in num_list:
    if type(num) is str:
        even_count = -1
        break
    if num % 2 == 0:
        even_count += 1

if even_count > 0:
    print(f'Number of even numbers: {even_count}')
    print(f'Number of odd numbers: {len(num_list) - even_count}')
else:
    print("It's a String!!")


# Question 4
def list_sum(int_list):
    return sum(int_list)


print(list_sum([1, 2, 3, 4]))


# Question 5
def list_product(int_list2):
    result = 1
    for fig in int_list2:
        result *= fig
    return result


print(list_product([2, 3, 2]))


# Question 6
def list_min(int_list3):
    return min(int_list3)


def list_min2(int_list3):
    smallest = int_list3[0]
    for n in range(1, len(int_list3)):
        if int_list3[n] < smallest:
            smallest = int_list3[n]
    return smallest


print(list_min([1, 2, 3, 4, 5, 6]))
print(list_min2([20, 4, 3, 4, 1, -111]))


# Question 7
def count_lower_upper(name_string):
    upper_count = 0
    lower_count = 0
    for letter in name_string:
        if letter.isupper():
            upper_count += 1
        elif letter.islower():
            lower_count += 1
    print(f'No. of Uppercase characters: {upper_count}')
    print(f'No. of Lowercase characters: {lower_count}')


count_lower_upper('Alex Kuznetsov')


# Challenge 1
def uniq_nums(list_nums):
    uniq_list = []
    for val in list_nums:
        if val not in uniq_list:
            uniq_list.append(val)
    return uniq_list


print(uniq_nums([1, 2, 3, 3, 3, 3, 4, 5]))


# Challenge 2
for i in range(1, 10):
    for j in range(1, i):
        print(j, end='')
    print(end='\n')


# Challenge 3




