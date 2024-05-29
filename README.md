# Thesis Application

This is a Django-based web application for managing theses. Follow the steps below to set up and run the application locally on your machine.

## Software Requirements

- Python
- Pip
- VSCode
- Git (CMD)
- MySQL Workbench or XAMPP (phpMyAdmin)

## Setup Instructions

1. **Fork the Repository:** Fork the repository from this [link](https://github.com/your-repository-link).

2. **Clone the Repository:** Using Git CMD, navigate to your desired directory and clone the forked repository:

   ```sh
   git clone https://github.com/your-forked-repository-link.git
   ```

3. **Change Directory:** Change the directory to the cloned repository:

   ```sh
   cd your-forked-repository
   ```

4. **Import the Database:** Using MySQL Workbench or phpMyAdmin, import the database included in the cloned repository. Ensure the database name matches the SQL file name provided.

5. **Open VSCode and Activate Virtual Environment:** Open the project in VSCode. Then, activate the virtual environment:

   ```sh
   Scripts\activate
   ```

6. **Install Dependencies:** Install all the necessary dependencies:

   ```sh
   pip install -r requirements.txt
   ```

7. **Change Directory to Project File:** Navigate to the `thesisapplication` directory:

   ```sh
   cd thesisapplication
   ```
8. **Make sure to run all migrations to ensure that the database is updated with the django-application's models.

   ```sh
   py manage.py makemigrations
   ```
   ```sh
   py manage.py migrate
   ```

9. **Run the Server:** Run the Django development server:

   ```sh
   py manage.py runserver
   ```

9. **Access the Application:** Open your web browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

10. **Log In:** Use the following credentials to log in:
    - **Username:** mfabrigas
    - **Password:** admin123

    Alternatively, you can create a new superuser account:

    ```sh
    py manage.py createsuperuser
    ```
    and add a new user using the Django Admin.
    Follow the prompts to set up your new superuser account.

## Additional Information

- **Admin Interface:** You can access the Django admin interface at [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)
- **Creating Theses:** After logging in, you can add, edit, and delete thesis entries as needed.
- **Comments:** Users can view and add comments to each thesis by clicking the thesis title.

## Troubleshooting

If you encounter issues, ensure that:
- All dependencies are installed correctly.
- The database is imported with the correct name.
- The virtual environment is activated.
- The server is running without errors.

---
