# TaskMate - Django TodoList Application

A modern, user-friendly TodoList application built with Django that helps you manage your daily tasks efficiently. TaskMate allows users to create, update, delete, and track their tasks with a clean and intuitive interface.

## 🚀 Features

- **User Authentication**: Secure user registration and login system
- **Task Management**: Create, read, update, and delete tasks
- **Task Status Tracking**: Mark tasks as completed or pending
- **Pagination**: Efficient task listing with pagination support
- **Responsive Design**: Modern Bootstrap 5 UI that works on all devices
- **User-Specific Tasks**: Each user can only see and manage their own tasks
- **Beautiful UI**: Clean and intuitive interface with color-coded task status

## 🛠️ Technology Stack

- **Backend**: Django 6.0.2
- **Database**: PostgreSQL (Production) / SQLite (Local Development)
- **Frontend**: Bootstrap 5, HTML5, CSS3, JavaScript
- **Forms**: Django Crispy Forms with Bootstrap 5
- **Deployment**: Railway.app
- **Web Server**: Gunicorn
- **Static Files**: WhiteNoise

## 📝 Usage

1. **Register a New Account**
   - Navigate to Register page
   - Fill in username, email, first name, last name, and password
   - Click Register

2. **Login**
   - Use your credentials to log in
   - You'll be redirected to the TodoList page

3. **Manage Tasks**
   - Add new tasks using the form on the TodoList page
   - Mark tasks as completed/pending
   - Update task descriptions
   - Delete tasks you no longer need

4. **View Tasks**
   - Tasks are displayed in a paginated table
   - Completed tasks are highlighted in green
   - Pending tasks are shown in white

## 🔒 Security Features

- CSRF protection enabled
- User authentication required for task management
- User-specific task isolation
- Secure password hashing
- Environment-based configuration

## 📦 Dependencies

See `requirements.txt` for the complete list of dependencies. Key packages:

- Django==6.0.2
- django-crispy-forms==2.5
- crispy-bootstrap5==2025.6
- django-environ==0.13.0
- psycopg2-binary==2.9.11
- gunicorn==25.1.0
- whitenoise==6.11.0

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.


## 🙏 Acknowledgments

- Django Framework
- Bootstrap 5
- Railway for hosting
- All contributors and users

## 🙏 Demo

Deployed on Railway - https://thetaskmate.up.railway.app/
Username: demo
Password: LearnDjango@7

**Note**: Make sure to keep your `.env` file secure and never commit it to version control. The `.env` file is already included in `.gitignore`.
