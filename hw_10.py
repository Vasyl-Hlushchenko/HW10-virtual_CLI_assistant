from collections import UserDict


class AddressBook(UserDict):
    #Класс AddressBook, который наследуется от UserDict, и мы потом добавим логику поиска по записям в этот класс.
    def add_record(self, record):
        self.data[record.name.value] = record


class Record:
    #Класс Record, который отвечает за логику добавления/удаления/редактирования необязательных полей и хранения обязательного поля Name.
    def __init__(self, name, phone = None):
        self.name = Name(name)
        self.phone = Phone(phone)
        if Phone(phone):
            self.optional_objects = [Phone(phone)]
        else:
            self.optional_objects = []

    def add_phone(self, phone):
        self.optional_objects.append(Phone(phone))

    def delete_phone(self, phone_for_delete):
        for phone in self.optional_objects:
            if phone.value == phone_for_delete:
                self.optional_objects.remove(phone)

    def change_phone(self, phone_for_change, new_phone):
        for index, phone in enumerate(self.optional_objects):
            if phone.value == phone_for_change:
                self.optional_objects[index] = Phone(new_phone)


class Field:
    #Класс Field, который будет родительским для всех полей, в нем потом реализуем логику общую для всех полей.
    def __init__(self, value):
        self.value = value


class Name(Field):
    #Класс Name, обязательное поле с именем.
    pass
    

class Phone(Field):
    #Класс Phone, необязательное поле с телефоном и таких одна запись (Record) может содержать несколько.
    pass