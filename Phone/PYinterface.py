from PYphoneFunc import *

CONTACTS = 'Contacts.txt'
CONTACTS2 = 'Contacts2.txt'

def interface():
    while True:
        print('Выберете действие : \
              \n 1 - Добавить контакт. \
              \n 2 - Вывести все контакты. \
              \n 3 - Найти контакт. \
              \n 4 - Удалить контакт по номеру телефона.\
              \n 5 - Копировать контакт в другой файл.\
              \n 0 - Выйти. ')
        command = int(input())
        match command:
            case 0:
                break
            case 1:
                add_contacts(CONTACTS)
            case 2:
                print_contacts(CONTACTS)
            case 3:
                find_contact(CONTACTS)
            case 4:
                del_cont(CONTACTS)
            case 5:
                copy_text(CONTACTS, CONTACTS2)
            case _:
                print('Неверная команда!')

if __name__ == '__main__':
    interface()
