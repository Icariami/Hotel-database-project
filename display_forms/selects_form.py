import tkinter as tk
from tkinter import messagebox
from tkinter import messagebox, ttk
from DB_connect import connect
import psycopg2
from PIL import Image, ImageTk

class SelectsForm:
    '''
    Form containing buttons redirecting to display existing tables in the database.
    '''
    def __init__(self, master):
        self.master = master
        self.top = tk.Toplevel(master)
        self.top.title("Displaying tables")

        background_image = Image.open("images/tree3.jpeg") 
        background_photo = ImageTk.PhotoImage(background_image)

        background_label = tk.Label(self.top, image=background_photo)
        background_label.image = background_photo
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.button_select_guest = tk.Button(self.top, text="Display Guests Table", command=self.open_guest_table)
        self.button_select_guest.pack(pady=10, padx=20)

        self.button_select_hotel = tk.Button(self.top, text="Display Hotels Table", command=self.open_hotel_table)
        self.button_select_hotel.pack(pady=10, padx=20)

        self.button_select_room_type = tk.Button(self.top, text="Display Room Types Table", command=self.open_room_type_table)
        self.button_select_room_type.pack(pady=10, padx=20)

        self.button_select_room = tk.Button(self.top, text="Display Rooms Table", command=self.open_room_table)
        self.button_select_room.pack(pady=10, padx=20)

        self.button_select_booking = tk.Button(self.top, text="Display Bookings Table", command=self.open_booking_table)
        self.button_select_booking.pack(pady=10, padx=20)

        self.button_select_service = tk.Button(self.top, text="Display Services Table", command=self.open_service_table)
        self.button_select_service.pack(pady=10, padx=20)

        self.button_select_booked_service = tk.Button(self.top, text="Display Booked Services Table", command=self.open_booked_service_table)
        self.button_select_booked_service.pack(pady=10, padx=20)

        self.button_select_review = tk.Button(self.top, text="Display Reviews Table", command=self.open_review_table)
        self.button_select_review.pack(pady=10, padx=20)


    def open_guest_table(self):
        result, column_names = self.execute_sql_query('''SELECT * FROM Hotel.Guest''')
        self.show_guest(result, column_names)

    def open_hotel_table(self):
        result, column_names = self.execute_sql_query('''SELECT * FROM Hotel.Hotel''')
        self.show_hotel(result, column_names)

    def open_room_type_table(self):
        result, column_names = self.execute_sql_query('''SELECT * FROM Hotel.Room_type''')
        self.show_room_type(result, column_names)

    def open_room_table(self):
        result, column_names = self.execute_sql_query('''SELECT * FROM Hotel.Room''')
        self.show_room(result, column_names)

    def open_booking_table(self):
        result, column_names = self.execute_sql_query('''SELECT * FROM Hotel.Booking''')
        self.show_booking(result, column_names)

    def open_service_table(self):
        result, column_names = self.execute_sql_query('''SELECT * FROM Hotel.Service''')
        self.show_service(result, column_names)

    def open_booked_service_table(self):
        result, column_names = self.execute_sql_query('''SELECT * FROM Hotel.Booked_Service''')
        self.show_booked_service(result, column_names)

    def open_review_table(self):
        result, column_names = self.execute_sql_query('''SELECT * FROM Hotel.Review''')
        self.show_review(result, column_names)

    def execute_sql_query(self, query):
        try:
            connection = connect()
            cursor = connection.cursor()
            cursor.execute(query)
            column_names = [desc[0] for desc in cursor.description]
            result = cursor.fetchall()
            connection.close()
            return result, column_names
        except psycopg2.Error as e:
            messagebox.showerror("Error", f"Error during SQL query execution: {str(e)}")

    def show_guest(self, result, column_names):
        result_window = tk.Toplevel(self.master)
        result_window.title("Guest table")
        result_treeview = ttk.Treeview(result_window)
        result_treeview["columns"] = column_names
        for col in column_names:
            result_treeview.column(col, anchor=tk.CENTER)
            result_treeview.heading(col, text=col, anchor=tk.CENTER)
        for row in result:
            result_treeview.insert("", tk.END, values=row)
        result_treeview.column("#0", width=0)
        result_treeview.column("#1", width=50)
        result_treeview.column("#2", width=120)
        result_treeview.column("#3", width=120)
        result_treeview.column("#4", width=100)
        result_treeview.column("#5", width=250)
        result_window.geometry("1000x500")  
        result_treeview.pack(expand=True, fill="both")

    def show_hotel(self, result, column_names):
        result_window = tk.Toplevel(self.master)
        result_window.title("Hotel table")
        result_treeview = ttk.Treeview(result_window)
        result_treeview["columns"] = column_names
        for col in column_names:
            result_treeview.column(col, anchor=tk.CENTER)
            result_treeview.heading(col, text=col, anchor=tk.CENTER)
        for row in result:
            result_treeview.insert("", tk.END, values=row)
        result_treeview.column("#0", width=0)
        result_treeview.column("#1", width=50)
        result_treeview.column("name", width=100)
        result_treeview.column("phone_number", width=90)
        result_treeview.column("star_rating", width=70)
        result_treeview.column("description", width=400)
        result_window.geometry("1600x700")  
        result_treeview.pack(expand=True, fill="both")

    def show_room_type(self, result, column_names):
        result_window = tk.Toplevel(self.master)
        result_window.title("Room_type table")
        result_treeview = ttk.Treeview(result_window)
        result_treeview["columns"] = column_names
        for col in column_names:
            result_treeview.column(col, anchor=tk.CENTER)
            result_treeview.heading(col, text=col, anchor=tk.CENTER)
        for row in result:
            result_treeview.insert("", tk.END, values=row)
        result_treeview.column("#0", width=0)
        result_treeview.column("#1", width=80)
        # result_treeview.column("#2", width=120)
        result_treeview.column("#4", width=100)
        result_treeview.column("#3", width=750)
        result_treeview.column("#5", width=100)
        result_treeview.column("#6", width=80)
        result_window.geometry("1500x300")  
        result_treeview.pack(expand=True, fill="both")

    def show_room(self, result, column_names):
        result_window = tk.Toplevel(self.master)
        result_window.title("Room table")
        result_treeview = ttk.Treeview(result_window)
        result_treeview["columns"] = column_names
        for col in column_names:
            result_treeview.column(col, anchor=tk.CENTER)
            result_treeview.heading(col, text=col, anchor=tk.CENTER)
        for row in result:
            result_treeview.insert("", tk.END, values=row)
        result_treeview.column("#0", width=0)
        result_treeview.column("#1", width=60)
        result_treeview.column("#2", width=60)
        result_treeview.column("#3", width=60)
        result_treeview.column("#4", width=60)
        result_window.geometry("500x450")  
        result_treeview.pack(expand=True, fill="both")

    def show_booking(self, result, column_names):
        result_window = tk.Toplevel(self.master)
        result_window.title("Booking table")
        result_treeview = ttk.Treeview(result_window)
        result_treeview["columns"] = column_names
        for col in column_names:
            result_treeview.column(col, anchor=tk.CENTER)
            result_treeview.heading(col, text=col, anchor=tk.CENTER)
        for row in result:
            result_treeview.insert("", tk.END, values=row)
        result_treeview.column("#0", width=0)
        result_treeview.column("#1", width=50)
        result_treeview.column("#2", width=100)
        result_treeview.column("#3", width=100)
        result_treeview.column("#4", width=130)
        result_treeview.column("#5", width=130)
        result_window.geometry("800x600")  
        result_treeview.pack(expand=True, fill="both")

    def show_service(self, result, column_names):
        result_window = tk.Toplevel(self.master)
        result_window.title("Service table")
        result_treeview = ttk.Treeview(result_window)
        result_treeview["columns"] = column_names
        for col in column_names:
            result_treeview.column(col, anchor=tk.CENTER)
            result_treeview.heading(col, text=col, anchor=tk.CENTER)
        for row in result:
            result_treeview.insert("", tk.END, values=row)
        result_treeview.column("#0", width=0)
        result_treeview.column("#1", width=50)
        result_treeview.column("#2", width=100)
        result_treeview.column("#3", width=500)
        result_treeview.column("#4", width=90)
        # result_treeview.column("#5", width=130)
        result_window.geometry("1000x300")  
        result_treeview.pack(expand=True, fill="both")

    def show_booked_service(self, result, column_names):
        result_window = tk.Toplevel(self.master)
        result_window.title("Booked_service table")
        result_treeview = ttk.Treeview(result_window)
        result_treeview["columns"] = column_names
        for col in column_names:
            result_treeview.column(col, anchor=tk.CENTER)
            result_treeview.heading(col, text=col, anchor=tk.CENTER)
        for row in result:
            result_treeview.insert("", tk.END, values=row)
        result_treeview.column("#0", width=0)
        result_treeview.column("#1", width=80)
        result_treeview.column("#2", width=60)
        result_treeview.column("#3", width=60)
        result_window.geometry("330x500")  
        result_treeview.pack(expand=True, fill="both")

    def show_review(self, result, column_names):
        result_window = tk.Toplevel(self.master)
        result_window.title("Review table")
        result_treeview = ttk.Treeview(result_window)
        result_treeview["columns"] = column_names
        for col in column_names:
            result_treeview.column(col, anchor=tk.CENTER)
            result_treeview.heading(col, text=col, anchor=tk.CENTER)
        for row in result:
            result_treeview.insert("", tk.END, values=row)
        result_treeview.column("#0", width=0)
        result_treeview.column("#1", width=80)
        result_treeview.column("#2", width=80)
        result_treeview.column("#3", width=80)
        result_treeview.column("#4", width=80)
        result_treeview.column("#5", width=500)
        result_window.geometry("1000x500")  
        result_treeview.pack(expand=True, fill="both")
    


if __name__ == "__main__":
    root = tk.Tk()
    main_gui = SelectsForm(root)
    root.mainloop()