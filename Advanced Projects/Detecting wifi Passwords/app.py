import subprocess
import tkinter as tk
from tkinter import messagebox, scrolledtext


# Function to get Wi-Fi profiles and passwords
def get_wifi_passwords():
    try:
        # Retrieve the list of Wi-Fi profiles
        command = (
            subprocess.check_output(["netsh", "wlan", "show", "profiles"])
            .decode("utf-8")
            .split("\n")
        )

        profiles = [i.split(":")[1][1:-1] for i in command if "All User Profile" in i]
        results_text.delete("1.0", tk.END)  # Clear the text widget

        for i in profiles:
            results = (
                subprocess.check_output(
                    ["netsh", "wlan", "show", "profile", i, "key=clear"]
                )
                .decode("utf-8")
                .split("\n")
            )
            results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
            try:
                results_text.insert(tk.END, "{:<30}|  {:<}\n".format(i, results[0]))
            except IndexError:
                results_text.insert(tk.END, "{:<30}|  {:<}\n".format(i, ""))

        messagebox.showinfo(
            "Info",
            "Wi-Fi profiles and passwords retrieved successfully!",
            parent=root,
            icon="info",
        )
    except Exception as e:
        messagebox.showerror("Error", str(e), parent=root)


# Create the main window
root = tk.Tk()
root.title("Wi-Fi Password Viewer")
root.geometry("800x600")  # Expanded window size
root.configure(bg="#2c3e50")

# Create a title label
title_label = tk.Label(
    root,
    text="Wi-Fi Password Viewer",
    font=("Helvetica", 18, "bold"),
    bg="#2c3e50",
    fg="#ecf0f1",
)
title_label.pack(pady=20)

# Create a frame for the text widget and scrollbar
frame = tk.Frame(root, bg="#2c3e50")
frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Create a scrolled text widget
results_text = scrolledtext.ScrolledText(
    frame,
    wrap=tk.WORD,
    width=80,
    height=20,
    font=("Courier", 12),
    bg="#ecf0f1",
    fg="#2c3e50",
    padx=10,
    pady=10,
    borderwidth=5,
    relief="groove",
)
results_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Create a button to retrieve Wi-Fi passwords
get_passwords_button = tk.Button(
    root,
    text="Get Wi-Fi Passwords",
    command=get_wifi_passwords,
    font=("Helvetica", 14),
    bg="#3498db",
    fg="#ecf0f1",
    activebackground="#2980b9",
    activeforeground="#ecf0f1",
    padx=20,
    pady=10,
    borderwidth=3,
    relief="raised",
)
get_passwords_button.pack(pady=20)

# Start the GUI event loop
root.mainloop()
