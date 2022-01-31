while True:
    print('\n\n\n\n\n\n\n')
    print('Hello what problem is it that you want to solve? Add, subtrack, devide or multiply')
    problem = input()

    if problem == 'add' or problem == 'Add':
        print('Ok plese enter your numbers')
        num = input()
        print('Plese enter the second number')
        num2 = input()
        print(f'The result is {num} + {num2} =', int(num) + int(num2))

    elif problem == 'subtrack':
        print('Plese enter the numbers you want')
        num = input()
        print('Plese enter the second number')
        num2 = input()
        print(f'The result is {num} - {num2} =', int(num) - int(num2))

    elif problem == 'devide':
        print('Plese enter you problem')
        num = input()
        print('Plese enter your second number')
        num2 = input()
        print(f'The result is {num} / {num2} =', int(num) / int(num2))

    elif problem == 'multiply':
        print('plese enter your numbers')
        num = input()
        print('Plese enter your second number')
        num2 = input()
        print(f'the result is {num} * {num2} =', int(num) * int(num2))