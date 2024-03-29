import tkinter as tk
from tkinter import messagebox
from DB_connect import connect
import psycopg2

class ReviewForm:
    '''
    Form for adding data to the Review table
    '''
    def __init__(self, master):
        self.master = master
        self.top = tk.Toplevel(master)
        self.top.title("Add a new review")

        self.label_booking_id = tk.Label(self.top, text="Reservation ID (required):")
        self.entry_booking_id = tk.Entry(self.top)

        self.label_booked_service_id = tk.Label(self.top, text="Booked service ID (required):")
        self.entry_booked_service_id = tk.Entry(self.top)

        self.label_rating = tk.Label(self.top, text="Rating (required):")
        self.entry_rating = tk.Entry(self.top)

        self.label_review_text = tk.Label(self.top, text="Review text:")
        self.entry_review_text = tk.Entry(self.top)

        self.submit_button = tk.Button(self.top, text="Add review", command=self.on_submit)


        self.label_booking_id.grid(row=1, column=0, padx=20, pady=10)
        self.entry_booking_id.grid(row=1, column=1, padx=20, pady=10)

        self.label_booked_service_id.grid(row=2, column=0, padx=20, pady=10)
        self.entry_booked_service_id.grid(row=2, column=1, padx=20, pady=10)

        self.label_rating.grid(row=3, column=0, padx=20, pady=10)
        self.entry_rating.grid(row=3, column=1, padx=20, pady=10)

        self.label_review_text.grid(row=4, column=0, padx=20, pady=10)
        self.entry_review_text.grid(row=4, column=1, padx=20, pady=10)

        self.submit_button.grid(row=5, column=0, columnspan=2, pady=20)


    def on_submit(self):
        booking_id = self.entry_booking_id.get()
        booked_service_id = self.entry_booked_service_id.get()
        rating = self.entry_rating.get()
        review_text = self.entry_review_text.get()

        if not booking_id or not rating or not booked_service_id:
            messagebox.showerror("Error", "All required fields must be filled.\nPlease fill in the missing information.")
            return

        if not record_exists("Hotel.Booking", "booking_ID", booking_id):
            messagebox.showerror("Error", f"No record in the Booking table with booking_ID equal to {booking_id}.")
            return

        if not record_exists("Hotel.Booked_service", "booked_service_ID", booked_service_id):
            messagebox.showerror("Error", f"No record in the Booked_service table with booked_service_ID equal to {booked_service_id}.")
            return

        try:
            insert_review(booking_id, booked_service_id, rating, review_text)
            messagebox.showinfo("Confirmation", "New review added!")
            print_review()
            self.top.destroy()
        except Exception as e:
            messagebox.showerror("Error", "The rating should be in the range of 1-10. Please correct the entered data.")


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

def print_review():
    try:
        conn = connect()
        cur = conn.cursor()

        query = '''SELECT * FROM Hotel.Review'''
        cur.execute(query)

        results = cur.fetchall()

        for row in results:
            print(row)
        cur.close()
        conn.close()
    except (psycopg2.Error, Exception) as error:
        print(f"Error retrieving review data: {error}")

def insert_review(booking_id, booked_service_id, rating, review_text):
    try:
        conn = connect()
        c = conn.cursor()

        sql = '''INSERT INTO Hotel.Review (booking_id, booked_service_id, rating, review_text) VALUES (%s, %s, %s, %s)'''

        c.execute(sql, (booking_id, booked_service_id, rating, review_text))
        conn.commit()
        c.close()
        conn.close()
        
    except (psycopg2.Error, Exception) as error:
        raise Exception(f"Error inserting review: {error}")

if __name__ == "__main__":
    root = tk.Tk()
    review_form = ReviewForm(root)
    root.mainloop()
