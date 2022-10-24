from dotenv import load_dotenv
from pathlib import Path
import os
load_dotenv()
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)
SECRET_KEY = os.getenv("SECRET_KEY")
DOMAIN = os.getenv("DOMAIN")
EMAIL = os.getenv("EMAIL")
PORT = os.getenv("PORT")
RECIVERS = os.getenv("RECIVERS")
PASSWORD = os.getenv("PASSWORD")