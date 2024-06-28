# log.py
import logging
import os

# Get the current directory of the script
current_directory = os.path.dirname(os.path.abspath(__file__))

# Define the log file path
log_file_path = os.path.join(current_directory, 'app.log')

# Set up logging configuration
logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Create a logger object
logger = logging.getLogger(__name__)
