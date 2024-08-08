import firebase_admin
from firebase_admin import credentials, firestore, initialize_app
#from google.cloud import firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin = initialize_app(cred)

db = firestore.client()

data = {
    'taskId': 5123,
    'taskName': 'Verificar que el proceso del CIGRED esté melo',
    'type': 'Task Force',
    'organism' : 'DAGMA',
    'description' : 'Debe ser realizada de manera prioritaria',
    'status': False,
    'state': 45.66,
    'assignedTo': 'Juan Pablo Guzmán Martínez',
    'stablishedDate': '25/05/2024',
    'doneDate': '07/08/2024',
    'commitments': 'Informar a Jocelyn cuando se cumpliera',
    'lastReport': '',
    'alert': True,
    'priority': 'High'
}

doc_ref = db.collection('tasksCollection').document()
doc_ref.set(data)


doc_ref = db.collection("tasksCollection")
docs = doc_ref.stream()

for doc in docs:
    print(f"{doc.id} => {doc.to_dict()}")