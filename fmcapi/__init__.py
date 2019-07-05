"""
The fmcapi __init__.py file is called whenever someone imports the package into their program.
"""

import logging
from .fmc import *

# Its always good to set up a log file.
logging_format = '%(asctime)s - %(levelname)s:%(filename)s:%(lineno)s - %(message)s'
logging_dateformat = '%Y/%m/%d-%H:%M:%S'
# Logging level options are logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL
logging_level = logging.INFO
# logging_level = logging.DEBUG
logging_filename = 'output.log'
logging.basicConfig(format=logging_format,
                    datefmt=logging_dateformat,
                    filename=logging_filename,
                    filemode='w',
                    level=logging_level)

logging.debug("In the fmcapi __init__.py file.")


def __authorship__():
    """In the FMC __authorship__() class method:
***********************************************************************************************************************
This python module was created by Dax Mickelson along with LOTs of help from Ryan Malloy and Neil Patel.
Feel free to send me comments/suggestions/improvements.  Either by email: dmickels@cisco.com or more importantly
via a Pull request from the github repository: https://github.com/daxm/fmcapi.
***********************************************************************************************************************
        """
    logging.debug(__authorship__.__doc__)


__authorship__()
