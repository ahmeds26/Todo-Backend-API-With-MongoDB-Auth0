from passlib.context import CryptContext



def encrypt_password(input_password: str) -> str:
    password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    return password_context.hash(input_password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    return password_context.verify(plain_password, hashed_password)


