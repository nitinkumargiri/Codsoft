import json

# File to store the contact book
CONTACTS_FILE = "contacts.json"

# Load contacts from the file
def load_contacts():
    try:
        with open(CONTACTS_FILE, 'r') as file:
            contacts = json.load(file)
        return contacts
    except FileNotFoundError:
        return {}

# Save contacts to the file
def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact(contacts):
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email address: ")

    contacts[name] = {'phone': phone, 'email': email}
    save_contacts(contacts)
    print(f"Contact for {name} added successfully!")

# View all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
    else:
        print("\nContacts List:")
        for name, info in contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}")
            print("-" * 20)

# Delete a contact
def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"Contact for {name} deleted successfully!")
    else:
        print(f"No contact found with the name: {name}")

# Main program loop
def main():
    contacts = load_contacts()

    while True:
        print("\nContact Book Menu:")
        print("1. Add a contact")
        print("2. View all contacts")
        print("3. Delete a contact")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            delete_contact(contacts)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

# Run the program
if __name__ == "__main__":
    main()
