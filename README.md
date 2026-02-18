# 🎓 College ERP System

A professional, robust, and feature-rich **College Education Management System** built with Django. This system provides a comprehensive suite of tools for managing students, staff, courses, and academic operations with a premium **Corporate Deep Navy** user interface.

## ✨ Key Features

### 🏢 Administration (HOD)
- **Course & Subject Management:** Add, edit, and manage academic departments.
- **Staff & Student Management:** Streamlined registration and profile management.
- **Session Management:** Track academic years and semesters.
- **Feedback Review:** Monitor feedback from students and staff.
- **Leave Management:** Approve or reject leave applications.

### 👨‍🏫 Staff Portal
- **Attendance Tracking:** Modern interface for marking and viewing student attendance.
- **Result Management:** Add and update student exam scores.
- **Feedback System:** Direct communication channel with HOD.
- **Leave Application:** Digital workflow for leave requests.

### 👨‍🎓 Student Portal
- **Academic Dashboard:** View attendance percentages and current results.
- **Online Apply:** Submit leave requests and view status.
- **Feedback & Rating:** Provide feedback on subjects and instructors.
- **Profile Management:** Update personal details and profile picture.

## 🎨 Design & Aesthetics
The system has been professionalized with a **Corporate Deep Navy/Slate** theme:
- **Clean Interface:** Flat surfaces, subtle borders, and professional typography.
- **Corporate Branding:** Custom gear icon logo with optimized visibility.
- **Responsive Design:** Fully mobile-friendly layouts with smooth transitions.
- **Premium Login:** Re-designed entry experience with deep navy gradients and secure branding.

## 🛠 Technology Stack
- **Backend:** Python 3.13+, Django 5.1
- **Database:** SQLite (Development) / PostgreSQL (Production ready)
- **Frontend:** Vanilla CSS, JavaScript, Bootstrap 5, AdminLTE v3
- **Middleware:** WhiteNoise for optimized static asset delivery

## 🚀 Getting Started

### Prerequisites
- Python 3.13 or higher
- Pip (Python package manager)

### Installation
1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd College-ERP-main
   ```

2. **Create and Activate Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Mac/Linux
   # or
   venv\Scripts\activate     # Windows
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize Database:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the Server:**
   ```bash
   python manage.py runserver
   ```

## 🔐 Credentials (Demo)
| Role | Email | Password |
| :--- | :--- | :--- |
| **Admin (HOD)** | `admin@admin.com` | `admin123` |
| **Staff** | `staff@staff.com` | `admin123` |
| **Student** | `student@student.com` | `admin123` |

## 📜 License
Standard **MIT License**. Created and maintained by **Ashwani Rai**.

---
© 2026 Ashwani Rai. All rights reserved.