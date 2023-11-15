# Django_homework

1. Clone this repository to your local machine.
2. Change services.app.environment's `EMAIL_HOST`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD` to send registration emails.
3. Run 'docker-compose up --scale app=3'.
4. Browse to http://127.0.0.1/ to test registration and login (after the user clicks the activation link in the email and confirms the account is able to log in).
5. Open another terminal in the same folder to run 'docker-compose run app python manage.py createsuperuser'. (Create an admin user to log in at http://127.0.0.1/admin)
6. Bonus: When a user is active and is staff and successfully logs in, there is a new inserted record in admin's Employee. (http://127.0.0.1/admin)
7. Other: Use redis as user session cache. Use git flow.


---
- Python 1.11
- Django 4.2.7
- DB Postgres 13
- Nginx latest 
- Redis latest alpine
<img width="1197" alt="image" src="https://github.com/Gocrazy/Django_homework/assets/106258/576e18b8-876b-4553-b717-4e3c8b8815cc">
