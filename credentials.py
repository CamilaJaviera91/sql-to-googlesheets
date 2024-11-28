from google.oauth2.service_account import Credentials

def credentials():

    FOLDER = './/'

    #Authentication

    SERVICE_ACCOUNT_FILE = FOLDER + 'credentials.json'

    SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 
            'https://spreadsheets.google.com/feeds', 
            'https://www.googleapis.com/auth/drive.file',
            'https://www.googleapis.com/auth/drive']

    # Load credentials from the JSON file
    creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    return creds