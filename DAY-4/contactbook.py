contact = {}
def add_contact(name,number):
    contact[name] = number
    print("CONTACT SAVED")
add_contact("DHRUV",9259588471)
add_contact("pranav",893478724)
add_contact("papa",8800960960)

def view_contacts():
    for key,value in contact.items():
        print(f"{key}=={value}")

def search_contact(name):

    print(contact.get(name))

search_contact("DHRUV")

def menu():
    print("ENTER 1 FOR ADDING CONTACTS","\n","ENTER 2 FOR VIEW CONTACTS","\n","ENTER 3 FOR SEARCH CONTACTS")
    w =int(input("ENTER HERE"))
    if(w==1):
        add_contact(name,number)
    elif(w==2):
        view_contacts()
    elif(w==3):
        search_contact(name1)
    
menu()


