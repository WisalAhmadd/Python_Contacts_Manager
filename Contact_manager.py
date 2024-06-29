#from Contact import Contact
import pickle

class Contact:
    # The __init__ method initializes the attributes.
    def __init__(self, name, phone, email):
        self.__name = name
        self.__phone = phone
        self.__email = email

    # The set_name method sets the name attribute.
    def set_name(self, name):
        self.__name = name

    # The set_phone method sets the phone attribute.
    def set_phone(self, phone):
        self.__phone = phone

    # The set_email method sets the email attribute.
    def set_email(self, email):
        self.__email = email

    # The get_name method returns the name attribute.
    def get_name(self):
        return self.__name

    # The get_phone method returns the phone attribute.
    def get_phone(self):
        return self.__phone

    # The get_email method returns the email attribute.
    def get_email(self):
        return self.__email

    # The __str__ method returns the object's state as a string.
    def __str__(self):
        return "Name: " + self.__name + \
               "\nPhone: " + self.__phone + \
               "\nEmail: " + self.__email


LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

filename = 'Contacts.dat'

def main():
    mycontacts = load_contacts()
    choice = 0
    while choice!=QUIT:
        choice=get_choice()

        if choice== LOOK_UP:
            look_up(mycontacts)
        elif choice == ADD:
            add(mycontacts)
        elif choice == CHANGE:
            change(mycontacts)
        elif choice == DELETE:
            delete(mycontacts)

    save_contacts(mycontacts)




def save_contacts(contacts):
    output_file = open(filename, 'wb')
    pickle.dump(contacts, output_file)
    output_file.close()


def add(contacts):
    name = input('Name: ')
    phone = input('Phone: ')
    email = input('Email: ')

    entry = Contact(name, phone, email)

    if name not in contacts:
        contacts[name] = entry
        print('The entry has been added.')
    else:
        print('That name already exists.')


def change(contacts):
    name = input('Enter a name: ')

    if name in contacts:
     # Get a new phone number.
        phone = input('Enter the new phone number: ')

    # Get a new email address.
        email = input('Enter the new email address: ')
     # Create a contact object named entry.
        entry = Contact(name, phone, email)

    # Update the entry.
        contacts[name] = entry
        print('Information updated.')
    else:
        print('That name is not found.')



def load_contacts():
    try:
        load = open(filename,"rb")
        contacts_dct = pickle.load(load)
        load.close()
    except IOError:
        contacts_dct = {}

    return contacts_dct


def get_choice():
    print()
    print('Menu')
    print('---------------------------')
    print('1. Look up a contact')
    print('2. Add a new contact')
    print('3. Change an existing contact')
    print('4. Delete a contact')
    print('5. Quit the program')
    print()
    choice = int(input("Enter Your Choice here: "))
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input("Enter Valid Choice : "))
    return choice


def look_up(Contacts):
    name = input("Enter Nanme: ")
    print(Contacts.get(name,"That name doesn't exist"))


def delete(contacts):

    # Get a name to look up.
    name = input('Enter a name: ')

    # If the name is found, delete the entry.
    if name in contacts:
        del contacts[name]
        print('Entry deleted.')
    else:
        print('That name is not found.')

main()
