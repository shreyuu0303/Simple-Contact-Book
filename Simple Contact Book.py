
contacts = []
print("Simple Contact Book")
def add_contact():
    name=input("enter name:")
    phone=int(input("enter phone num :"))
    email=input("enter emmail :")
    contact={"name":name,"phone":phone,"email":email}
    contacts.append(contact)
    print("✅ Contact added!")

def view_contact():
    if not contacts:
        print("❌ No contacts yet.")
    else:
        print("\n📒 Contact List:")
        for c in contacts:
            print(f"Name:{c['name']},Phone_Num:{c['phone']},Email_id: {c["email"]}")

def Search_name():
    Search=input("Enter name to search: ")
    found = False
    for c in contacts:
        if c["name"].lower()==Search.lower():
            print(f"🔎 Found: Name: {c['name']}, Phone: {c['phone']}, Email: {c['email']}")
            found=True
    if not found:
        print("❌ Contact not found.")


def show_menu():
    while True:
        print("\n--- Contact Book ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice==1:
            add_contact
        elif choice==2:
            view_contact
        elif choice==3:
            Search_name
        elif choice==4:
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Try again.")
         