book_file = "books.txt"
member_file = "members.txt"
book = {}
member = {}

def save_data():
    try:
        with open(book_file, "a") as f:
            for title, info in book.items():
                f.write(f"{title},{info['nevisande']},{info['vaziat']},{info['borrowed by']}\n")
    except FileNotFoundError:
        pass

    try:
        with open(member_file, "a") as f:
            for member_id, info in member.items():
                f.write(f"{info['name']},{member_id}\n")
    except FileNotFoundError:
        pass

def load_data():
    try:
        with open(book_file, "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 4:
                    title, nevisande, vaziat, borrowed_by = parts
                    book[title] = {'nevisande': nevisande, 'vaziat': vaziat, 'borrowed by': borrowed_by}
                else:
                    print(f"{line.strip()}")
    except FileNotFoundError:
        pass

    try:
        with open(member_file, "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 2:
                    name, member_id = parts
                    member[member_id] = {'name': name}
                else:
                    print(f"{line.strip()}")
    except FileNotFoundError:
        pass

def add_book(title, nevisande):
    if title in book:
        print(f"ketab {title} az ghabl vojood darad")
    else:
        book[title] = {'nevisande': nevisande, 'vaziat': "mojood", "borrowed by": 'none'}
        print(f"ketab {title} ba movafaghiat ezafe shod")

def remove_book(title):
    if title in book:
        del book[title]
        print(f"ketab {title} ba movafaghiat hazf shod")
    else:
        print(f"ketab {title} vojood nadarad")

def register_member(name, member_id):
    if member_id in member:
        print(f"fardy ba {member_id} vojood darad")
    else:
        member[member_id] = {'name': name}
        print(f"membery ba {name} va {member_id} ozv member ha shod ")

def remove_member(member_id):
    if member_id in member:
        for title, info in book.items():
            if info["borrowed by"] == member_id:
                info["vaziat"] = 'mojood'
                info["borrowed by"] = 'None'
        del member[member_id]
        print(f"karbar ba {member_id} ba movafaghiat hazf shod")
    else:
        print(f"karbary ba {member_id} vojood nadarad")

def borrow_book(title, member_id):
    member_id = member_id.strip()
    if title in book:
        if book[title]['vaziat'] == 'mojood':
            if member_id in member:
                book[title]['vaziat'] = 'gharz gerefte shode'
                book[title]['borrowed by'] = member_id
                print(f"ketab {title} ba movafaghiat tavasot {member_id} gharz gerefte shod")
            else:
                print(f"fardy ba {member_id} ozv ketabkhane nist.")
        else:
            print(f"ketab {title} mojood nist.")
    else:
        print(f"ketab {title} vojood nadarad.")

def return_book(title):
    if title in book:
        if book[title]['vaziat'] == 'gharz gerefte shode':
            book[title]["vaziat"] = 'mojood'
            book[title]["borrowed by"] = 'None'
            print(f"ketab {title} ba movafaghiat bargardande shod")
        else:
            print(f"ketab {title} tavasot kasi gharz gerefte nashode ast")
    else:
        print(f"ketab {title} vojood nadard")

def menu():
    while True:
        print("\nMenu:")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Register Member")
        print("4. Remove Member")
        print("5. Borrow Book")
        print("6. Return Book")
        print("7. Exit")
        entekhab = input("lotfan yek gozine ra entekhab konid: ")
        if entekhab == '1':
            title = input("lotfan esm ketab khod ra vared konid:")
            nevisande = input("lotfan esm nevisande ketab ra vvared konid: ")
            add_book(title, nevisande)
        if entekhab == '2':
            title = input("lotfan esm ketab ra vard konid: ")
            remove_book(title)
        if entekhab == '3':
            name = input("lotfan esm khod ra vared konid: ")
            member_id = input("lotfan ye member id vared konid: ")
            register_member(name, member_id)
        if entekhab == '4':
            member_id = input("lotfan member id khod ra vared konid")
            remove_member(member_id)
        if entekhab == '5':
            title = input("lotfant esm ketab ra vared konid: ")
            member_id = input("lotfan member id khod ra vared konid: ")
            borrow_book(title, member_id)
        if entekhab == '6':
            title = input("lotfant esm ketab ra vared konid: ")
            return_book(title)
        if entekhab == '7':
            save_data()
            print("dar hal kharej shodan")
            break
load_data()
menu()
