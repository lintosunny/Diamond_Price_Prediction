# it logs every information of every events

import logging
import os
from datetime import datetime

datetime.now()

Log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

log_path = os.path.join(os.getcwd(), "logs")

os.mkdirs(log_path, exist_ok=True)

LOG_FILEPATH = os.path.join(log_path, Log_file)

logging.basicConfig(level=logging.INFO,
                    filename=LOG_FILEPATH,
                    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"

)
