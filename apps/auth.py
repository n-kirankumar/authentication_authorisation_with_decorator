# auth.py
from constants import users
from log import logger

current_user = None

def authenticate(username, password):
    """
    Authenticates a user.
    """
    global current_user
    for user in users:
        if user['username'] == username and user['password'] == password:
            current_user = user
            logger.info(f"User {username} authenticated successfully")
            return True
    logger.error(f"Authentication failed for user {username}")
    return False

def add_user(username, password, role):
    """
    Adds a new user.
    """
    for user in users:
        if user['username'] == username:
            logger.error(f"User {username} already exists")
            return False
    users.append({"username": username, "password": password, "role": role})
    logger.info(f"User {username} added successfully")
    return True

def get_current_user():
    """
    Returns the currently authenticated user.
    """
    return current_user

def authorize(role):
    """
    Decorator to restrict access to functions based on user roles.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            if current_user and current_user['role'] == role:
                return func(*args, **kwargs)
            else:
                logger.error(f"Unauthorized access attempt by {current_user['username'] if current_user else 'None'}")
                return False
        return wrapper
    return decorator

def authenticate_required(func):
    """
    Decorator to ensure a user is authenticated before accessing a function.
    """
    def wrapper(*args, **kwargs):
        if current_user:
            return func(*args, **kwargs)
        else:
            logger.error("Authentication required")
            return False
    return wrapper
