# Learning Log

[![Live Demo](https://img.shields.io/badge/Live_Demo-46E2D2?style=for-the-badge&logo=render)](https://devs-learning-log.onrender.com/)

A web-based application built with Django that enables users to register an account and keep a log of topics they are learning. Each user can create topics, add timestamped entries, and organize their personal learning journey.

---

## Table of Contents

- [About The Project](#about-the-project)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Contributing](#contributing)
- [Contact](#contact)

---

## About The Project

Learning Log is designed to help individuals track what they're studying, jot down notes, and maintain a record of their learning progress. The application follows best practices for usability, privacy, and responsive design, providing a simple yet robust tool for lifelong learners.

---

## Features

- **User Authentication:** Secure registration, login, and logout system.
- **Topic Management:** Create, view, and delete custom topics for different subjects.
- **Entry Logging:** Add detailed, timestamped entries under each topic, supporting rich text formatting.
- **Personalized Views:** Each user sees and manages only their own topics and entries.
- **Search Functionality:** Quickly find topics or entries using the built-in search bar.
- **Responsive UI:** Clean, modern interface built with Bootstrap 5.
- **Rich Text Support:** Integration with [Django Summernote](https://github.com/summernote/django-summernote) for enhanced entry formatting.

---

## Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, Bootstrap 5, Django Templates
- **Database:** SQLite3 (default; easy to switch to PostgreSQL/MySQL for production)
- **Other:** Django Summernote, Django Auth

---

## Getting Started

Follow these steps to set up the project locally.

### Prerequisites

- Python 3.x
- pip (Python package manager)
- git (optional, for cloning)

### Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/aditya-is22/learning_log.git
    cd learning_log
    ```

2. **Create and activate a virtual environment:**
    - macOS/Linux:
      ```sh
      python3 -m venv ll_env
      source ll_env/bin/activate
      ```
    - Windows:
      ```sh
      python -m venv ll_env
      ll_env\Scripts\activate
      ```

3. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Apply database migrations:**
    ```sh
    python manage.py migrate
    ```

5. **Run the development server:**
    ```sh
    python manage.py runserver
    ```

6. Open your browser and visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to start using Learning Log!

---

## Project Structure

```
learning_log/
├── learning_log/         # Django project config (settings, core URLs)
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── learning_logs/        # App for topics and entries
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   ├── templates/
│   └── ...
├── users/                # App for registration and authentication
│   ├── views.py
│   ├── urls.py
│   └── ...
├── static/               # Static files (CSS, images, etc.)
│   └── css/
├── requirements.txt      # Python dependencies
├── db.sqlite3            # Default SQLite database
├── manage.py             # Django command-line utility
├── Procfile              # For deployment (e.g., Heroku)
└── runtime.txt           # Python runtime version for deployment
```

---

## Usage

- **Register:** Create a user account to begin.
- **Create Topics:** Start a new topic for any subject you're learning.
- **Add Entries:** Log what you've learned under each topic, attach formatted notes, and review your progress.
- **Search:** Use the search bar to quickly find specific topics or entries.
- **Edit:** Manage your topics and entries as needed.

---

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a feature branch (`git checkout -b my-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin my-feature`).
5. Open a pull request.

---


## Contact

Aditya - [GitHub Profile](https://github.com/aditya-is22)

Project Link: [https://github.com/aditya-is22/learning_log](https://github.com/aditya-is22/learning_log)

---
