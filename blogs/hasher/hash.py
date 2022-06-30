from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_passwor(password):
    return pwd_context.hash(password)

def verify_passwor(plain_password, hashed_password) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
    