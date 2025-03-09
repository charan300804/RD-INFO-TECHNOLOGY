import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

class ContactApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Contact Book")
        self.window.geometry("700x500")
        self.window.configure(bg="#f0f0f0")  # Light gray background

        # Apply a modern theme
        self.style = ttk.Style()
        self.style.configure("TButton", font=("Arial", 12), padding=5)
        self.style.configure("TLabel", font=("Arial", 12), background="#f0f0f0")
        self.style.configure("TEntry", font=("Arial", 12))

        # Database Connection
        self.con = sqlite3.connect("contact_book.db")
        self.cursor = self.con.cursor()
        self.create_table()

        self.create_widgets()
        self.window.mainloop()

    def create_table(self):
        """Create the CONTACTS_TABLE if it does not exist."""
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS CONTACTS_TABLE (
            Name TEXT NOT NULL, 
            Mobile_Number TEXT PRIMARY KEY, 
            Phone1 TEXT, 
            Phone2 TEXT, 
            Email TEXT, 
            Notes TEXT
        )
        """)
        self.con.commit()

    def create_widgets(self):
        """Main UI Components"""
        self.clear()

        # Header
        tk.Label(self.window, text="📖 Contact Book", font=("Arial", 18, "bold"), bg="#f0f0f0").pack(pady=10)

        # Search Bar
        search_frame = tk.Frame(self.window, bg="#f0f0f0")
        search_frame.pack(pady=10)

        self.search_entry = ttk.Entry(search_frame, width=40)
        self.search_entry.pack(side=tk.LEFT, padx=5)
        self.search_entry.bind("<KeyRelease>", lambda event: self.show_contacts())

        search_button = ttk.Button(search_frame, text="🔍 Search", command=self.show_contacts)
        search_button.pack(side=tk.LEFT, padx=5)

        # Contact List
        self.contact_list = ttk.Treeview(self.window, columns=("Name", "Mobile"), show="headings")
        self.contact_list.heading("Name", text="Name")
        self.contact_list.heading("Mobile", text="Mobile Number")
        self.contact_list.column("Name", width=250)
        self.contact_list.column("Mobile", width=150)
        self.contact_list.pack(pady=10)

        # Buttons
        btn_frame = tk.Frame(self.window, bg="#f0f0f0")
        btn_frame.pack(pady=10)

        ttk.Button(btn_frame, text="➕ Add Contact", command=self.add_contact_ui).pack(side=tk.LEFT, padx=10)
        ttk.Button(btn_frame, text="✏️ Edit Contact", command=self.edit_contact_ui).pack(side=tk.LEFT, padx=10)
        ttk.Button(btn_frame, text="🗑️ Delete Contact", command=self.delete_contact).pack(side=tk.LEFT, padx=10)

        self.show_contacts()

    def clear(self):
        """Clear all widgets from the window."""
        for widget in self.window.winfo_children():
            widget.destroy()

    def add_contact_ui(self):
        """UI for adding a contact."""
        self.contact_form("Add Contact", self.save_contact_to_db)

    def edit_contact_ui(self):
        """UI for editing a selected contact."""
        selected = self.contact_list.selection()
        if not selected:
            messagebox.showerror("Error", "Please select a contact to edit.")
            return

        name, mobile = self.contact_list.item(selected, "values")
        self.contact_form("Edit Contact", self.update_contact_to_db, name, mobile)

    def contact_form(self, title, save_command, name="", mobile=""):
        """Reusable Contact Form"""
        self.clear()
        tk.Label(self.window, text=title, font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=10)

        form_frame = tk.Frame(self.window, bg="#f0f0f0")
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Name:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.name_entry = ttk.Entry(form_frame, width=30)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)
        self.name_entry.insert(0, name)

        tk.Label(form_frame, text="Mobile Number:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.mobile_entry = ttk.Entry(form_frame, width=30)
        self.mobile_entry.grid(row=1, column=1, padx=5, pady=5)
        self.mobile_entry.insert(0, mobile)

        tk.Label(form_frame, text="Phone 1:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.phone1_entry = ttk.Entry(form_frame, width=30)
        self.phone1_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Phone 2:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.phone2_entry = ttk.Entry(form_frame, width=30)
        self.phone2_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Email:").grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.email_entry = ttk.Entry(form_frame, width=30)
        self.email_entry.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Notes:").grid(row=5, column=0, padx=5, pady=5, sticky="e")
        self.notes_entry = ttk.Entry(form_frame, width=30)
        self.notes_entry.grid(row=5, column=1, padx=5, pady=5)

        ttk.Button(self.window, text="💾 Save", command=save_command).pack(pady=10)
        ttk.Button(self.window, text="⬅️ Back", command=self.create_widgets).pack(pady=5)

    def save_contact_to_db(self):
        """Save a new contact."""
        name = self.name_entry.get().strip()
        mobile = self.mobile_entry.get().strip()
        if not name or not mobile:
            messagebox.showerror("Error", "Name and Mobile Number are required!")
            return

        self.cursor.execute("INSERT INTO CONTACTS_TABLE (Name, Mobile_Number) VALUES (?, ?)", (name, mobile))
        self.con.commit()
        messagebox.showinfo("Success", "Contact added successfully!")
        self.create_widgets()

    def update_contact_to_db(self):
        """Update an existing contact."""
        name = self.name_entry.get().strip()
        mobile = self.mobile_entry.get().strip()
        self.cursor.execute("UPDATE CONTACTS_TABLE SET Name = ? WHERE Mobile_Number = ?", (name, mobile))
        self.con.commit()
        messagebox.showinfo("Success", "Contact updated successfully!")
        self.create_widgets()

    def show_contacts(self):
        """Display all contacts."""
        search = self.search_entry.get().strip()
        self.contact_list.delete(*self.contact_list.get_children())

        query = "SELECT Name, Mobile_Number FROM CONTACTS_TABLE WHERE Name LIKE ? ORDER BY Name ASC"
        for row in self.cursor.execute(query, ('%' + search + '%',)):
            self.contact_list.insert("", "end", values=row)

    def delete_contact(self):
        """Delete a selected contact."""
        selected = self.contact_list.selection()
        if not selected:
            messagebox.showerror("Error", "Please select a contact to delete.")
            return

        name, mobile = self.contact_list.item(selected, "values")
        self.cursor.execute("DELETE FROM CONTACTS_TABLE WHERE Mobile_Number = ?", (mobile,))
        self.con.commit()
        messagebox.showinfo("Success", f"{name} deleted!")
        self.show_contacts()

if __name__ == "__main__":
    ContactApp()
