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
num_list =  [1, 2, 3, 4, 5, 6, 7, 8, 9]
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

