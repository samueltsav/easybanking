#import hashlib
import uuid


users = {}
sessions = {}

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.id = str(uuid.uuid4())
       
    def create_user(username, password):
        if username in users:
            return "Username already exists."
        user = User(username, password)
        users[username] = user
        return "User created successfully."
    
    def login(username, password):
        user = users.get(username)
        if user and user.password == password:
            session_id = str(uuid.uuid4())
            sessions[session_id] = username
            return session_id
        return None

    def logout(session_id):
        return sessions.pop(session_id, None) is not None
        print(f'You are logged out.')


