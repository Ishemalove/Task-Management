Task Management / Attendance System (Django)
=========================================

Small Django app that manages contributors, tasks and attendance.

Overview
--------
- Django project root: `c:\Python\tms`
- App: `task_assignment`
- Models: `Contributor`, `Task`, `Attendance`
- Templates live in `task_assignment/templates/` (e.g. `contributor_list.html`, `mark_attendance.html`)

Requirements
------------
- Python 3.10+ (project uses 3.12 in environment)
- Django 5.2.7
- (Optional) PostgreSQL if you prefer; SQLite is supported for local development

Quick setup (SQLite local dev)
-----------------------------
1. Create a virtual environment and activate it (Windows PowerShell):

```powershell
python -m venv env
.\env\Scripts\Activate.ps1
```

2. Install requirements (if you have a `requirements.txt`):

```powershell
pip install -r requirements.txt
```

3. Run migrations and start server:

```powershell
py manage.py makemigrations
py manage.py migrate
py manage.py runserver
```

4. Open the app in your browser:

- Contributors list / mark attendance: `http://127.0.0.1:8000/mark-attendance/`
- Add contributor: `/add_contributor/` (if view enabled)

How attendance works
--------------------
- On `mark-attendance` the page lists contributors with checkboxes.
- Check boxes for contributors who are present and click "Save Attendance".
- The view creates/updates `Attendance` records for the current date with status `Present` or `Absent`.
- Saved contributors appear checked and with a "Present" badge when you reload the page for the same date.

Switching to PostgreSQL (optional)
----------------------------------
1. Create a PostgreSQL database and user (outside this README). Example:

```sql
CREATE DATABASE tms;
CREATE USER tmsuser WITH PASSWORD 'yourpassword';
GRANT ALL PRIVILEGES ON DATABASE tms TO tmsuser;
```

2. Update `tms/settings.py` DATABASES to use `django.db.backends.postgresql` and provide NAME/USER/PASSWORD/HOST/PORT.
3. Run migrations and start server.

Troubleshooting
---------------
- "relation \"attendance\" does not exist": run `py manage.py makemigrations` and `py manage.py migrate`.
- Missing templates: ensure templates live under `task_assignment/templates/` and `APP_DIRS=True` is set in settings.
- App not recognized: ensure `'task_assignment'` is present in `INSTALLED_APPS` in `tms/settings.py`.

Next improvements (suggestions)
-----------------------------
- Add date picker to `mark-attendance` to select dates other than today.
- Add admin pages for quick data management.
- Add tests for the attendance workflow.

Contact
-------
If you want more features or help wiring PostgreSQL, tell me which task to implement next.