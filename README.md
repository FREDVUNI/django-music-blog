# django-music-blog
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

## Screenshot

![viberr](https://user-images.githubusercontent.com/41730664/212619110-939b41bc-784c-4076-bbc9-31876ffe1ea3.png)
