import logging
import os

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/processing.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

logger = logging.getLogger(__name__)


def log_process(message):
    logger.info(message)