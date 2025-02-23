import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,  # Default level
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("app.log"),  # Log to file
        logging.StreamHandler()  # Log to console
    ]
)

# Get logger instance
logger = logging.getLogger("mycli")