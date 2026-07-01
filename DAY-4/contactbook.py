contact = {}
def add_contact():
    name = input("ENTER NAME")
    number = input("ENTER NUMBER1")
    contact[name] = number
    print("CONTACT SAVED")

def view_contacts():
    for key,value in contact.items():
        print(f"{key}=={value}")

def search_contact():
    name = input("ENTER NO TO SEARCH1")

    print(contact.get(name))



def menu():
    print("ENTER 1 FOR ADDING CONTACTS","\n","ENTER 2 FOR VIEW CONTACTS","\n","ENTER 3 FOR SEARCH CONTACTS","\n","5 FOR EXIT")
    w =int(input("ENTER HERE"))
    if(w==1):
        add_contact()
    elif(w==2):
        view_contacts()
    elif(w==3):
        search_contact()
    elif(w==5):
        print("EXUTED")
    
menu()


