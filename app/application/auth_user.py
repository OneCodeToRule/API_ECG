from datetime import datetime, timedelta

import jwt
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext


JWT_SECRET = "mysecretkey"  # Debería ser una clave segura en un entorno real
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

fake_users_db = {
    "user1": {
        "username": "user1",
        "hashed_password": "$2b$12$sYWD7sCRzCzntKot.0CT4e6Zvl2m/TJUpxA8tu1VaybCJDZwjFZ36", # Contraseña: password1
        "disabled": False,
        "role": "USER"
    },
    "admin": {
        "username": "admin",
        "hashed_password": "$2b$12$v75.RTtYqKJYRnYaDYm1tuLXoUDlMAWn2xdS2ayQPj5J7trD5EKn6", # Contraseña: adminpassword
        "disabled": False,
        "role": "ADMIN"
    }
}


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_user(username: str):
    if username in fake_users_db:
        user_dict = fake_users_db[username]
        return user_dict


def authenticate_user(username: str, password: str):
    user = get_user(username)
    if not user:
        return False
    if not verify_password(password, user["hashed_password"]):
        return False
    
    return user


def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET, algorithm=ALGORITHM)

    return encoded_jwt


# def decode_token(token: str):
#     try:
#         payload = jwt.decode(token, JWT_SECRET, algorithms=[ALGORITHM])
#         username = payload.get("sub")
#         if username is None:
#             raise HTTPException(
#                 status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
#         return username
#     except jwt.ExpiredSignatureError:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expired")
#     except jwt.JWTError:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
