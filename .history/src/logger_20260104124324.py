import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m-%Y-%d_%H-%M-%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG-FILE)
os.makedirs(logs_path,exist_ok=True)

