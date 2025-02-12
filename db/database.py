from pymongo import MongoClient
import bcrypt

class Database:
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client['image_converter_db']
        self.users = self.db['users']

    def register_user(self, username,email, password):
        if self.users.find_one({"username": username}):
            return False, "Username already exists"
        
        if self.users.find_one({"email": email}):
            return False, "Email already exists"
        
        hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        self.users.insert_one({
            "username": username,
            "password": hashed_pw,
            "email": email
        })
        return True, "User registered successfully"

    def validate_login(self, email, password):
        user = self.users.find_one({"email": email})
        if user and bcrypt.checkpw(password.encode('utf-8'), user['password']):
            return True, user
        return False, "Invalid credentials"
