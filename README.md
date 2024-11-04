# Django Music Album App

This is a Django app that displays a collection of music albums, allows users to mark favorite albums, and provides a search functionality for finding albums by title or artist.

## Installation

1. Clone the repository: `git clone https://github.com/FREDVUNI/django-music-album-app.git`
2. Navigate to the project directory: `cd django-music-album-app`
3. Install dependencies: `pip install -r requirements.txt`
4. Create a `.env` file by copying `.env.example` and updating the values for your local environment: `cp .env.example .env`
5. Set up your local PostgreSQL database by updating the `DATABASE_URL` value in the `.env` file
6. Run database migrations: `python manage.py migrate`
7. Create a superuser account: `python manage.py createsuperuser`
8. Start the development server: `python manage.py runserver`

## Usage

To access the app, navigate to `http://localhost:8000` in your browser. You can view a list of music albums, mark favorite albums, and search for albums by title or artist.

To add new albums, log in to the admin interface at `http://localhost:8000/admin/` using your superuser account and add albums to the `Albums` table.

## Technologies Used

- Django
- sQLite
- HTML/CSS
- Bootstrap

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request. 

## Screenshots

![image](https://github.com/user-attachments/assets/f08ad562-6830-4929-bc39-72b22e2f30d1)
![image](https://github.com/user-attachments/assets/187bfbf5-19a7-45cf-90ee-36784138d385)
![image](https://github.com/user-attachments/assets/cebcada1-a930-430e-a7f9-b1809a55919a)



