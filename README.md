# Introduction

This document presents the project structure for a web-based application that can significantly benefit various organizations such as ambulatory care services, drug stores, and similar entities. The primary aim is to develop an MVP (Minimum Viable Product) that centers on key functionalities crucial for enhancing operational efficiency in patient or client management and route optimization. In line with the MVP strategy, certain aspects like patient or client data are deliberately simplified to meet the minimum necessary requirements for the application's effective functioning. This approach ensures a concentrated development effort on the essential features, providing immediate practical benefits.

The application is designed to streamline management processes and route planning, offering a straightforward digital interface for easy interaction. It employs modern web technologies to facilitate effective communication between the front-end and back-end via API and JSON. This is vital for ensuring real-time data exchange, a necessity in the fast-paced environments of healthcare and retail. Deployed on Heroku, the application guarantees reliable access and scalability to cater to the dynamic needs of various service providers. Beyond being a technological tool, this application is envisioned as a means to advance more personalized, efficient, and customer-centric service delivery.

# Frontend-URL "gh-pages"
https://dashdothub.github.io/PlanRoute/#/
# Backend-URL "heroku"
https://planroute-6bd1a349d590.herokuapp.com

# Epics and User Stories

## Epic 1: Build Frontend

### User Story 1.1
As a visitor, I want to access a landing page with overall information about the application, so I can understand its purpose and features.

### User Story 1.2
As a visitor, I want the ability to register for an account or log in, so I can access personalized features of the application.

### User Story 1.3
As a logged-in user, I want to be redirected to a dashboard where I can manage patients, so I can easily add or edit patient information.

### User Story 1.4
As a user, I want to view a grid or table of patients, so I can select them for route planning.

### User Story 1.5
As a user, I want to click a button to calculate routes between selected patients, so I can efficiently plan visits or appointments.

## Epic 2: Build Backend

### User Story 2.1
As a system, I need to securely handle user registration and login, so that user data is protected.

### User Story 2.2
As a system, I need to store and manage patient information, so that users can add, view, and edit patient details.

### User Story 2.3
As a system, I need an API to communicate with the frontend using JSON, to manage and provide patient data and calculated routes.

## Epic 3: Deploy on Heroku

### User Story 3.1
As a developer, I want to deploy the application on Heroku, so that it is accessible online for users.

### User Story 3.2
As a system administrator, I want to ensure that the application runs smoothly on Heroku, with necessary resources and configurations in place.

## Epic 4: Create API for Frontend-Backend Communication

### User Story 4.1 - RESTful API Development
As a developer, I want to develop a RESTful API for efficient communication between the frontend and backend.

### User Story 4.2 - API Documentation
As a developer, I want to document the API, so that it is easy for other developers to understand and use.

### User Story 4.3 - Frontend Integration with API
As a frontend developer, I want to integrate the frontend application with the backend API.

## Epic 5: Ensure Application Security

### User Story 5.1
As a system, I need to implement robust security measures, so that user data and patient information are protected against unauthorized access and breaches.

## Epic 6: User Experience and Interface Design

### User Story 6.1
As a user, I want a user-friendly interface, so that I can navigate and use the application with ease.

### User Story 6.2
As a user, I want clear and informative feedback from the system, so that I can understand the outcomes of my actions (like successful patient additions, errors, etc.).

## Epic 7: Testing and Quality Assurance

### User Story 7.1
As a developer, I want to thoroughly test the application, so that users encounter minimal bugs and issues.

### User Story 7.2
As a user, I expect a reliable and consistent performance, so that I can trust and effectively use the application.

# Local Deployment Guide for this Project

## Prerequisites
- Basic knowledge of using terminal/bash/shell.
- Git installed on your system (optional).

## Installing Python LTS (Long Term Support)

Python is a critical component for running Django applications. Here's how you can install the latest Long Term Support (LTS) version of Python:

### For Windows Users

1. **Download the Installer:**
   - Visit the official Python website: [Python Downloads](https://www.python.org/downloads/)
   - Download the latest LTS version (e.g., Python 3.9.x) for Windows.

2. **Run the Installer:**
   - Execute the downloaded file.
   - Ensure to check the box that says **"Add Python 3.x to PATH"** at the beginning of the installation process.
   - Click **Install Now**.

3. **Verify Installation:**
   - Open Command Prompt and type `python --version`.
   - You should see the Python version number if the installation was successful.

### For macOS Users

1. **Install Homebrew (if not already installed):**
   - Open Terminal.
   - Paste `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"` and press Enter.
   - Follow the on-screen instructions.

2. **Install Python via Homebrew:**
   - In the Terminal, type `brew install python@3.9` (replace `3.9` with the latest LTS version).
   - Wait for the installation to complete.

3. **Verify Installation:**
   - In the Terminal, type `python3 --version`.
   - You should see the Python version number if the installation was successful.

### For Linux Users

1. **Update Package Lists:**
   - Open Terminal.
   - Run `sudo apt-get update` to update package lists.

2. **Install Python:**
   - Run `sudo apt-get install python3.9` (replace `3.9` with the latest LTS version).

3. **Verify Installation:**
   - Type `python3 --version` in the Terminal.
   - The installed Python version number should be displayed.

## Installing npm (Node Package Manager)

npm is a package manager for JavaScript, and is necessary for managing and installing packages for Vue.js projects. Here's how to install npm, which is distributed with Node.js:

### For Windows Users

1. **Download Node.js Installer:**
   - Visit the official Node.js website: [Node.js Downloads](https://nodejs.org/en/download/)
   - Download the installer for Windows (choose LTS version for long-term support).

2. **Run the Installer:**
   - Execute the downloaded file.
   - Follow the installation prompts, ensuring that npm is included in the installation.

3. **Verify Installation:**
   - Open Command Prompt.
   - Type `node -v` and `npm -v`.
   - If the installation was successful, you should see the installed versions of Node.js and npm.

### For macOS Users

1. **Install Homebrew (if not already installed):**
   - Open Terminal.
   - Paste `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"` and press Enter.
   - Follow the on-screen instructions.

2. **Install Node.js and npm via Homebrew:**
   - In the Terminal, type `brew install node`.
   - Wait for the installation to complete.

3. **Verify Installation:**
   - In the Terminal, type `node -v` and `npm -v`.
   - You should see the version numbers of Node.js and npm if the installation was successful.

### For Linux Users (Debian/Ubuntu)

1. **Update Package Lists:**
   - Open Terminal.
   - Run `sudo apt-get update` to update package lists.

2. **Install Node.js and npm:**
   - Run `sudo apt-get install nodejs npm`.

3. **Verify Installation:**
   - Type `node -v` and `npm -v` in the Terminal.
   - The installed versions of Node.js and npm should be displayed.

## Initial Setup

### Clone the Repository
- Command: `git clone <repository-url>`
- This command clones the project repository from GitHub to your local machine.

### Navigate to Project Directory
- Command: `cd <project-name>`

## Backend Setup (Django)

### Create and Activate a Virtual Environment
- For macOS/Linux:
  - Create: `python3 -m venv venv`
  - Activate: `source venv/bin/activate`
- For Windows:
  - Create: `python -m venv venv`
  - Activate: `.\venv\Scripts\activate`

### Install Required Packages
- Command: `pip install -r requirements.txt`
- This installs all the Python packages listed in the `requirements.txt` file.

### Setting up `env.py`
- Create a file `env.py` in the project root.
- Insert the following content:
  ```python
  import os

  # Set environment variables
  os.environ['API_KEY'] = '<your_tomtom_api_key>'
  os.environ['DEVELOPMENT'] = 'True'
  os.environ['DATABASE_URL'] = 'postgres://<user>:<password>@<host>:<port>/<dbname>'
  os.environ.setdefault('SECRET_KEY', '<your_django_secret_key>')
   ```
- Replace placeholders with your actual credentials.

### Database Setup
- Register and create a new PostgreSQL database using ElephantSQL or another service.
- Update the `DATABASE_URL` in `env.py` with your database credentials.

### Migrate Database
- Command: `python manage.py migrate`
- This sets up your database schema.

### Create Django Superuser
- Command: `python manage.py createsuperuser`
- Follow the prompts to create a new admin user.

## Frontend Setup (Vue.js)

### Navigate to Frontend Directory
- Command: `cd <frontend-directory>`

### Install Node.js Packages
- Command: `npm install`
- This installs the required Node.js packages for the Vue.js frontend.

## Running the Application

### Start Django Backend Server
- Command: `python manage.py runserver`
- This starts the Django development server.

### Start Vue.js Frontend Server
- In a new terminal, navigate to the frontend directory and run:
  - Command: `npm run serve`
  - This starts the Vue.js development server.

### Access the Application
- The Django server typically runs at `http://127.0.0.1:8000`
- The Vue.js frontend can usually be accessed at `http://localhost:8080`

# Complete List of Environment Variables

Environment variables are used to configure various aspects of the application. Here's a breakdown of the variables and their descriptions:

- `API_KEY`: The API key used for accessing external services. Here it is TomTom, available at TomTom, free tier possible.
- `DEVELOPMENT`: Specifies whether the application is in development mode. Set to `True` for development and `False` for production.
- `DATABASE_URL`: The URL for connecting to the PostgreSQL database.
- `SECRET_KEY`: A secret key used for cryptographic signing in Django applications.
- `EMAIL_ADDRESS`: The email address used for sending emails from the application.
- `EMAIL_PASSWORD`: The password associated with the email address for email authentication. For 2FA eMails, an application password needs to be created.
- `PRODUCTION_URL`: The URL of the production server. (Frontend). Needed for the correct email token redirect link, without slash at the end.
- `PROD_ALLOWED_HOSTS`: Comma-separated list of allowed hosts in production.
- `PROD_CSRF_TRUSTED_ORIGINS`: Comma-separated list of origins that are trusted for Cross-Origin Resource Sharing (CORS) and Cross-Site Request Forgery (CSRF) protection in production.
- `PROD_CORS_ALLOWED_ORIGINS`: Comma-separated list of origins allowed for CORS requests in production.
- `PROD_CORS_ALLOW_CREDENTIALS`: Boolean value indicating whether to allow credentials in CORS requests in production.
- `RUNNING_TESTS`: Specifies whether tests are currently running. Set to `True` during test execution.
- `DEVELOPMENT_URL`: The URL of the development server, this way you can debug your application on e.g. heroku, paste here the url and set DEVELOPMENT to true.
- `ACCESS_TOKEN_LIFETIME`: Lifetime of access tokens in minutes.
- `REFRESH_TOKEN_LIFETIME`: Lifetime of refresh tokens in days.

These environment variables are essential for configuring your Django application and ensuring it operates correctly in various environments.
For Swagger documentation of the API, DEVELOPMENT needs to be set to true.
For all tests inside the backend to run correct, DEVELOPMENT and RUNNING_TESTS needs to be set to true.


# Tools and Libraries Used

## Backend:
- **asgiref==3.7.2**: ASGI server implementation used by Django.
- **certifi==2023.11.17**: Python package for providing Mozilla's CA Bundle.
- **charset-normalizer==3.3.2**: Python package for character set normalization.
- **dj-database-url==0.5.0**: Django package to utilize 12factor inspired DATABASE_URL environment variable.
- **Django==4.2**: High-level Python Web framework that encourages rapid development and clean, pragmatic design.
- **django-cors-headers==4.3.1**: Django package for handling the server headers required for Cross-Origin Resource Sharing (CORS).
- **django-extensions==3.2.3**: Django package providing various extensions for the Django web framework.
- **djangorestframework==3.14.0**: Django package for building Web APIs.
- **djangorestframework-simplejwt==5.3.1**: Django package providing JSON Web Token authentication for Django REST Framework.
- **drf-yasg==1.21.7**: Yet another Swagger generator for Django REST Framework.
- **exceptiongroup==1.2.0**: Django package for grouping Django exception middleware.
- **gunicorn==20.1.0**: Python WSGI HTTP Server for UNIX.
- **idna==3.6**: Internationalized Domain Names in Applications (IDNA) library.
- **inflection==0.5.1**: Python library for string transformation.
- **iniconfig==2.0.0**: Pytest plugin for reading configuration from INI-style files.
- **packaging==23.2**: Core utilities for Python packages.
- **pluggy==1.4.0**: Plugin registration and hook calling mechanisms for Python.
- **psycopg2==2.9.9**: PostgreSQL adapter for Python.
- **PyJWT==2.8.0**: JSON Web Token implementation in Python.
- **pytest==8.0.0**: Testing framework for Python.
- **pytest-django==4.8.0**: Pytest plugin for Django applications.
- **python-decouple==3.8**: Strict separation of settings from code.
- **pytz==2023.3.post1**: World timezone definitions for Python.
- **PyYAML==6.0.1**: YAML parser and emitter for Python.
- **requests==2.31.0**: HTTP library for Python.
- **sqlparse==0.4.4**: Non-validating SQL parser for Python.
- **tomli==2.0.1**: TOML parser for Python.
- **typing_extensions==4.9.0**: Backported and experimental type hints for Python.
- **uritemplate==4.1.1**: URI template library for Python.
- **urllib3==2.1.0**: HTTP client for Python.
- **whitenoise==6.6.0**: Static file serving for Python web apps.

## Frontend:
- **axios**: Promise-based HTTP client for the browser and Node.js.
- **bootstrap**: Front-end framework for developing responsive and mobile-first websites.
- **bootstrap-icons**: Official open-source SVG icon library for Bootstrap.
- **bootstrap-vue-3**: Bootstrap components for Vue 3.
- **core-js**: Modular standard library for JavaScript.
- **pinia**: Intuitive and type-safe store for Vue.js.
- **vue**: Progressive JavaScript framework for building user interfaces.
- **vue-router**: Official router for Vue.js.
- Also github pages

# Credits

This project was made possible thanks to the invaluable resources and documentation provided by the following:

- [Django Documentation](https://docs.djangoproject.com/en/stable/): The official documentation for Django, which served as a fundamental reference for building the backend of this project.
- [Vue.js Documentation](https://v3.vuejs.org/guide/introduction.html): The official documentation for Vue.js, which provided guidance on frontend development and state management.
