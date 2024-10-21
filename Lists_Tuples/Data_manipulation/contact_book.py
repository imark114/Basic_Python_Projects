# Contact Book: Create a contact book using lists of tuples. Each tuple can store a person's name, phone number, and email address. Implement functions to add, delete, and search for contacts.

def add_contact(contact_book, cntct_name, cntct_number, email_address):
    contact_book.append((cntct_name, cntct_number, email_address))

def delete_contact(contact_book, number):
    found = False
    for i, (_,cntct_number, _) in enumerate(contact_book):
        if number == cntct_number:
            contact_book.pop(i)
            found = True
            print("Sucessfully Deleted")
            break
    if not found:
        print("This Number isn't in the contact book")

def search_contact(contact_book, name):
    result = []
    for cntct_name, cntct_number, email_address in contact_book:
        if name == cntct_name:
            result.append((cntct_name, cntct_number, email_address))
    return result

contact_book = []
add_contact(contact_book,"Rakib", "01870789627", "rakib@gmail.com")
add_contact(contact_book,"Rakib", "01316593199", "rakib@gmail.com")
add_contact(contact_book,"Sakib", "01416513129", "rakib@gmail.com")
# print(contact_book)
print(search_contact(contact_book, "Rakib"))
delete_contact(contact_book, "01316593199")

