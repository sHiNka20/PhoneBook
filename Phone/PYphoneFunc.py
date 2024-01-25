CONTACTS = 'Contacts.txt'
CONTACTS2 = 'Contacts2.txt'

def print_contacts(file_name):
    with open(file_name, 'r', encoding = 'utf8') as file:
        all_cont = file.readlines()
        if len(all_cont) != 0:
            for line in all_cont:
                print(line.strip(), end = '\n\n')
        else:
            print('\nСписок контактов пустой.')
            
def connect_with_user():
    print('Введите имя, фамилию и телефон (Например Иван Иванов 89238765988) : ')
    cont_info = input()
    return cont_info
            
def add_contacts(file_name):
    with open(file_name, 'r', encoding = 'utf8') as file:
        all_cont = file.readlines()
        new_info = connect_with_user()
        all_cont.append('\n' + new_info)
    with open(file_name, 'w', encoding = 'utf8') as file:
        file.writelines(all_cont)
        
def find_contact(file_name):
    with open(file_name, 'r', encoding = 'utf8') as file:
        all_cont = file.readlines()
        
    print('Выберите критерий для поиска :\
        \n 1 - Имя\
        \n 2 - Фамилия\
        \n 3 - Номер телефона')
    
    comm = int(input())
    
    print('\nВведите строку для поиска :')
    data = input()
    print('\nНайденные контакты :')
        
    for cont in all_cont:
        cont_as_list = cont.strip().split()
        if data in cont_as_list[comm - 1]:
            print(*cont_as_list,'\n')
    print('Введите :\
          \n 1 - Удалить контакт по номеру телефона\
          \n 2 - Вернуться в меню')
    command = int(input())
    match command:
        case 1:
            del_cont(CONTACTS)
        case 2:
            pass
            
def del_cont(file_name):
    print('Введите номер телефона, который хотите удалить :')
    tel_data = input()
    with open(file_name, 'r', encoding = 'utf8') as file:
        all_cont = file.readlines()
    with open(file_name, 'w', encoding = 'utf8') as file:
        for cont in all_cont:
            cont_as_list = cont.strip().split()
            if tel_data != cont_as_list[2]:
                file.write(cont)
                
def copy_text(file_name, second_file_name):
    i = 0
    print('Введите номер строки которую хотите скопировать :')
    stroka = int(input())
    with open(file_name, 'r', encoding = 'utf8') as file:
        all_cont = file.readlines()
        while i < len(all_cont):
            if all_cont[stroka - 1] == all_cont[i]:
                with open(second_file_name, 'r', encoding = 'utf8') as file:
                    all_cont2 = file.readlines()
                    all_cont2.append(all_cont[i])
                with open(second_file_name, 'w', encoding = 'utf8') as file:
                    file.writelines(all_cont2)
                i = i + 1
            i = i + 1