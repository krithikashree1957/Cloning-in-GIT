
contacts={}

def add_contact(name, phone):
    contacts[name]=phone
def search_contact(name):
    return contacts.get(name,"Not found")

if __name__=="__main__":
    add_contact("Lala","986544987")
    add_contact("Kiki","125384677")
    print("Arun's number: ",search_contact("Arun"))
    print("Search Kabir:", search_contact("Kabir"))
    print("Search Kiki", search_contact("Kiki"))
    
