import datetime
import sys


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

def parity(value):
    if (value == "True"):
     for number in range(100):
        if number % 2 == 0:
            print(number)
    else:
        if (value == "False"):
         for number in range(100):
            if number % 2 == 1:
                print(number)
parity("True")
parity("False")

