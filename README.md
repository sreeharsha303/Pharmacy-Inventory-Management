# Pharmacy Inventory Management System (Django)

A beginner-friendly mini project to manage medicines in a pharmacy.

## Features
- Dashboard with medicine count, low-stock count, and expired/expiring-soon count
- Add, view, edit, and delete medicine records
- Search medicines by name, category, or batch number
- Low-stock warning
- Expiry status (Expired / Expiring soon / Good)
- Login page and protected inventory pages (Django authentication)
- SQLite database by default (no separate database setup required)

## Requirements
- Python 3.10 or newer
- pip

## Run on Windows (VS Code / Command Prompt)

1. Extract the ZIP file.
2. Open the extracted `pharmacy_inventory_django` folder in VS Code.
3. Open Terminal in that folder.
4. Create and activate a virtual environment:

   ```bat
   python -m venv venv
   venv\Scripts\activate
   ```

5. Install dependencies:

   ```bat
   python -m pip install -r requirements.txt
   ```

6. Create database tables:

   ```bat
   python manage.py makemigrations inventory
   python manage.py migrate
   ```

7. (Optional) Create an admin account:

   ```bat
   python manage.py createsuperuser
   ```

8. Start the server:

   ```bat
   python manage.py runserver
   ```

9. Create a login account if you have not already done so:

   ```bat
   python manage.py createsuperuser
   ```

10. Open http://127.0.0.1:8000/login/ and sign in using that account.
    After login, you will be redirected to the dashboard.

Admin page: http://127.0.0.1:8000/admin/

## Notes
- The project uses SQLite by default so it runs immediately for a mini-project demo.
- Do not use this demo app to manage real pharmacy inventory or patient information.
