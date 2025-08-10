# 📝 Django Blog

A fully functional blog application built with **Django** that allows users to sign up, log in, create posts, comment on posts, and manage their own content.  
Perfect for learning Django’s authentication, forms, and template system — or as a base for your own blog website.

---

## 🚀 Features

- **User Authentication**: Sign up, log in, and log out securely.
- **Create & Manage Posts**: Add, edit, and delete your own blog posts.
- **Comment System**: Leave comments on posts to engage with readers.
- **Responsive Design**: Works smoothly across desktop and mobile devices.
- **Static Files & Images**: Organized media handling for blog images and user uploads.

---

## 📸 Screenshots

<img width="1919" height="905" alt="Sign Up" src="https://github.com/user-attachments/assets/912941f5-14ff-4ca0-b921-cdbc987bfbe7" />
<img width="1919" height="900" alt="My Posts and Delete Posts" src="https://github.com/user-attachments/assets/5ac3e258-1dc9-4472-ba7b-7c310ed3c6ea" />
<img width="1917" height="903" alt="Log In" src="https://github.com/user-attachments/assets/b6386828-d2cc-418e-a2aa-ba72fc6aad31" />
<img width="1919" height="909" alt="home" src="https://github.com/user-attachments/assets/06f6e1e0-3a0a-4a46-a99c-fa331f8d6478" />
<img width="1919" height="905" alt="Create posts" src="https://github.com/user-attachments/assets/a9200ae6-1204-4641-b7be-0407a377fd1d" />


---

## 🛠️ Technologies Used

- **Backend**: [Django](https://www.djangoproject.com/)
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: SQLite (default, can be swapped for PostgreSQL/MySQL)
- **Version Control**: Git & GitHub

---

## 📂 Project Structure
Django_blog/
├── Django_blog/ # Project settings and URLs
├── blog/ # Main blog app
│ ├── migrations/ # Database migrations
│ ├── static/ # CSS, JS, images
│ ├── templates/ # HTML templates
│ ├── admin.py # Django admin configuration
│ ├── forms.py # Forms for posts & comments
│ ├── models.py # Database models
│ └── views.py # Application logic
├── Screenshots/ # Project screenshots
└── manage.py # Django project manager


---

## ⚙️ Installation & Setup

1. **Clone the repository**
    ```bash
    git clone https://github.com/harshsharma2004/Django_blog.git
    cd Django_blog
    ```

2. **Create and activate a virtual environment**
    ```bash
    python -m venv .venv
    .venv\Scripts\activate    # Windows
    source .venv/bin/activate # macOS/Linux
    ```

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply database migrations**
    ```bash
    python manage.py migrate
    ```

5. **Run the development server**
    ```bash
    python manage.py runserver
    ```

6. **Open in your browser**
    ```
    http://127.0.0.1:8000/
    ```

---

## 🌐 Deployment

You can deploy this project using:
- **Heroku**
- **PythonAnywhere**
- **Railway**
- **Render**
  
For production, remember to:
- Use a production-ready server (e.g., Gunicorn)
- Set `DEBUG = False` in `settings.py`
- Configure static and media file hosting

---

## 🤝 Contributing

Contributions are welcome!  
If you’d like to add new features or fix bugs:
1. Fork this repository
2. Create a new branch (`feature/amazing-feature`)
3. Commit your changes
4. Push to your branch
5. Open a pull request

---

## 📜 License

This project is licensed under the **MIT License** — you are free to use, modify, and distribute it.

---

## 👨‍💻 Author

**Harsh Sharma**  
📧 Email: harsh.141615@gmail.com 
🌐 GitHub: [harshsharma2004](https://github.com/harshsharma2004)

---

> “Code is like humor. When you have to explain it, it’s bad.” – Cory House
