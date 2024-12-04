import tkinter as tk
from tkinter.ttk import Combobox, Style
from tkinter import StringVar, IntVar, PhotoImage, Label, Entry, Button
import pandas as pd
import pathlib

# Create the main window
root = tk.Tk()
root.title("Data Entry Form")
root.geometry("700x500+300+200")
root.resizable(False, False)
root.configure(bg="#2C3E50")

# Define styles
style = Style()
style.configure('TButton', font=("Arial", 12), background="#E74C3C", foreground="white")
style.configure('TLabel', font=("Arial", 12, "bold"), background="#2C3E50", foreground="white")
style.configure('TEntry', font=("Arial", 12))
style.configure('TCombobox', font=("Arial", 12))

frame = tk.Frame(root, bg="#2C3E50")
frame.pack(padx=20, pady=20)

df = pd.DataFrame()

file = pathlib.Path("data.xlsx")
if not file.exists():
    df = pd.DataFrame(columns=["Name", "Email", "Contact", "Age", "Gender", "Address"])
    df.to_excel("data.xlsx", index=False)
else:
    # If the file exists, read it into df
    df = pd.read_excel("data.xlsx")

def clear():
    name_var.set("")
    email_var.set("")
    contact_var.set("")
    age_var.set("")
    gender_var.set("Male")
    address_var.set("")
    notification_label.config(text="")

def submit():
    try:
        new_data = pd.DataFrame({'Name': [name_var.get()],
                                 'Email': [email_var.get()],
                                 'Contact': [contact_var.get()],
                                 'Age': [age_var.get()],
                                 'Gender': [gender_var.get()],
                                 'Address': [address_var.get()]})
        global df
        df = pd.concat([df, new_data], ignore_index=True)
        df.to_excel("data.xlsx", index=False)
        clear()
        notification_label.config(text="Data entered successfully!", foreground="white")
    except Exception as e:
        notification_label.config(text=f"Error: {str(e)}", foreground="green")

# Icons
try:
    icon_image = PhotoImage(file="ameer-high-resolution-logo.png")
    root.iconphoto(False, icon_image)
except Exception as e:
    print(f"Icon image error: {str(e)}")

# Heading
heading_label = Label(frame, text="Please fill out this form", font=("Arial", 20, "bold"), background="#2C3E50", foreground="white")
heading_label.grid(row=0, column=0, columnspan=2, pady=10)

# Labels and Entry Fields
name_var = StringVar()
email_var = StringVar()
contact_var = StringVar()
age_var = IntVar()
gender_var = StringVar()
gender_var.set("Male")
address_var = StringVar()

labels = ["Name", "Email", "Contact Info", "Age", "Gender", "Address"]
variables = [name_var, email_var, contact_var, age_var, gender_var, address_var]
for i, (label, var) in enumerate(zip(labels, variables), start=1):
    label_widget = Label(frame, text=label, background="#2C3E50", foreground="white")
    label_widget.grid(row=i, column=0, sticky='e', padx=5, pady=5)
    if label == "Gender":
        combobox = Combobox(frame, textvariable=var, values=["Male", "Female"])
        combobox.grid(row=i, column=1, sticky='w', padx=5, pady=5)
    else:
        entry = Entry(frame, textvariable=var)
        entry.grid(row=i, column=1, sticky='w', padx=5, pady=5)

# Buttons
submit_button = Button(frame, text="Submit", command=submit, bg="green", fg="white", width=10, height=1, font=("Arial", 10))
submit_button.grid(row=7, column=0, padx=5, pady=20)
clear_button = Button(frame, text="Clear", command=clear, bg="#3498DB", fg="white", width=10, height=1, font=("Arial", 10))
clear_button.grid(row=7, column=1, padx=5, pady=20)
exit_button = Button(frame, text="Exit", command=root.destroy, bg="#E74C3C", fg="white", width=10, height=1, font=("Arial", 10))
exit_button.grid(row=7, column=2, padx=5, pady=20)

# Notification label
notification_label = Label(frame, text="", font=("Arial", 12), background="#2C3E50", foreground="white")
notification_label.grid(row=8, column=0, columnspan=3, pady=5)

root.mainloop()
