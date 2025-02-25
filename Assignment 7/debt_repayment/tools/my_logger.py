import logging
import os

#Create a Log Folder
log_folder = "debt_repayment/files/logs/"
os.makedirs(log_folder, exist_ok=True)
log_file = os.path.join(log_folder, "getting_out_of_debt.log")

#Configure Log Files
logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(name)s - Line %(lineno)d: %(message)s"
)
logger = logging.getLogger(__name__)

#Create Log Infor Message
def log_info(message):
    logger.info(message)

#Create Log Debug Message
def log_debug(message):
    logger.debug(message)
