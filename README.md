# Natural_Disaster_Management_System
A Django-based web application that allows users to report and view updates on natural disasters. The system also includes an admin interface for managing disaster reports

## Introduction
The Natural Disaster Management System is designed to help communities report and stay informed about natural disasters. Users can submit updates about disasters, and these updates can be viewed by others. The system also includes an admin interface for managing disaster reports.

## Features
- User can submit disaster updates through a form.
- Admin can manage disaster updates through the Django admin interface.
- Users can view detailed information about each disaster.
- Aesthetic and interactive home page with disaster updates.
- Navigation bar with links to different sections of the website.

### Prerequisites
- Python 3.8 or higher
- Django 3.2 or higher
- Virtualenv (optional, but recommended)

### Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/natural-disaster-management.git
    cd natural-disaster-management
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Make migrations and migrate the database:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a superuser:**
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**
   ```bash
    python manage.py runserver
    ```

7. **Open your browser and visit:**
    ```
    http://127.0.0.1:8000/
    ```

## Usage

1. **Home Page:**
   - Displays recent disaster updates.
   - Users can click on a disaster to view more details.

2. **Add Update Page:**
   - Users can submit new disaster updates using a form.

3. **View Details:**
   - Admin and users can view detailed information about specific disasters.

## Admin Interface

1. **Access the admin interface:**
   - Visit `http://127.0.0.1:8000/admin/`
   - Log in using the superuser credentials created during setup.

2. **Manage Disaster Updates:**
   - Add, edit, or delete disaster updates.


## Contributing
Contributions are what make the open source community such an amazing place to be, learn, inspire, and create. Any contributions you make are **greatly appreciated**.


