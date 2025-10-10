# Contact Book

# empty dict
contact = {}

# infinite loop
while True:
    print('\n-- Contact Book --')
    print('My Contact Application')
    print('1- Create contact')
    print('2- View contact')
    print('3- Update contact')
    print('4- Delete contact')
    print('5- Count contact list')
    print('6- Search contact')
    print('7- Exit from contact book')

    user_choice = int(input("Enter your choice here: "))

    # Step 1: Create contact
    if user_choice == 1:
        user_name = input("Enter a name here: ")
        if user_name in contact:
            print(f'Name {user_name} is already in contact list.')
        else:
            age = int(input("Enter age: "))
            email = input("Enter E-mail: ")
            mobile = input('Enter mobile number: ')
            contact[user_name] = {'age': age, 'email': email, 'mobile': mobile}
            print(f"Contact for {user_name} added successfully.")

    # Step 2: View contact
    elif user_choice == 2:
        if not contact:
            print("Contact list is empty.")
        else:
            for name, details in contact.items():
                print(f"\nName: {name}")
                print(f"Age: {details['age']}")
                print(f"Email: {details['email']}")
                print(f"Mobile: {details['mobile']}")

    # Step 3: Update contact
    elif user_choice == 3:
        user_name = input("Enter the name of the contact to update: ")
        if user_name in contact:
            age = int(input("Enter new age: "))
            email = input("Enter new E-mail: ")
            mobile = input("Enter new mobile number: ")
            contact[user_name] = {'age': age, 'email': email, 'mobile': mobile}
            print(f"Contact for {user_name} updated successfully.")
        else:
            print(f"No contact found with name {user_name}.")

    # Step 4: Delete contact
    elif user_choice == 4:
        user_name = input("Enter the name of the contact to delete: ")
        if user_name in contact:
            del contact[user_name]
            print(f"Contact for {user_name} deleted successfully.")
        else:
            print(f"No contact found with name {user_name}.")

    # Step 5: Count contact list
    elif user_choice == 5:
        print(f"Total contacts: {len(contact)}")

    # Step 6: Search contact
    elif user_choice == 6:
        user_name = input("Enter the name of the contact to search: ")
        if user_name in contact:
            details = contact[user_name]
            print(f"\nName: {user_name}")
            print(f"Age: {details['age']}")
            print(f"Email: {details['email']}")
            print(f"Mobile: {details['mobile']}")
        else:
            print(f"No contact found with name {user_name}.")

    # Step 7: Exit
    elif user_choice == 7:
        print("Exiting Contact Book. Goodbye!")
        break

    # Invalid choice
    else:
        print("Invalid choice")