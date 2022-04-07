""" 
Car Park Machine - Console interface for the application
"""

import sys
import os
import time
from . import time_handler


# The reason we use raw string literal here is because we need to escape the backslash in the ascii text.
TicketText = r"""
  _____ _      _        _     __  __            _     _            
 |_   _(_) ___| | _____| |_  |  \/  | __ _  ___| |__ (_)_ __   ___ 
   | | | |/ __| |/ / _ \ __| | |\/| |/ _` |/ __| '_ \| | '_ \ / _ \
   | | | | (__|   <  __/ |_  | |  | | (_| | (__| | | | | | | |  __/
   |_| |_|\___|_|\_\___|\__| |_|  |_|\__,_|\___|_| |_|_|_| |_|\___|
"""

PricesChart = """ 
              +========+======================+
              | Hours  | Rate of pay per hour |
              +========+======================+
              | 1-4    | £1.85                |
              +--------+----------------------+
              | 5-7    | £1.50                |
              +--------+----------------------+
              | 8-11   | £1.40                |
              +--------+----------------------+
              | 12-24  | £1.30                |
              +--------+----------------------+


"""



def ClearConsole():
    """ 
    Clears entire console
    """
    if os.name != 'nt':
        os.system('clear')
    else:
        os.system('cls')



def PrintMain():
    """
    Prints main interface of the ticket machine, ascii text, current time, current date and prices
    """
    ClearConsole()
    print(TicketText)
    print(f"                    Current Time: {time_handler.GetCurrentTime()}")
    print(f"                        Date: {time_handler.GetCurrentDate()}")
    print(PricesChart)


def PaymentMethod():
    ClearConsole()



def TriggerLoading():
    ClearConsole()
    for i in range(100+1):
        time.sleep(0.015)
        sys.stdout.write(('='*i)+(''*(100-i))+("\r [ %d"%i+"% ] "))
        sys.stdout.flush()
    time.sleep(0.7)
    ClearConsole()





