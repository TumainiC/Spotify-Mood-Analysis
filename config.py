import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access API keys
CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URI")

# Print to check if they are loaded (remove this later for security)
print("Client ID:", CLIENT_ID)
