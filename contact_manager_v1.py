import json
data = {
    "Name":[],
    "Contact":[]
}
def saver():
    with open("data.txt","w") as file:
        json.dump(data,file)

def read_contact():
    try:
        with open("data.txt","r") as file:
            read = json.load(file)
            for key,value in read.items():
                print(f"{key}: {value}")
        print("\n")
    except FileNotFoundError:
        print("[]")
    
def add_contact():
    name = input("Enter name: ")
    contact = input("Enter contact: ")
    data["Name"].append(name)
    data["Contact"].append(contact)
    saver()
    print("\n")

def update_contact():
    update_choice = input("What would you like to change -- name(1) or contact(2) or both(3): ")    

    match update_choice:
        case "1":
            old_name = input("Enter name you want to change: ")
            new_name = input("Enter new name: ")
            try:
                index_name = data["Name"].index(old_name)
                data["Name"].pop(index_name)
                data["Name"].append(new_name)
                saver()
            except ValueError:
                print("Invalid name!!")
            print("\n")    
        
        case "2":
            old_contact = input("Enter old contact number: ")                
            new_contact = input("Enter new contact: ")
            try:
                index_contact = data["Contact"].index(old_contact)
                data["Contact"].pop(index_contact)
                data["Contact"].append(new_contact)
                saver()
            except ValueError:
                print("Invalid number!!")          
            print("\n")
        
        case "3":
            old_name = input("Enter name you want to change: ")
            new_name = input("Enter new name: ")
            old_contact = input("Enter old contact number: ")                
            new_contact = input("Enter new contact: ")
            try:
                index_name = data["Name"].index(old_name)
                data["Name"].pop(index_name)
                data["Name"].append(new_name)
                        
                index_contact = data["Contact"].index(old_contact)
                data["Contact"].pop(index_contact)
                data["Contact"].append(new_contact)
                saver()
            except ValueError:
                print("Invalid name or number!!")
            print("\n")

        case _:
            print("Invalid choice!!")
            print("\n")

def delete_contact():
    delete_name = input("Enter name: ")
    delete_contact = input("Enter contact: ")
    try:
        index_delete_name = data["Name"].index()
        data["Name"].pop(index_delete_name)

        index_delete_contact = data["Contact"].index()
        data["Contact"].pop(index_delete_contact)
        saver()
    except ValueError:
        print("Invalid name or number!!")
    print("\n")

def main():
    print("\n")
    while True:
        print("Welcome to our app! | choose an option")
        print("1.Add")
        print("2.Read")    
        print("3.Update")    
        print("4.Delete")    
        print("5.Exit")
        choice = input("Enter your choice: ")
        
        match choice:
            case '1':
                add_contact()
            case '2':
                read_contact()
            case '3':
                update_contact()
            case '4':
                delete_contact()
            case '5':
                print("Thank you!!")
                break
            case _:
                print("Invalid choice!!")

if __name__ == "__main__":
    main()