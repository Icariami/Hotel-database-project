import tkinter as tk
from tkinter import messagebox
from DB_connect import connect
import psycopg2

class RoomTypeForm:
    '''
    Form for adding data to the Room_type table
    '''
    def __init__(self, master) -> None:
        self.master = master
        self.top = tk.Toplevel(master)
        self.top.title("Add a new room type")

        self.label_name = tk.Label(self.top, text="Name: (required)")
        self.entry_name = tk.Entry(self.top)

        self.label_description = tk.Label(self.top, text="Description:")
        self.entry_description = tk.Entry(self.top)

        self.label_price_per_night = tk.Label(self.top, text="Price per night: (required)")
        self.entry_price_per_night = tk.Entry(self.top)

        self.label_pet_friendly = tk.Label(self.top, text="Pet-friendly (yes/no): (required)")
        self.entry_pet_friendly = tk.Entry(self.top)

        self.label_capacity = tk.Label(self.top, text="Capacity: (required)")
        self.entry_capacity = tk.Entry(self.top)

        self.submit_button = tk.Button(self.top, text="Add room type", command=self.on_submit)

        self.label_name.grid(row=1, column=0, padx=20, pady=10)
        self.entry_name.grid(row=1, column=1, padx=20, pady=10)

        self.label_description.grid(row=2, column=0, padx=20, pady=10)
        self.entry_description.grid(row=2, column=1, padx=20, pady=10)

        self.label_price_per_night.grid(row=3, column=0, padx=20, pady=10)
        self.entry_price_per_night.grid(row=3, column=1, padx=20, pady=10)

        self.label_pet_friendly.grid(row=4, column=0, padx=20, pady=10)
        self.entry_pet_friendly.grid(row=4, column=1, padx=20, pady=10)

        self.label_capacity.grid(row=5, column=0, padx=20, pady=10)
        self.entry_capacity.grid(row=5, column=1, padx=20, pady=10)

        self.submit_button.grid(row=6, column=0, columnspan=2, pady=20)

    def on_submit(self):
        name = self.entry_name.get()
        description = self.entry_description.get()
        price_per_night = self.entry_price_per_night.get()
        pet_friendly = self.entry_pet_friendly.get()
        if pet_friendly.lower() == "tak":
            pet_bool = True
        elif pet_friendly.lower() == "nie":
            pet_bool = False
        else:
            messagebox.showerror("Error", "Invalid entry. Allowed options: yes/no")
            return

        capacity = self.entry_capacity.get()

        if not name or not price_per_night or not pet_friendly or not capacity:
            messagebox.showerror("Error", "All required fields must be filled.\nPlease fill in the missing information.")
            return

        if not price_per_night.isdigit():
            messagebox.showerror("Error", "Invalid price.")
            return

        if not capacity.isdigit():
            messagebox.showerror("Error", "Invalid room capacity.")
            return

        insert_room_type(name, description, price_per_night, pet_bool, capacity)
        messagebox.showinfo("Confirmation", "New room type added!")
        print_room_type()
        self.top.destroy()



def insert_room_type(name, description, price_per_night, pet_friendly, capacity):
    try:
        conn = connect()
        c = conn.cursor()

        sql = '''INSERT INTO Hotel.Room_type (name, description, price_per_night, pet_friendly, capacity) VALUES (%s, %s, %s, %s, %s)'''

        c.execute(sql, (name, description, price_per_night, pet_friendly, capacity))
        conn.commit()
        c.close()
        conn.close()
    
    except (psycopg2.Error, Exception) as error:
        print(f"Error inserting data: {error}")


def print_room_type():
    try:
        conn = connect()
        cur = conn.cursor()

        query = '''SELECT * FROM Hotel.Room_type'''
        cur.execute(query)

        results = cur.fetchall()

        for row in results:
            print(row)
        cur.close()
        conn.close()
    except (psycopg2.Error, Exception) as error:
        print(f"Error inserting data: {error}")

if __name__ == "__main__":
    root = tk.Tk()
    hotel_form = RoomTypeForm(root)
    root.mainloop()