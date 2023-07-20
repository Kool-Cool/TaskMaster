# TaskMaster
![Star Badge](https://img.shields.io/static/v1?label=%F0%9F%8C%9F&message=If%20Useful&style=style=flat&color=BC4E99)
![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)


"TO-DO" webapp from "flask" #CRUD 

## Preview 
![](https://github.com/Kool-Cool/dump-/blob/main/taskmaster_flask_todo.png)

# Flask Todo App 

This documentation provides an overview of the Flask Todo web application. The application is designed to manage and organize tasks in a simple and user-friendly manner.

## Table of Contents

1. Introduction
2. Features
3. Dependencies
4. Installation
5. Usage
6. Routes
7. Models
8. Contributing
9. License

## 1. Introduction

The Flask Todo web application allows users to create, view, update, and delete tasks. It utilizes the Flask web framework along with SQLAlchemy for database management. Users can add tasks with a content description and a timestamp to track their creation date. The application provides a simple and intuitive user interface for managing tasks efficiently.

## 2. Features

- Add new tasks with content and timestamp
- View all tasks in chronological order
- Update task content
- Delete tasks
- About page providing information about the application
- Connect page with links to social media and contact information

## 3. Dependencies

- Flask: A micro web framework for Python
- Flask-SQLAlchemy: An extension to handle SQLAlchemy database integration

## 4. Installation

1. Clone the repository from GitHub:
```
git clone https://github.com/your-username/flask-todo-app.git
```


2. Navigate to the project directory:
```
cd flask-todo-app
```


3. Create a virtual environment (optional but recommended):
```
python -m venv venv
```

4. Activate the virtual environment (Windows):
```
venv\Scripts\activate
```
or (macOS/Linux):
```
source venv/bin/activate
```


5. Install the required dependencies:
```
pip install Flask Flask-SQLAlchemy
```

## 5. Usage

1. Run the application:
```
python app.py
```

2. Open your web browser and navigate to `http://localhost:5000/` to access the Todo app.

## 6. Routes

- `/`: Home page where users can view, add, and manage tasks.
- `/about`: About page providing information about the application.
- `/connect`: Connect page with links to social media and contact information.
- `/delete/<int:id>`: Route to delete a specific task with the given `id`.
- `/update/<int:id>`: Route to update the content of a specific task with the given `id`.

## 7. Models

### Todo Model

- `id`: Primary key for each task entry.
- `content`: Content description of the task.
- `date_created`: Timestamp of task creation (defaulted to the current date and time).

## 8. Contributing

Contributions to the Flask Todo web application are welcome. If you find any issues or have suggestions for improvement, feel free to open an issue or submit a pull request on GitHub.

## 9. License

The Flask Todo web application is open-source software released under the [MIT License](LICENSE).

---
This concludes the documentation for the Flask Todo web application. Happy coding