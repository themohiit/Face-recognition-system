cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    "databaseURL":"https://face-recognition-system-b41c1-default-rtdb.firebaseio.com/"
})