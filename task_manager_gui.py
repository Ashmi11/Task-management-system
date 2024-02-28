# gui/task_manager_gui.py
# gui/task_manager_gui.py
import tkinter as tk
from tkinter import Entry, Label, Button, Text, OptionMenu, BooleanVar, Checkbutton, StringVar, Toplevel, messagebox, \
    Scrollbar, Listbox

from task import Task
from task_routes import TaskManager

import speech_recognition as sr
import spacy


class TaskManagerGUI:
    def __init__(self, root):

        self.root = root
        self.root.title("Task Manager")

        self.create_main_page()
        self.listbox = Listbox(self.root, width=50, height=10)
        self.listbox.pack()
        self.listbox_frame = None
        self.root.configure(bg='#FFFFCC')

        # Initialize speech recognition and spaCy
        self.recognizer = sr.Recognizer()
        self.nlp = spacy.load("en_core_web_sm")

        # Initialize task manager
        self.task_manager = TaskManager()

    def create_main_page(self):
        self.title_label = Label(self.root, text="Title:",bg='#ADD8E6',highlightthickness=2, highlightbackground='#000080',  # Dark blue outline
                                        font=('Helvetica', 12, 'bold'), fg='#8B4513')
        self.title_label.pack()

        self.title_entry = Entry(self.root)
        self.title_entry.pack()

        self.desc_label = Label(self.root, text="Description:",bg='#ADD8E6',highlightthickness=2, highlightbackground='#000080',  # Dark blue outline
                                        font=('Helvetica', 12, 'bold'), fg='#8B4513')
        self.desc_label.pack()

        self.desc_entry = Text(self.root, height=5, width=30)
        self.desc_entry.pack()

        self.priority_label = Label(self.root, text="Priority:", bg='#ADD8E6', highlightthickness=2, highlightbackground='#000080',  # Dark blue outline
                                        font=('Helvetica', 12, 'bold'), fg='#8B4513')
        self.priority_label.pack()

        self.priority_var = StringVar(self.root)
        self.priority_var.set("Medium")  # Default priority
        priorities = ["Low", "Medium", "High"]
        self.priority_menu = OptionMenu(self.root, self.priority_var, *priorities)
        self.priority_menu.pack()

        self.urgent_var = BooleanVar(self.root)
        self.urgent_checkbox = Checkbutton(self.root, text="Urgent", variable=self.urgent_var, bg='#ADD8E6', highlightthickness=2, highlightbackground='#000080',  # Dark blue outline
                                        font=('Helvetica', 12, 'bold'), fg='#8B4513')
        self.urgent_checkbox.pack()

        self.metric_label = Label(self.root, text="Custom Metric:", bg='#ADD8E6',highlightthickness=2, highlightbackground='#000080',  # Dark blue outline
                                        font=('Helvetica', 12, 'bold'), fg='#8B4513')
        self.metric_label.pack()

        self.metric_entry = Entry(self.root)
        self.metric_entry.pack()

        self.team_members_label = Label(self.root, text="Team Members (comma-separated):",bg='#ADD8E6',highlightthickness=2, highlightbackground='#000080',  # Dark blue outline
                                        font=('Helvetica', 12, 'bold'), fg='#8B4513')
        self.team_members_label.pack()

        self.team_members_entry = Entry(self.root)
        self.team_members_entry.pack()

        self.add_button = Button(self.root, text="Add Task", command=self.add_task,bg='#ADD8E6',highlightthickness=2, highlightbackground='#000080',  # Dark blue outline
                                        font=('Helvetica', 12, 'bold'), fg='#8B4513')
        self.add_button.pack()

        self.voice_button = Button(self.root, text="Voice Command Section", command=self.create_voice_page,bg='#ADD8E6',highlightthickness=2, highlightbackground='#000080',  # Dark blue outline
                                        font=('Helvetica', 12, 'bold'), fg='#8B4513')
        self.voice_button.pack()

        self.show_all_button = Button(self.root, text="Show All Tasks", command=self.show_all_tasks,bg='#ADD8E6',highlightthickness=2, highlightbackground='#000080',  # Dark blue outline
                                        font=('Helvetica', 12, 'bold'), fg='#8B4513')
        self.show_all_button.pack()

        self.delete_task_button = Button(self.root, text="Delete Task", command=self.delete_task,bg='#ADD8E6',highlightthickness=2, highlightbackground='#000080',  # Dark blue outline
                                        font=('Helvetica', 12, 'bold'), fg='#8B4513')
        self.delete_task_button.pack()

    def create_voice_page(self):
        voice_page = Toplevel(self.root,bg='#FFFFCC')
        voice_page.title("Voice Command Section")


        self.voice_add_title_button = Button(voice_page, text="Add Task Title (Voice)", command=self.voice_add_title, bg='#ADD8E6',highlightthickness=2, highlightbackground='#000080',  # Dark blue outline
                                        font=('Helvetica', 12, 'bold'), fg='#8B4513')
        self.voice_add_title_button.pack()

        self.voice_add_desc_button = Button(voice_page, text="Add Task Description (Voice)",
                                            command=self.voice_add_description, bg='#ADD8E6',highlightthickness=2, highlightbackground='#000080',  # Dark blue outline
                                        font=('Helvetica', 12, 'bold'), fg='#8B4513')
        self.voice_add_desc_button.pack()

        self.voice_add_task_button = Button(voice_page, text="Add Task (Voice)", command=self.voice_add_task, bg='#ADD8E6',highlightthickness=2, highlightbackground='#000080',  # Dark blue outline
                                        font=('Helvetica', 12, 'bold'), fg='#8B4513')
        self.voice_add_task_button.pack()

        self.show_info_label = Label(voice_page, text="")
        self.show_info_label.pack()

        back_button = Button(voice_page, text="Back to Main Page", command=voice_page.destroy, bg='#ADD8E6',highlightthickness=2, highlightbackground='#000080',  # Dark blue outline
                                        font=('Helvetica', 12, 'bold'), fg='#8B4513')
        back_button.pack()

    def add_task(self):
        title = self.title_entry.get()
        description = self.desc_entry.get("1.0", "end-1c")
        priority = self.priority_var.get()
        is_urgent = self.urgent_var.get() == 1
        custom_metric = self.metric_entry.get()
        team_members = [name.strip() for name in self.team_members_entry.get().split(',') if name.strip()]

        # Data validation
        if not title:
            messagebox.showwarning("Warning", "Title cannot be empty. Please enter a title.")
            return

        # Add logic to add task to the manager
        self.task_manager.add_task(title, description, priority, is_urgent, custom_metric, team_members)
        messagebox.showinfo("Success",
                            f"Task added successfully - Title: {title}, Priority: {priority}, Urgent: {is_urgent}, Metric: {custom_metric}")

    def voice_add_title(self):
        with sr.Microphone() as source:
            self.show_info_label.config(text="Speak the task title.")
            self.root.update()
            audio = self.recognizer.listen(source)

        try:
            title = self.recognizer.recognize_google(audio)
            self.title_entry.delete(0, tk.END)
            self.title_entry.insert(0, title)
            self.show_info_label.config(text=f"Task title set to: {title}")

        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

    def voice_add_description(self):
        with sr.Microphone() as source:
            self.show_info_label.config(text="Speak the task description.")
            self.root.update()
            audio = self.recognizer.listen(source)

        try:
            description = self.recognizer.recognize_google(audio)
            self.desc_entry.delete("1.0", tk.END)
            self.desc_entry.insert(tk.END, description)
            self.show_info_label.config(text=f"Task description set to: {description}")

        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

    def voice_add_task(self):
        title = self.title_entry.get()
        description = self.desc_entry.get("1.0", "end-1c")
        priority = self.priority_var.get()
        is_urgent = self.urgent_var.get() == 1
        custom_metric = self.metric_entry.get()
        team_members = [name.strip() for name in self.team_members_entry.get().split(',') if name.strip()]

        # Set default values for missing attributes

        if not priority:
            priority = "Medium"
        if custom_metric == "":
            custom_metric = "Not specified"
        if not team_members:
            team_members = []  # Default: Empty list for team members

        # Add logic to add task to the manager
        self.task_manager.add_task(title, description, priority, is_urgent, custom_metric, team_members)
        messagebox.showinfo("Success",
                            f"Task added successfully - Title: {title}, description: {description}, Priority: {priority}, Urgent: {is_urgent}, Metric: {custom_metric},team_members: {team_members}")

    def show_all_tasks(self):
        tasks = self.task_manager.get_tasks()
        if tasks:
            self.listbox.delete(0, tk.END)  # Clear previous entries
            for task in tasks:
                self.listbox.insert(tk.END,
                                    f"ID: {task[0]}, Title: {task[1]}")  # Assuming task[0] is task_id and task[1] is title

        else:
            messagebox.showinfo("No Tasks", "There are no tasks to display.")
    def delete_task(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            task_id_to_delete = int(self.listbox.get(selected_index).split(',')[0].split(': ')[1])
            confirm_delete = messagebox.askyesno("Delete Task",
                                                 f"Do you want to delete task with ID {task_id_to_delete}?")
            if confirm_delete:
                self.task_manager.delete_task(task_id_to_delete)
                messagebox.showinfo("Success", f"Task with ID {task_id_to_delete} deleted successfully.")
                self.show_all_tasks()  # Refresh the displayed tasks after deletion
        else:
            messagebox.showinfo("Select Task", "Please select a task to delete.")

    def create_listbox(self):
        self.listbox = Listbox(self.root, width=50, height=10)
        self.listbox.pack()
        scrollbar = Scrollbar(self.listbox_frame, orient=tk.VERTICAL)
        self.listbox = Listbox(self.listbox_frame, yscrollcommand=scrollbar.set, selectmode=tk.SINGLE)
        scrollbar.config(command=self.listbox.yview)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def measure_response_time(self):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerGUI(root)
    app.create_listbox()  # Call create_listbox method to initialize Listbox
    root.mainloop()
