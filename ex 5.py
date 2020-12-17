with open('new_file_ex_5.txt', 'w+') as my_file:
    line = input('Введите числа через пробел: ')
    my_file.writelines(line)
    my_numb = line.split()
print(sum(map(int, my_numb)))
