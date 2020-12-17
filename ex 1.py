f_obj = open('new_file_ex_1.txt', 'w')
while True:
    data = input('Укажите данные для ввода: ')
    if data == '':
        break
    f_obj.write(data+'\n')
f_obj = open('new_file_ex_1.txt', 'r')
content = f_obj.read()
print(content)
f_obj.close()
