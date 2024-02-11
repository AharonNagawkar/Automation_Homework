# Exercise 1
print('Exercise 1:')
name = input('Enter your full name:\n')
print(name[::-1], '\n')


# Exercise 2
print('Exercise 2:')
name = input('Enter your name again:\n')
split_name = name.split(' ')
print(split_name[0][0].upper() + '.' + split_name[1][0].upper() + '.', '\n')


# Exercise 3
print('Exercise 3:')
string1 = input('Enter the first string:\n')
string2 = input('Enter the second string:\n')
print(string2.lower() == string1.lower(), '\n')

# Exercise 4
print('Exercise 4:')
for number in range(1, 20):
    if number % 3 == 0 and number % 5 == 0:
        print('FizzBuzz')
    elif number % 3 == 0:
        print('Fizz')
    elif number % 5 == 0:
        print('Buzz')
    else:
        print(number)
print('\n')


# Exercise 5
print('Exercise 5:')
user_string = input('Enter your sentence here:\n')
if 'python' in user_string.lower():
    print('Contains Python\n')
else:
    print('Does not contain Python\n')


# Exercise 6
print('Exercise 6:')
x = 1
while x < 100:
    print(x)
    x *= 2
print('\n')


# Exercise 7
print('Exercise 7:')
numbers = []
for _ in range(5):
    numbers.append(input('Enter a number:'))
print(f'The largest number is: {max(numbers)}\n')


# Exercise 8
print('Exercise 8:')
squares = [val**2 for val in range(1, 11)]
print(squares[::-1], '\n')


# Exercise 9
print('Exercise 9:')
n = int(input('Enter number of rows:'))
for row in range(1, n+1):
    spaces = n - row
    stars = 2*row - 1
    print(" " * spaces, end='')
    print("*" * stars)
