from hw_10 import *

CONTACTS = AddressBook()


def input_error(handler):
    def wrapper(*args, **kwargs):
        try:
            handler(*args, **kwargs)
        except (ValueError, IndexError, UnboundLocalError):
            print("Error. Give me correct name and phone, please")
        except KeyError:
            print("Error. Enter user name, please")
    return wrapper


def hello_handler():
    print("How can I help you?")


def quit_handler():
    print("Good bye!")
    quit()


@input_error
def change_contact_handler(var):
    name = var.split()[1]
    phone_for_change = var.split()[2]
    new_phone = var.split()[3]
    if phone_for_change.isdigit() and new_phone.isdigit():
        record = CONTACTS.data[name]
        record.change_phone(phone_for_change, new_phone)
        print("Contact was changed")


def show_contacts_handler():
    for name, record in CONTACTS.items():
        print(f"{name}: {[phone.value for phone in record.phones]}")


@input_error
def add_contact_handler(var):
    if (var.split()[1]).isalpha():
        name = var.split()[1]
    if (var.split()[2]).isdigit():
        phone = var.split()[2]
    if name in CONTACTS:
        record = CONTACTS.data[name]
        record.add_phone(phone)
    else:
        record = Record(name, phone)
        CONTACTS.add_record(record)
    print(f"New contact was added")


@input_error
def find_contact_handler(var):
    for name, record in CONTACTS.items():
        if name == var.split()[1]:
            print(f"{name}: {[phone.value for phone in record.phones]}")


@input_error
def delete_contact_handler(var):
    name = var.split()[1]
    phone_for_delete = var.split()[2]
    record = CONTACTS.data[name]
    record.delete_phone(phone_for_delete)
    print("Contact's phone was deleted")


COMMANDS = {
    "hello": hello_handler,
    "show all": show_contacts_handler,
    "exit": quit_handler,
    "close": quit_handler,
    "good bye": quit_handler
}


def main():
    while True:
        var = (input("Enter command: ")).lower()
        if var.startswith('add'):
            add_contact_handler(var)
        elif var.startswith('change'):
            change_contact_handler(var)
        elif var.startswith('phone'):
            find_contact_handler(var)
        elif var.startswith('delete'):
            delete_contact_handler(var)
        elif var not in COMMANDS:
            print("Wrong command!")
            continue
        else:
            COMMANDS[var]()


if __name__ == "__main__":
    main()