# Django Music Album App

This is a Django app that displays a collection of music albums, allows users to mark favorite albums, and provides a search functionality for finding albums by title or artist.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/FREDVUNI/django-music-blog.git
   ```

2. Navigate to the project directory:

   ```bash
   cd django-music-blog/website
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file by copying `.env.example` and updating the values for your local environment:

   ```bash
   cp .env.example .env
   ```

5. Since we are using SQLite, ensure that your `DATABASES` setting in `settings.py` is configured correctly (the default settings provided in the template should work out of the box).

6. Run database migrations:

   ```bash
   python manage.py migrate
   ```

7. Create a superuser account:

   ```bash
   python manage.py createsuperuser
   ```

8. Start the development server:

   ```bash
   python manage.py runserver
   ```

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