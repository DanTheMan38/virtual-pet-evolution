import logging

# Configure the logger
logging.basicConfig(
    filename="db_operations.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Create a logger instance
logger = logging.getLogger("db_operations")

# Define helper functions
def log_info(message):
    logger.info(message)

def log_error(message):
    logger.error(message)