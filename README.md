# 🛍️ Szymys E-commerce

## 🌐 Live Demo
🔗 [www.szymys-ecommerce.online](https://www.szymys-ecommerce.online)

**Django-based e-commerce app** built with Docker, PostgreSQL, and deployed to a remote Ubuntu VPS with Nginx and HTTPS support.

![Screenshot - Homepage](https://raw.githubusercontent.com/Szymys/ecommerce_project/main/ecommerce/static/media/images/GLOWNA.png)

## 🔧 Stack

- **Backend**: Django 5, Python 3.12
- **Frontend**: Bootstrap 5 (Dark Theme)
- **Database**: PostgreSQL
- **Web server**: Nginx (with HTTPS via Certbot)
- **Deployment**: Docker & Docker Compose
- **Hosting**: Contabo VPS (Ubuntu 22.04)

---

## 🚀 Features

- 🛒 Product listing, categories, cart, checkout
- 🔒 User authentication (login/register + email activation link)
- ✅ Form validation with custom error messages
- 👤 **User Panel** with:
  - 🧾 Order history
  - 🏠 Delivery address
  - ✏️ Email & personal data update
- 🧑‍💻 **Admin panel** for:
  - Managing products & categories
  - Viewing and managing user orders
  - Editing user accounts
- 📬 Activation email sent on registration
- 🐳 Fully containerized with Docker
- 📦 Static/media file handling via Nginx

---

## ⚙️ Quick Start (Local Dev)

# 1. Clone the repo
https://github.com/Szymys/ecommerce_project

# 2. Create a .env file (in project root, same level as docker-compose.local.yml)
# Here's an example of what to put in it:

# SECRET_KEY=your_secret_key
# DEBUG=True
# POSTGRES_DB=ecommerce_db
# POSTGRES_USER=ecommerce_user
# POSTGRES_PASSWORD=securepassword
# EMAIL_HOST=smtp.gmail.com
# EMAIL_PORT=587
# EMAIL_USE_TLS=True
# EMAIL_HOST_USER=your.email@gmail.com
# EMAIL_HOST_PASSWORD=your_app_password

# 3. Run the app with Docker
docker-compose -f docker-compose.local.yml up --build
