# ttracker
Backend of a project time tracking application

### How to setup the project

1. Clone the repository
`git clone <repository_url>`

2. Open the cloned repository and in the base directory, create a virtual environment with this command for linux/Mac users
`python -m venv venv `

3. Activate the virtual environment. Use this command for linux/Mac users
 `source venv/bin/activate`

4. Create a .env file for environment variables as specified in .env_example 

5. Install the requirements
 `pip install -r requirements.txt`

6. Finally, run the application, on default it runs on port 8000
 `python manage.py runserver `

7. To run tests,
    `python manage.py test`

# Endpoint Docs
To access the various endpoints in the API, visit:  
    `http://localhost:8000/docs/`