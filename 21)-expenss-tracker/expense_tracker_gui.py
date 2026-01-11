import tkinter as tk
from tkinter import messagebox

# LOGIC
store_Expenses = []

def add_expense_logic(name, amount, category):
    store_Expenses.append([name, amount, category])

def total_expense_logic():
    total = 0
    for exp in store_Expenses:
        total += exp[1]
    return total

# GUI PART 
def add_expense():
    name = name_entry.get()
    amount = amount_entry.get()
    category = category_entry.get()

    if name == "" or amount == "" or category == "":
        messagebox.showerror("Error", "All fields are required")
        return

    try:
        amount = int(amount)
    except:
        messagebox.showerror("Error", "Amount must be number")
        return

    add_expense_logic(name, amount, category)
    messagebox.showinfo("Success", "Expense Added Successfully")

    name_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)

def view_expenses():
    expense_text.delete("1.0", tk.END)
    if not store_Expenses:
        expense_text.insert(tk.END, "No expenses found\n")
        return

    for exp in store_Expenses:
        expense_text.insert(tk.END, f"Name: {exp[0]} | Amount: {exp[1]} | Category: {exp[2]}\n")

def view_total():
    total = total_expense_logic()
    messagebox.showinfo("Total Expense", f"Total Expense = ₹ {total}")

# WINDOW 
root = tk.Tk()
root.title("🛼 Expense Tracker 🛼")
root.geometry("500x450")

# LABELS & INPUT
tk.Label(root, text="Expense Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Amount").pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

tk.Label(root, text="Category").pack()
category_entry = tk.Entry(root)
category_entry.pack()

# BUTTONS 
tk.Button(root, text="Add Expense", command=add_expense, bg="green", fg="white").pack(pady=5)
tk.Button(root, text="View Expenses", command=view_expenses, bg="blue", fg="white").pack(pady=5)
tk.Button(root, text="View Total Expense", command=view_total, bg="orange").pack(pady=5)

# DISPLAY AREA
expense_text = tk.Text(root, height=10)
expense_text.pack()

root.mainloop()