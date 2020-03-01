# Back-end Travel Simple

Back-end of the application Travel Simple.

## Environment

- Python: 3.8.2
- Django: 3.0.3
- SQLite: 3.8.3 (most recent, native of Django)

## How to run

Access `backend-travel-simple` project directory from a terminal, run the command `python manage.py runserver 0.0.0.0:8000`. To verify it's working properly, open the URL `http://localhost:8000/api/host/<host_number>` or `http://localhost:8000/api/bedroom/<bedroom-number>` from a browser of your preference.

## How to add data

To add new data to the SQLite database, access `http://localhost:8000/admin` with administrator credentials and add data from the admin dashboard.
