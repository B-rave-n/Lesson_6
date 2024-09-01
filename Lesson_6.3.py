number = int(input(print('Введи число:')))
while number > 9:
    result = 1
    for i in str(number):
        result *= int(i)
        number = result
print(number)
