# Google Calendar Integration with Django REST API

![License](https://img.shields.io/badge/license-MIT-blue.svg)

## Description

This project implements Google Calendar integration using Django REST API. It utilizes the OAuth2 mechanism to obtain users' calendar access. The API provides two endpoints:

- `/rest/v1/calendar/init/` (GET) - This endpoint starts step 1 of the OAuth flow. It prompts the user for their credentials and initiates the authentication process.

- `/rest/v1/calendar/redirect/` (GET) - This endpoint handles the redirect request sent by Google with the authorization code. It performs two tasks:
  1. Retrieves the access token from the provided authorization code using the OAuth2 mechanism.
  2. Retrieves a list of events from the user's calendar using the obtained access token.

## Installation and Setup

1. Clone the repository:
   - git clone https://github.com/your-username/google-calendar-django-rest-api.git
  
2. Create and activate a virtual environment:
  - cd google-calendar-django-rest-api
  - python3 -m venv venv
  - source venv/bin/activate

3. Install the dependencies:
   - pip install -r requirements.txt

4. Set up Google API credentials:
  - Go to the Google Cloud Platform Console (https://console.cloud.google.com/).
  - Create a new project or select an existing project.
  - Enable the Google Calendar API for your project.
  - Create OAuth 2.0 credentials.
  - Download the credentials JSON file and save it as client_secret.json in the project root directory.

5. Apply database migrations:
  - python manage.py migrate

6. Start the development server:
  - python manage.py runserver

7. Open your browser and go to http://localhost:8000 to access the API.

## Usuage

- To initiate the OAuth flow, send a GET request to /rest/v1/calendar/init/. This will prompt the user to enter their credentials.

- After entering the credentials, the user will be redirected to the Google sign-in page for authentication.

- Once authenticated, the user will be redirected back to /rest/v1/calendar/redirect/. This view will handle the redirect request and retrieve the access token from Google.

- After obtaining the access token, the view will fetch a list of events from the user's calendar using the obtained access token.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please follow these steps:

- Fork the repository.
- Create a new branch for your feature or bug fix.
- Implement your changes.
- Commit and push your changes to your forked repository.
- Submit a pull request explaining your changes.

## License
This project is licensed under the MIT License. See the LICENSE file for details

