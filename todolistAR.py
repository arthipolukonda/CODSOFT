import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

TODO_FILE = "todo_list.json"

def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as file:
            return json.load(file)
    return []

def save_todos(todos):
    with open(TODO_FILE, 'w') as file:
        json.dump(todos, file)

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")

        self.todos = load_todos()

        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.task_listbox = tk.Listbox(self.frame, width=50, height=15, selectmode=tk.SINGLE)
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
        
        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        self.load_tasks()

        self.entry_task = tk.Entry(root, width=50)
        self.entry_task.pack(pady=5)

        self.button_add = tk.Button(root, text="Add Task", command=self.add_task)
        self.button_add.pack(pady=5)

        self.button_update = tk.Button(root, text="Update Task", command=self.update_task)
        self.button_update.pack(pady=5)

        self.button_complete = tk.Button(root, text="Complete Task", command=self.complete_task)
        self.button_complete.pack(pady=5)

        self.button_delete = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.button_delete.pack(pady=5)

    def load_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for idx, todo in enumerate(self.todos):
            status = "✔" if todo["completed"] else "✘"
            self.task_listbox.insert(tk.END, f"{idx+1}. [{status}] {todo['task']}")

    def add_task(self):
        task = self.entry_task.get()
        if task:
            self.todos.append({"task": task, "completed": False})
            self.entry_task.delete(0, tk.END)
            self.save_and_reload()
            messagebox.showinfo("Info", f'Task "{task}" added!')
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    def update_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            task_number = selected[0]
            new_task = simpledialog.askstring("Update Task", "Enter the new task:")
            if new_task:
                self.todos[task_number]["task"] = new_task
                self.save_and_reload()
                messagebox.showinfo("Info", "Task updated!")
        else:
            messagebox.showwarning("Warning", "No task selected!")

    def complete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            task_number = selected[0]
            self.todos[task_number]["completed"] = True
            self.save_and_reload()
            messagebox.showinfo("Info", "Task marked as completed!")
        else:
            messagebox.showwarning("Warning", "No task selected!")

    def delete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            task_number = selected[0]
            deleted_task = self.todos.pop(task_number)
            self.save_and_reload()
            messagebox.showinfo("Info", f'Task "{deleted_task["task"]}" deleted!')
        else:
            messagebox.showwarning("Warning", "No task selected!")

    def save_and_reload(self):
        save_todos(self.todos)
        self.load_tasks()

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
