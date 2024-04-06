import time
contact_book = {}

def add(store,name,contact,email):
    contact_book[name] = {
        'store' : store,
        'name' : name,
        'contact' : contact,
        'email' : email
    }
    print('added !!')

def search(name):
    if name in contact_book:
        print(contact_book[name])
    else:
        print('No record found !!')

def view():
    if contact_book:
        count = 1
        for key,value in contact_book.items():
            print(f'{count}.{key}:-{value}')
            count += 1
    else:
        print('empty !!')

def update(name):
    if name in contact_book:
        print('Your details')
        print(contact_book[name])
        update_store_name = input('Enter new store name:')
        update_name = input('Enter new name:')
        update_contact = input('Enter new contact:')
        update_email = input('Enter new email:')
        updated_record = {'store':update_store_name,'name':update_name,'contact':update_contact,'email':update_email}
        contact_book.update({name:updated_record})
        print('updated !!')
    else:
        print('No such record !!')

def delete(name):
    del contact_book[name]
    print('deleted !!')

ch = 'Y'
while ch.upper() == 'Y':
    print('''
    1. press 1 to add 
    2. press 2 to search
    3. press 3 to view
    4. press 4 to update
    5. press 5 to delete
    6. press 6 to exit
    ''')
    choice = int(input('Enter choice:'))
    if choice == 1:
        store = input('Enter store name:')
        name = input('Enter name:')
        contact = input('Enter contact:')
        email = input('Enter email:')
        add(store,name,contact,email)
    elif choice == 2:
        name = input('Enter your name:')
        search(name)
    elif choice == 3:
        view()
    elif choice == 4:
        name = input('Enter the name:')
        update(name)
    elif choice == 5:
        name = input('Enter the name:')
        delete(name)
    elif choice == 6:
        second = 3
        print('Exiting....')
        while second > 0:
            time.sleep(1)
            print(second)
            second -=1
        print('Exited !!')
        break
    ch = input('press Y to continue:')[0]
   