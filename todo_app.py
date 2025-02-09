import tkinter as tk
from tkinter import ttk, font, Canvas, Frame
from tkinter.constants import *

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("DarkTodo")
        self.root.geometry("400x500")
        self.root.configure(bg="#2d2d2d")
        
        # Custom dark theme colors
        self.colors = {
            "background": "#2d2d2d",
            "foreground": "#ffffff",
            "accent": "#7c4dff",
            "secondary": "#424242",
            "text": "#e0e0e0"
        }

        self.tasks = []
        self.setup_ui()
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.configure_styles()

    def configure_styles(self):
        self.style.configure("TEntry", 
                          foreground=self.colors["text"],
                          background=self.colors["secondary"],
                          insertcolor=self.colors["text"],
                          padding=5)
        
        self.style.map("TButton",
                      background=[('active', self.colors["accent"]), ('!active', self.colors["secondary"])],
                      foreground=[('active', self.colors["text"]), ('!active', self.colors["text"])])

    def setup_ui(self):
        # Header
        header_frame = tk.Frame(self.root, bg=self.colors["background"])
        header_frame.pack(pady=15, padx=20, fill=X)

        self.task_entry = ttk.Entry(header_frame, width=30, font=('Segoe UI', 12))
        self.task_entry.pack(side=LEFT, expand=True, fill=X)
        self.task_entry.bind("<Return>", lambda e: self.add_task())

        add_btn = ttk.Button(header_frame, text="➕", width=3, command=self.add_task)
        add_btn.pack(side=LEFT, padx=5)

        # Task List
        self.canvas = Canvas(self.root, bg=self.colors["background"], highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(self.root, orient=VERTICAL, command=self.canvas.yview)
        self.task_frame = Frame(self.canvas, bg=self.colors["background"])

        self.canvas.create_window((0, 0), window=self.task_frame, anchor=NW)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.task_frame.bind("<Configure>", lambda e: self.canvas.configure(
            scrollregion=self.canvas.bbox("all")
        ))

    def add_task(self):
        task_text = self.task_entry.get().strip()
        if task_text:
            task = {
                "text": task_text,
                "completed": False,
                "frame": None
            }
            self.tasks.append(task)
            self.create_task_widget(task)
            self.task_entry.delete(0, END)

    def create_task_widget(self, task):
        frame = tk.Frame(self.task_frame, bg=self.colors["secondary"], pady=5, padx=10)
        frame.pack(fill=X, pady=2)

        # Checkbox
        check_var = tk.BooleanVar(value=task["completed"])
        checkbox = ttk.Checkbutton(frame, variable=check_var, 
                                command=lambda t=task: self.toggle_task(t),
                                style="TCheckbutton")
        checkbox.pack(side=LEFT)

        # Task Text
        task_label = tk.Label(frame, text=task["text"], 
                            bg=self.colors["secondary"],
                            fg=self.colors["text"],
                            font=('Segoe UI', 11))
        task_label.pack(side=LEFT, padx=10)

        # Delete Button
        delete_btn = ttk.Button(frame, text="✖️", 
                              command=lambda t=task: self.delete_task(t),
                              style="TButton")
        delete_btn.pack(side=RIGHT)

        task["frame"] = frame
        task["check_var"] = check_var
        task["label"] = task_label

        if task["completed"]:
            self.toggle_task(task)

    def toggle_task(self, task):
        task["completed"] = not task["completed"]
        if task["completed"]:
            task["label"].config(fg="#616161", font=('Segoe UI', 11, 'overstrike'))
        else:
            task["label"].config(fg=self.colors["text"], font=('Segoe UI', 11))

    def delete_task(self, task):
        task["frame"].destroy()
        self.tasks.remove(task)

if __name__ == "__main__":
    root = tk.Tk()
    # root.tk.call('source', 'azure.tcl')
    # root.tk.call('set_theme', 'dark')
    app = TodoApp(root)
    root.mainloop()