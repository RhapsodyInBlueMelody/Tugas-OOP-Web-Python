from flask import Flask
import logging

# Create Flask app
app = Flask(__name__)

# Set secret key for sessions and flash messages
app.secret_key = 'Fazser'

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),  # Prints to console
        logging.FileHandler('app.log')  # Writes to a file
    ]
)

# Import routes after app is created to avoid circular imports
from app import routes
