import string
users_select = input(print('Введи дві літери через дефіс'))
letters = string.ascii_letters
index_1 = letters.index(users_select[0])
index_2 = letters.index(users_select[-1])
print(letters[index_1:index_2], letters [index_2], sep = '')