import os
import shutil
import tkinter as tk
from tkinter import filedialog, ttk


class FileSorterApp:
    def __init__(self, master):
        self.master = master
        master.title("File Sorter")

        self.style = ttk.Style()
        self.style.configure(
            "TButton",
            padding=6,
            relief="flat",
            background="#4285F4",  # Google Blue
            foreground="black",
        )
        self.style.map("TButton", background=[("active", "#1A73E8")])

        self.label = tk.Label(
            master, text="Select a folder to sort:", font=("Arial", 12)
        )
        self.label.pack(pady=10)

        self.select_button = ttk.Button(
            master, text="Select Folder", command=self.select_folder
        )
        self.select_button.pack(pady=10)

        self.status_label = tk.Label(master, text="", font=("Arial", 10))
        self.status_label.pack(pady=10)

        self.sort_button = ttk.Button(
            master, text="Sort Files", command=self.sort_files
        )
        self.sort_button.pack(pady=10)

        self.progress_bar = ttk.Progressbar(
            master, orient="horizontal", length=200, mode="determinate"
        )
        self.progress_bar.pack(pady=10)

    def select_folder(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.folder_path = folder_selected
            self.status_label.config(text=f"Selected Folder: {self.folder_path}")

    def sort_files(self):
        if hasattr(self, "folder_path") and self.folder_path:
            try:
                self.status_label.config(text="Sorting files...")
                self.sort_files_and_remove_empty_folders(self.folder_path)
                self.status_label.config(text="Files sorted successfully!")
            except Exception as e:
                self.status_label.config(text=f"Error: {str(e)}")
        else:
            self.status_label.config(text="Please select a folder first.")

    def sort_files_and_remove_empty_folders(self, folder_path):
        total_files = sum(len(files) for _, _, files in os.walk(folder_path))
        current_progress = 0

        for root_dir, sub_dir, filenames in os.walk(folder_path):
            for filename in filenames:
                file_path = os.path.join(root_dir, filename)
                extension = os.path.splitext(filename)[1]

                if extension:
                    target_folder = self.create_folder(folder_path, extension)
                    target_path = os.path.join(target_folder, filename)
                    shutil.move(file_path, target_path)

                current_progress += 1
                self.update_progress(current_progress, total_files)

        self.remove_empty_folders(folder_path)
        self.progress_bar["value"] = 100  # Set progress bar to 100% after completion

    @staticmethod
    def create_folder(path: str, extension: str) -> str:
        folder_name = extension[1:]
        folder_path = os.path.join(path, folder_name)

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        return folder_path

    @staticmethod
    def remove_empty_folders(source_path: str):
        for root_dir, sub_dir, filenames in os.walk(source_path, topdown=False):
            for current_dir in sub_dir:
                folder_path = os.path.join(root_dir, current_dir)

                if not os.listdir(folder_path):
                    os.rmdir(folder_path)

    def update_progress(self, current, total):
        progress_value = int((current / total) * 100)
        self.progress_bar["value"] = progress_value
        self.master.update_idletasks()


def main():
    root = tk.Tk()
    app = FileSorterApp(root)
    root.geometry("400x300")
    root.mainloop()


if __name__ == "__main__":
    main()
