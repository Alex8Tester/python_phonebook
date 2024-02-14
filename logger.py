### Operations

from date_create import *

def create_contact():
    name = input_name()
    surname = input_surname()
    middlename = input_middlename()
    phone = input_phone()
    address = input_address()
    return f'{surname} {name} {middlename} {phone}\n{address}\n\n'
def add_contact(contact):
    with open('phonebook.txt', 'a', encoding='UTF-8') as file:
        file.write(contact)

def show_info():
    with open('phonebook.txt', 'r', encoding='UTF-8') as file:
        contact_list = file.read().rstrip().split('\n\n')
        # print(file.read().rstrip())
        for nn, contact in enumerate(contact_list, 1):
            print(nn, contact)
def search_contact():
    print(
        'Выберите вариант поиска:\n'
        '1. По фамилии\n'
        '2. По имени\n'
        '3. По отчеству\n'
        '4. По номеру телефона\n'
        '5. По адресу\n'
    )
    var_search = input('Выберите номер действия: ')

    while var_search not in ('1', '2', '3', '4', '5'):
        print('Некорректный ввод данных, попробуйте еще раз!')
        var_search = input('Выберите номер действия: ')

    index_var = int(var_search) - 1

    search = input('Введите данные для поиска: ')

    with open('phonebook.txt', 'r', encoding='UTF-8') as file:
        contact_list = file.read().rstrip().split('\n\n')

    for contact_str in contact_list:
        contact_ls = contact_str.replace('\n', ' ').split()
        if search in contact_ls[index_var]:
            print(contact_str)

def copy_contact():
    contact_list = create_list_contact()

    print_contacts(contact_list)
    print()

    num_contact_copy = int(input("Выберите номер контакта для копирования: ")) - 1
    while num_contact_copy not in range(len(contact_list)):
        print("Выран некорректный номер!")
        num_contact_copy = int(input("Выберите номер контакта для копирования: ")) - 1

    with open("phonebook_copy.txt", "a", encoding="utf-8") as file_copy:
        file_copy.write(f"{contact_list[num_contact_copy]}\n")

    print("Копирование завершено")

def create_list_contact():
    with open("phonebook.txt", "r", encoding="utf-8") as file:
        contacts_str = file.read()
    return contacts_str.rstrip().split("\n")

def print_contacts(cont_list=create_list_contact()):
    for n, contact in enumerate(cont_list, 1):
        print(n, contact)