from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build
from rest_framework.views import APIView
from rest_framework.response import Response
from google.auth.transport import requests

CLIENT_SECRET_FILE = r'#'
SCOPES = ['https://www.googleapis.com/auth/calendar']
REDIRECT_URI = 'http://localhost:8000/rest/v1/calendar/redirect/'
CLIENT_ID = '#'

class GoogleCalendarInitView(APIView):
    def get(self, request):
        flow = Flow.from_client_secrets_file(
            CLIENT_SECRET_FILE,
            scopes=SCOPES,
            redirect_uri=REDIRECT_URI
        )
        auth_url, _ = flow.authorization_url(prompt='consent')

        return Response({'auth_url': auth_url})

class GoogleCalendarRedirectView(APIView):
    def get(self, request):
        code = request.query_params.get('code')
        print(code)
        flow = Flow.from_client_secrets_file(
            CLIENT_SECRET_FILE,
            scopes=SCOPES,
            redirect_uri=REDIRECT_URI
        )
        flow.fetch_token(code=code)

        credentials = flow.credentials
        token = credentials.id_token
        print(credentials, token)

        id_info = id_token.verify_oauth2_token(
            token, requests.Request(), CLIENT_ID
        )
        user_id = id_info['sub']

        service = build('calendar', 'v3', credentials=credentials)
        events_result = service.events().list(calendarId='primary', maxResults=10).execute()
        events = events_result.get('items', [])

        return Response({'events': events})