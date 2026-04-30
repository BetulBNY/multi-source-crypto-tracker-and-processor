import time
import logging
from functools import wraps

# Logging Setup / rules / format setup
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s' # name part is logger name (DataPipeline in this case) -- message part is the actual log message we send when we call logger.info(...)
)
logger = logging.getLogger("DataPipeline")

def monitor_execution(func):
    """
    A decorator that measures and logs how long a function takes to run.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Process Started: {func.__name__}")
        start_time = time.time()
        try:
            result = func(*args, **kwargs)
            end_time = time.time()
            logger.info(f"Process Completed Successfully: {func.__name__} (Duration: {end_time - start_time:.2f} sn)")
            return result
        except Exception as e:
            logger.error(f"Error {func.__name__}: {str(e)}")
            raise e
    return wrapper
# INFO: logger.info(...) --> stores this information in logs (we are writing log message and sending it to logging system at INFO level)
# logger.info("message") -> logging system receives message -> puts it into %(message)s -> formats full log using basicConfig -> prints / stores log