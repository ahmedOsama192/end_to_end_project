


import os
import logging
from sys import stdout
# Initialize the logger
logging_str = "[%(asctime)s - %(levelname)s - %(module)s - %(message)s]"

log_dir = "src\\ml_project\\logging\\logs"

log_file = os.path.join(log_dir, "running_log.log") 

os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler(stdout)
    ]
    
)

logger = logging.getLogger('ml_project_logger')







