import datetime
import sys
import logging


def get_current_date():
    """
    :return: DateTime object
    """
    return datetime.datetime


def get_current_platform():
    """
    :return: current platform
    """
    return sys.platform


def loggingTest ():
    checkValue = ("value")
    try:
       checkValue = int(checkValue)
       logging.info("information.message")
    except:
    	logging.error("Something go wrong")

loggingTest()