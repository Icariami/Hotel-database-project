import tkinter as tk
from tkinter import messagebox, ttk
from DB_connect import connect
import psycopg2
from PIL import Image, ImageTk

class RaportsForm:
    '''
    The form containing buttons to open reports based on views created on various elements in the database
    '''
    def __init__(self, master):
        self.master = master
        self.top = tk.Toplevel(master)
        self.top.title("Reports")

        background_image = Image.open("images/snowysky.jpg!d") 
        background_photo = ImageTk.PhotoImage(background_image)

        background_label = tk.Label(self.top, image=background_photo)
        background_label.image = background_photo
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.label_first_report = tk.Label(self.top, text="Report 1 - Summary of revenues for Chata Hotel in 2023:")
        self.button_first_report = tk.Button(self.top, text="View Report 1", command=self.first_report)

        self.label_second_report = tk.Label(self.top, text="Report 2 - Summary of guests who used any of the hotel's services \nand provided a review:")
        self.button_second_report = tk.Button(self.top, text="View Report 2", command=self.second_report)

        self.label_third_report = tk.Label(self.top, text="Report 3 - Summary of guests who revisited the hotel, \nalong with the average length of their visits:")
        self.button_third_report = tk.Button(self.top, text="View Report 3", command=self.third_report)

        self.label_first_report.grid(row=1, column=0, padx=10, pady=10)
        self.button_first_report.grid(row=1, column=1, padx=10, pady=10)

        self.label_second_report.grid(row=2, column=0, padx=10, pady=10)
        self.button_second_report.grid(row=2, column=1, padx=10, pady=10)

        self.label_third_report.grid(row=3, column=0, padx=10, pady=10)
        self.button_third_report.grid(row=3, column=1, padx=10, pady=10)

    def first_raport(self):
        result, column_names = self.execute_sql_query('''SELECT * FROM Monthly_revenue''')
        self.show_first_raport(result, column_names)

    def second_raport(self):
        result, column_names = self.execute_sql_query('''SELECT * FROM Guest_Service_Reservations_With_Reviews''')
        self.show_second_raport(result, column_names)

    def third_raport(self):
        result, column_names = self.execute_sql_query('''SELECT * FROM Average_duration_of_stay''')
        self.show_third_raport(result, column_names)

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
        
    def show_second_raport(self, result, column_names):
        result_window = tk.Toplevel(self.master)
        result_window.title("Report 2 - Summary of guests who used any of the hotel's services and provided a review")
        result_treeview = ttk.Treeview(result_window)
        result_treeview["columns"] = column_names
        for col in column_names:
            result_treeview.column(col, anchor=tk.CENTER, width=200)
            result_treeview.heading(col, text=col, anchor=tk.CENTER)
        for row in result:
            result_treeview.insert("", tk.END, values=row)
        result_treeview.column("#0", width=0)
        result_treeview.column("#1", width=100)
        result_treeview.column("#2", width=100)
        result_treeview.column("opinion", width=500)
        result_treeview.column("rating", width=50)
        result_window.geometry("1150x500")  
        result_treeview.pack(expand=True, fill="both")

    def show_first_raport(self, result, column_names):
        result_window = tk.Toplevel(self.master)
        result_window.title("Report 1 - Summary of revenues for Chata Hotel in 2023")
        result_treeview = ttk.Treeview(result_window)
        result_treeview["columns"] = column_names
        for col in column_names:
            result_treeview.column(col, anchor=tk.CENTER, width=200)
            result_treeview.heading(col, text=col, anchor=tk.CENTER)
        for row in result:
            result_treeview.insert("", tk.END, values=row)
        result_treeview.column("#0", width=0)
        result_treeview.column("#1", width=60)
        result_window.geometry("700x400") 
        result_treeview.pack(expand=True, fill="both")

    def show_third_raport(self, result, column_names):
        result_window = tk.Toplevel(self.master)
        result_window.title("Report 3 - Summary of guests who revisited the hotel, along with the average length of their visits")
        result_treeview = ttk.Treeview(result_window)
        result_treeview["columns"] = column_names
        for col in column_names:
            result_treeview.column(col, anchor=tk.CENTER, width=200)
            result_treeview.heading(col, text=col, anchor=tk.CENTER)
        for row in result:
            result_treeview.insert("", tk.END, values=row)
        result_treeview.column("#0", width=0)
        result_treeview.column("#1", width=100)
        result_treeview.column("#2", width=100)
        result_treeview.column("#3", width=150)
        result_window.geometry("700x400") 
        result_treeview.pack(expand=True, fill="both")


if __name__ == "__main__":
    root = tk.Tk()
    reports_gui = RaportsForm(root)
    root.mainloop()
