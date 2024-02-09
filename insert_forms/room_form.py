import tkinter as tk
from tkinter import messagebox
from DB_connect import connect
import psycopg2

class RoomForm:
    '''
    Form for adding data to the Room table
    '''
    def __init__(self, master):
        self.master = master
        self.top = tk.Toplevel(master)
        self.top.title("Add a new room")

        self.label_room_type = tk.Label(self.top, text="Room type: (required)")
        self.entry_room_type = tk.Entry(self.top)

        self.label_door_number = tk.Label(self.top, text="Door number: (required)")
        self.entry_door_number = tk.Entry(self.top)

        self.label_hotel_id = tk.Label(self.top, text="Hotel ID: (required)")
        self.entry_hotel_id = tk.Entry(self.top)

        self.submit_button = tk.Button(self.top, text="Add room", command=self.on_submit)

        self.label_room_type.grid(row=1, column=0, padx=20, pady=10)
        self.entry_room_type.grid(row=1, column=1, padx=20, pady=10)

        self.label_door_number.grid(row=2, column=0, padx=20, pady=10)
        self.entry_door_number.grid(row=2, column=1, padx=20, pady=10)

        self.label_hotel_id.grid(row=3, column=0, padx=20, pady=10)
        self.entry_hotel_id.grid(row=3, column=1, padx=20, pady=10)

        self.submit_button.grid(row=4, column=0, columnspan=2, pady=20)

    def on_submit(self):
        room_type = self.entry_room_type.get()
        door_number = self.entry_door_number.get()
        hotel_id = self.entry_hotel_id.get()

        if not room_type or not door_number or not hotel_id:
            messagebox.showerror("Error", "All required fields must be filled.\nPlease fill in the missing information.")
            return

        if not record_exists("Hotel.Room_type", "room_type_ID", room_type):
            messagebox.showerror("Error", f"No record in the Room_type table with room_type_ID equal to {room_type}.")
            return

        if not record_exists("Hotel.Hotel", "hotel_ID", hotel_id):
            messagebox.showerror("Error", f"No record in the Hotel table with hotel_ID equal to {hotel_id}.")
            return

        if not door_number.isdigit():
            messagebox.showerror("Error", "Invalid room door number.")
            return

        insert_room(room_type, door_number, hotel_id)
        messagebox.showinfo("Confirmation", "New room added!")
        print_room()
        self.top.destroy()


def record_exists(table, column, value):
    try:
        conn = connect()
        cur = conn.cursor()

        query = f"SELECT 1 FROM {table} WHERE {column} = %s"
        cur.execute(query, (value,))

        result = cur.fetchone()

        cur.close()
        conn.close()

        return result is not None

    except (psycopg2.Error, Exception) as error:
        print(f"Error checking record existence: {error}")
        return False

def print_room():
    try:
        conn = connect()
        cur = conn.cursor()

        query = '''SELECT * FROM Hotel.Room'''
        cur.execute(query)

        results = cur.fetchall()

        for row in results:
            print(row)
        cur.close()
        conn.close()
    except (psycopg2.Error, Exception) as error:
        print(f"Error retrieving guest data: {error}")

def insert_room(room_type, door_number, hotel_id):
    try:
        conn = connect()
        c = conn.cursor()

        sql = '''INSERT INTO Hotel.Room (room_type, door_number, hotel_id) VALUES (%s, %s, %s)'''

        c.execute(sql, (room_type, door_number, hotel_id))
        conn.commit()
        c.close()
        conn.close()
        
    except (psycopg2.Error, Exception) as error:
        print(f"Error inserting guest: {error}")



if __name__ == "__main__":
    root = tk.Tk()
    room_form = RoomForm(root)
    root.mainloop()
