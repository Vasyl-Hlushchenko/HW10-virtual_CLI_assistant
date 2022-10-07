from collections import UserDict


class AddressBook(UserDict):
    #Класс AddressBook, который наследуется от UserDict, и мы потом добавим логику поиска по записям в этот класс.
    def add_record(self):
        self.data[Record.name.value] = Record


class Record:
    #Класс Record, который отвечает за логику добавления/удаления/редактирования необязательных полей и хранения обязательного поля Name.
    def __init__(self, name, phone=None):
        self.name = Name(name)
        self.phone = Phone(phone)
        if phone:
            self.optional_objects = [self.phone]
        else:
            self.optional_objects = []

    def add_phone(self, phone):
        return self.optional_objects.append(self.phone)

    def delete_phone(self, phone):
        if self.phone in self.optional_objects:
            self.optional_objects.remove(self.phone)

    def change_phone(self, phone, new_phone):
        if self.phone in self.optional_objects:
            self.optional_objects[self.optional_objects.index(self.phone)] = Phone(new_phone)


class Field:
    #Класс Field, который будет родительским для всех полей, в нем потом реализуем логику общую для всех полей.
    pass


class Name(Field):
    #Класс Name, обязательное поле с именем.
    def __init__(self, name):
        self.name = name
    

class Phone(Field):
    #Класс Phone, необязательное поле с телефоном и таких одна запись (Record) может содержать несколько.
    def __init__(self, phone=None):
        self.phone = phone