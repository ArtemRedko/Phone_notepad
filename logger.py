from data_create import name_data, surname_data, phone_data, address_data


def input_data():
   name = name_data()
   surname = surname_data()
   phone = phone_data()
   address = address_data()
   var = int(input(f'В каком формате записать данные \n\n'
    f'1 вариант: \n'
    f'{name}\n{surname}\n{phone}\n{address}\n \n'
    f'2 вариант: \n'
    f'{name};{surname};{phone};{address}\n'
    f'Выберите вариант: '))
   
   while var != 1 and var != 2:
       print('Неправильный ввод')
       var = int(input('Введите вариант: '))

   if var == 1:
       with open('data_first_variant.csv', 'a', encoding = 'utf-8') as f:
           f.write(f'{name}\n{surname}\n{phone}\n{address}\n\n')
   elif var == 2:
        with open('data_second_variant.csv', 'a', encoding = 'utf-8') as f:
           f.write(f'{name};{surname};{phone};{address}\n')               



def print_data():
    print('Вывожу данные из 1 файла: \n')
    with open('data_first_variant.csv', 'r', encoding = 'utf-8') as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_list.append(''.join(data_first[j:i + 1]))
                j = i
        print(''.join(data_first_list))         
    print('Вывожу данные из 2 файла: \n')
    with open('data_second_variant.csv', 'r', encoding = 'utf-8') as f:
        data_second = f.readlines()
        print(*data_second)

def replace(file_name, line_num, text):
    data = open(file_name, 'r', encoding='utf-8').readlines()
    data[line_num] = text
    new_data = open(file_name, 'w', encoding='utf-8')
    new_data.writelines(data)

def change_data():
    print('Пожалуйста, введите новые данные!')
    name_new = name_data()
    surname_new = surname_data()
    phone_new = phone_data()
    address_new = address_data()
    print_data()
    file = int(input('Введите номер файла, в котором нужно сделать замену данных: '))
    num = int(input('Введите номер записи, которую нужно заменить: '))
    if file == 2:
        replace('data_second_variant.csv', num + num - 2, f'{name_new};{surname_new};{phone_new};{address_new}\n')    
    elif file == 1:
        replace('data_first_variant.csv', 5 * num - 5, f'{name_new}\n')       
        replace('data_first_variant.csv', 5 * num - 4, f'{surname_new}\n')
        replace('data_first_variant.csv', 5 * num - 3, f'{phone_new}\n')
        replace('data_first_variant.csv', 5 * num - 2, f'{address_new}\n')


def delete_data():
    print_data()
    file = int(input('Выберите номер файла, в котором вы хотите удалить данные: '))
    num = int(input('Выберите номер записи, которую вы хотите удалить: '))
    if file == 1:
        with open('data_first_variant.csv', 'r', encoding = 'utf-8') as f:
            data_first = f.readlines()
            del data_first[5*num-5:5*num]
        with open('data_first_variant.csv', 'w', encoding = 'utf-8') as f:
            f.writelines(data_first)
    elif file == 2:
        with open('data_second_variant.csv', 'r', encoding = 'utf-8') as f:
            data_second = f.readlines()
            del data_second[2*num-2:2*num]       
        with open('data_second_variant.csv', 'w', encoding = 'utf-8') as f:
            f.writelines(data_second)





            
    




