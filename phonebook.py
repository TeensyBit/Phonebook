import sqlite3

def create_database():
    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS contacts
                      (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                      Name TEXT NOT NULL,
                      Cell TEXT NOT NULL,
                      Email TEXT)''')
    conn.close()

def add_contact(name, cell, email):
    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO contacts (Name, Cell, Email) VALUES (?, ?, ?)', (name, cell, email))
    conn.commit()
    conn.close()

def fetch_contacts():
    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM contacts')
    all_contacts = cursor.fetchall()
    conn.close()
    return all_contacts

def main():
    create_database()
    contacts_data = [
        ("Snehal", "1234567890", "snehal@gmail.com"),
        ("Hemal", "9876543210", "hemal@gmail.com"),
        ("Neymar", "5551234567", "neymar@gmail.com"),
        ("Messi", "9871234560", "messi@gmail.com"),
        ("Ronaldo", "4567890123", "ronnie@gmail.com")
    ]
    for contact in contacts_data:
        add_contact(*contact)
    all_contacts = fetch_contacts()
    print("All Contacts:")
    for contact in all_contacts:
        print(contact)

if __name__ == "__main__":
    main()
