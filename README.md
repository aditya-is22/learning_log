# Learning Log
[![Live Demo](https://img.shields.io/badge/Live_Demo-46E2D2?style=for-the-badge&logo=render)](https://devs-learning-log.onrender.com/)

A web application built with Django that allows users to create a personal log of topics they are learning about.

## About The Project

Learning Log is a simple yet effective application designed to help users track their learning progress. Users can register for an account, create different topics they are studying, and add journal-like entries to each topic. This helps in organizing thoughts, reviewing concepts, and maintaining a consistent learning habit.

The project is built following the practices outlined in the book "Python Crash Course" by Eric Matthes.

## Features

  * **User Authentication**: Secure user registration and login system.
  * **Topic Creation**: Users can create new topics they want to learn about.
  * **Entry Logging**: Add detailed, timestamped entries for each topic to track progress and notes.
  * **Personalized Views**: Users can only see and manage their own topics and entries.
  * **Responsive Design**: A clean and simple interface built with HTML and Bootstrap.

## Built With

This project is built using the following technologies:

  * [Python](https://www.python.org/)
  * [Django](https://www.djangoproject.com/)
  * HTML
  * Bootstrap 5
  * SQLite3

## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

Make sure you have Python and pip installed on your system.

  * Python 3.x
    ```sh
    python --version
    ```

### Installation

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/aditya-is22/learning_log.git
    ```
2.  **Navigate to the project directory:**
    ```sh
    cd learning_log
    ```
3.  **Create and activate a virtual environment (recommended):**
      * On macOS and Linux:
        ```sh
        python3 -m venv ll_env
        source ll_env/bin/activate
        ```
      * On Windows:
        ```sh
        python -m venv ll_env
        ll_env\Scripts\activate
        ```
4.  **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```
5.  **Apply database migrations:**
    ```sh
    python manage.py migrate
    ```
6.  **Run the development server:**
    ```sh
    python manage.py runserver
    ```
7.  Open your web browser and go to `http://127.0.0.1:8000/`

You can now register a new account and start using the Learning Log\!

## Project Structure

```
learning_log/
├── .idea/
├── learning_log/         # Core project configuration
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── learning_logs/        # Main application for topics and entries
│   ├── migrations/
│   ├── templates/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── users/                # Application for user management
│   ├── ...
├── Procfile              # For Heroku deployment
├── db.sqlite3            # Development database
├── manage.py             # Django's command-line utility
├── requirements.txt      # Project dependencies
└── runtime.txt           # Specifies Python runtime for Heroku
```

## Contact

Aditya - [@aditya-is22](https://www.google.com/search?q=https://github.com/aditya-is22)

Project Link: [https://github.com/aditya-is22/learning\_log](https://github.com/aditya-is22/learning_log)
