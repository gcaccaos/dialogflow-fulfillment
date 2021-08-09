from os import environ

from google.cloud import dialogflow

PROJECT_ID = environ.get('PROJECT_ID')
SESSION_ID = environ.get('SESSION_ID')

session_client = dialogflow.SessionsClient()

session = session_client.session_path(PROJECT_ID, SESSION_ID)
