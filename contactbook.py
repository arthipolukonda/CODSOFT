import tkinter as tk
from tkinter import messagebox, simpledialog

class ContactManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")
        self.root.geometry("600x500")
        
        self.contacts = []

        
        self.title_label = tk.Label(root, text="Contact Manager", font=("Arial", 24))
        self.title_label.pack(pady=10)

        
        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        
        self.listbox = tk.Listbox(self.frame, width=50, height=15, font=("Arial", 12), bd=0, selectbackground="#a6a6a6")
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        
        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

        
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=20)

        
        self.add_contact_button = tk.Button(self.button_frame, text="Add Contact", font=("Arial", 12), command=self.add_contact)
        self.add_contact_button.pack(side=tk.LEFT, padx=10)

        
        self.view_contacts_button = tk.Button(self.button_frame, text="View Contacts", font=("Arial", 12), command=self.view_contacts)
        self.view_contacts_button.pack(side=tk.LEFT, padx=10)

        
        self.search_contact_button = tk.Button(self.button_frame, text="Search Contact", font=("Arial", 12), command=self.search_contact)
        self.search_contact_button.pack(side=tk.LEFT, padx=10)

        
        self.update_contact_button = tk.Button(self.button_frame, text="Update Contact", font=("Arial", 12), command=self.update_contact)
        self.update_contact_button.pack(side=tk.LEFT, padx=10)

        
        self.delete_contact_button = tk.Button(self.button_frame, text="Delete Contact", font=("Arial", 12), command=self.delete_contact)
        self.delete_contact_button.pack(side=tk.LEFT, padx=10)

    def add_contact(self):
        name = simpledialog.askstring("Input", "Enter Name:")
        phone = simpledialog.askstring("Input", "Enter Phone Number:")
        email = simpledialog.askstring("Input", "Enter Email:")
        address = simpledialog.askstring("Input", "Enter Address:")
        
        if name and phone and email and address:
            self.contacts.append({"name": name, "phone": phone, "email": email, "address": address})
            messagebox.showinfo("Success", "Contact added successfully!")
        else:
            messagebox.showwarning("Warning", "All fields must be filled out!")

    def view_contacts(self):
        self.listbox.delete(0, tk.END)
        for contact in self.contacts:
            display_text = f"{contact['name']} - {contact['phone']}"
            self.listbox.insert(tk.END, display_text)

    def search_contact(self):
        query = simpledialog.askstring("Search", "Enter Name or Phone Number:")
        if query:
            results = [contact for contact in self.contacts if query.lower() in contact["name"].lower() or query in contact["phone"]]
            self.listbox.delete(0, tk.END)
            for contact in results:
                display_text = f"{contact['name']} - {contact['phone']}"
                self.listbox.insert(tk.END, display_text)
            if not results:
                messagebox.showinfo("Result", "No contacts found.")
        else:
            messagebox.showwarning("Warning", "Search query cannot be empty!")

    def update_contact(self):
        try:
            selected_index = self.listbox.curselection()[0]
            selected_contact = self.contacts[selected_index]

            name = simpledialog.askstring("Input", "Enter Name:", initialvalue=selected_contact["name"])
            phone = simpledialog.askstring("Input", "Enter Phone Number:", initialvalue=selected_contact["phone"])
            email = simpledialog.askstring("Input", "Enter Email:", initialvalue=selected_contact["email"])
            address = simpledialog.askstring("Input", "Enter Address:", initialvalue=selected_contact["address"])
            
            if name and phone and email and address:
                self.contacts[selected_index] = {"name": name, "phone": phone, "email": email, "address": address}
                messagebox.showinfo("Success", "Contact updated successfully!")
                self.view_contacts()
            else:
                messagebox.showwarning("Warning", "All fields must be filled out!")
        except IndexError:
            messagebox.showwarning("Warning", "You must select a contact to update!")

    def delete_contact(self):
        try:
            selected_index = self.listbox.curselection()[0]
            del self.contacts[selected_index]
            messagebox.showinfo("Success", "Contact deleted successfully!")
            self.view_contacts()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a contact to delete!")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManagerApp(root)
    root.mainloop()
