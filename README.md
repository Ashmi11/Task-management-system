# Task-management-system

A Python-based application designed to help you organize and manage your tasks efficiently.

## Features

- **User-Friendly GUI**: Intuitive graphical user interface for easy interaction.
- **Voice Commands**: Utilize voice commands to add task titles and descriptions effortlessly.
- **SQLite Database**: All tasks are stored in an SQLite database for persistent data storage.
- **Task Prioritization**: Assign priorities to tasks with options for Low, Medium, and High.
- **Team Collaboration**: Assign team members to tasks for effective collaboration.
- **Task Deletion**: Easily delete tasks using task IDs.

## Getting Started

1. **Install Dependencies**: Make sure you have Python and required libraries installed.

   a) Tkinter: Tkinter is Python's standard GUI (Graphical User Interface) package, and it is used for creating the graphical user interface of the application.
       pip install tk

   b) SpeechRecognition: This library is used for recognizing speech input, enabling voice commands for adding task titles and descriptions.
       pip install SpeechRecognition

   c) spaCy: spaCy is a natural language processing (NLP) library that may be used for more advanced text processing. However, it seems not to be extensively used in the provided code.
       pip install spacy

   d) SQLite3: This is a built-in module in Python and doesn't require a separate installation. It's used for working with SQLite databases


Unit tests have been implemented to evaluate functional and non-functional requirements.
Run the tests using the following command:
python test_task_manager_gui.py
