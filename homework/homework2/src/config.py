import os
from dotenv import load_dotenv

def load():
    load_dotenv()

def get(key: str, default=None) -> str:
    return os.getenv(key, default)

