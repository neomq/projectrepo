print('''
**********************************
** Welcome to Simple Calculator **
**********************************
''')

operation = input('''
Enter the number of the operation you would like to perform:
[1] addition
[2] subtraction
[3] multiplication
[4] division
''')

first_num = int(input('Enter your first number: '))
second_num = int(input('Enter your second number: '))

if operation == '1':
    # Addition
    result_addition = first_num + second_num
    print('{} + {} = {}'.format(first_num, second_num, result_addition))

elif operation == '2':
    # Subtraction
    result_subtraction = first_num - second_num
    print('{} + {} = {}'.format(first_num, second_num, result_subtraction))

elif operation == '3':
    # Multiplication
    result_multiplication = first_num * second_num
    print('{} + {} = {}'.format(first_num, second_num, result_multiplication))

elif operation == '4':
    # Division
    result_division = first_num / second_num
    print('{} + {} = {}'.format(first_num, second_num, result_division))

else:
    print('Option does not exist')
