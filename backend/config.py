import os
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

INFERMEDICA_APP_ID = os.getenv('INFERMEDICA_APP_ID')
INFERMEDICA_API_KEY = os.getenv('INFERMEDICA_API_KEY')

