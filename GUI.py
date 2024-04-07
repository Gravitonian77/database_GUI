import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter.ttk import Treeview
import pymysql

def execute_query():
    query = simpledialog.askstring("Input", "Enter your SQL query:")
    if query:
        try:
            connection = pymysql.connect(host='xjc353.encs.concordia.ca', user='xjc353_4', password='hBZ26yuO', database='xjc353_4')
            with connection.cursor() as cursor:
                    cursor.execute(query)
                    if query.lower().startswith("select"):
                    # This is a SELECT query
                        results = cursor.fetchall()
                    # Clear previous data
                        for i in tree.get_children():
                            tree.delete(i)
                    # Inserting new data
                        for row in results:
                            tree.insert('', 'end', values=row)
                    else:
                    
                        connection.commit()  # Commit changes to the database
                        messagebox.showinfo("Success", "The query was executed successfully.")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            if connection:
                connection.close()

root = tk.Tk()
root.title("Database GUI")
root.geometry("600x400")

tree = Treeview(root, columns=('Result'), show='headings')
tree.heading('Result', text='Query Result')
tree.pack(side=tk.TOP, fill=tk.X)


query_button = tk.Button(root, text="Execute Query", command=execute_query)
query_button.pack(side=tk.BOTTOM)

root.mainloop()
