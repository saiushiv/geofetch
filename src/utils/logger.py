import logging

"""
This module configures the logging for the GeoFetch CLI application.

The logging configuration includes:
- Logging level set to INFO, which means all messages at this level and above (e.g., WARNING, ERROR, CRITICAL) will be logged.
- Log messages formatted to include the timestamp, log level, and message.
- Handlers to log messages to both a file named 'app.log' and the console (standard output).

Attributes:
    logger (logging.Logger): The logger instance for the GeoFetch CLI application.
"""

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
logger = logging.getLogger("geofetchcli")