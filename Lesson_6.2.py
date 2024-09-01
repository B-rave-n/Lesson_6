user_number = int(input(print('Введи число від 0 до 8640000:')))
days = user_number//86400
hours = (str(user_number%86400//3600)).zfill(2)
minutes = (str(user_number%86400%3600//60)).zfill(2)
seconds = (str(user_number%86400%3600%60)).zfill(2)
day = None
if str(days)[-1] == '1' and days != 11:
    day = 'день'
elif str(days)[-1] == '2'  or str(days)[-1] == '3' or str(days)[-1] == '4':
    day = 'дні'
else:
    day = 'днів'
print(days,' ', day, ' , ', hours, ':', minutes, ':', seconds, sep = '')