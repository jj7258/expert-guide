import os
import io
import pickle
import os.path
import time
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from PyQt5.QtCore import QObject, pyqtSignal

# Define the folder ID or path in Google Drive where the images are located
FOLDER_ID = '1Dm38CmR9s_9banF60aWoEVdFBEtW_ZO4'  # Replace with the actual folder ID or path

# Define the local folder where you want to save the images (use an absolute path)
LOCAL_FOLDER_PATH = 'C:/Users/joelj/OneDrive/Documents/Programming/PycharmProjects/UWR_Internship/Google Drive Images/Slideshow'

# Google Drive API scope required for accessing files
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

def get_authenticated_service():
    credentials = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            credentials = pickle.load(token)

    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            credentials = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(credentials, token)

    service = build('drive', 'v3', credentials=credentials)
    return service

class GoogleDriveWorker(QObject):
    new_image_downloaded = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)

    def download_file(self, service, file_id, local_folder_path, file_name):
        request = service.files().get_media(fileId=file_id)
        fh = io.FileIO(os.path.join(local_folder_path, file_name), 'wb')
        downloader = MediaIoBaseDownload(fh, request)

        done = False
        while not done:
            status, done = downloader.next_chunk()

        # Notify the GUI that a new image has been downloaded
        self.new_image_downloaded.emit()

    def download_new_files(self, service, local_folder_path, known_files):
        results = service.files().list(q=f"'{FOLDER_ID}' in parents and trashed=false", fields="files(id, name)").execute()
        files = results.get('files', [])
        new_files = [file for file in files if file['name'] not in known_files]

        for file in new_files:
            file_id = file['id']
            file_name = file['name']
            local_file_path = os.path.join(local_folder_path, file_name)
            print(f"Downloading new file: {file_name}")
            self.download_file(service, file_id, local_folder_path, file_name)

        return [file['name'] for file in files]

    def start_sync(self):
        # Move the Google Drive synchronization functionality here
        if not os.path.exists(LOCAL_FOLDER_PATH):
            os.makedirs(LOCAL_FOLDER_PATH)

        service = get_authenticated_service()

        local_files = [f for f in os.listdir(LOCAL_FOLDER_PATH) if os.path.isfile(os.path.join(LOCAL_FOLDER_PATH, f))]

        known_files = self.download_new_files(service, LOCAL_FOLDER_PATH, local_files)

        while True:
            time.sleep(60)  # Check for changes every 60 seconds

            known_files = self.download_new_files(service, LOCAL_FOLDER_PATH, known_files)

            # Notify the GUI that a new image has been downloaded
            self.new_image_downloaded.emit()