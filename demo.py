from visa.logger import logging
from visa.exception import USvisaException
import sys
#logging.info("This is an info message from demo.py")

try:
    a = 1/0
except Exception as e:
    raise USvisaException(e,sys)
