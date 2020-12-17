my_file = open('new_file_ex_1.txt', 'r')
data = my_file.readlines()
print(f'Количество строк - {len(data)}')
for i in range(len(data)):
    print(f'Окличество символов, строка № {i + 1}: {len(data[i])}')
my_file.close()
