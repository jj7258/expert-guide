from google import Create_Service

CLIENT_SECRET_FILE='Slideshow_Google_Drive.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service=Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)

print(dir(service))\

"""   def __init__(self):
       # Initialize the Google Drive API client
       creds = None
       # The file token.json stores the user's access and refresh tokens, and is
       # created automatically when the authorization flow completes for the first
       # time.
       if os.path.exists('token.json'):
           creds = Credentials.from_authorized_user_file('token.json', SCOPES)
       # If there are no (valid) credentials available, let the user log in.
       if not creds or not creds.valid:
           if creds and creds.expired and creds.refresh_token:
               creds.refresh(Request())
           else:
               flow = InstalledAppFlow.from_client_secrets_file(
                   'Credentials.json', SCOPES)
               creds = flow.run_local_server(port=0)
           # Save the credentials for the next run

       drive_service = googleapiclient.discovery.build('drive', 'v3', credentials=creds)

       self.slide_images = []  # List to store image URLs
       self.current_image_index = 0"""