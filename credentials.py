import creds
from firebase_admin import credentials
firebase_cred_file = credentials.Certificate('API/serviceAccountKey.json')


#print(firebase_cred_file)