""" 
Car Park Machine - Time Handler Module 
"""


from datetime import datetime, timedelta


def GetCurrentTime():
    """ 
    Returns current time with the format of hours, mins and seconds 
    """
    return datetime.now().strftime("%H:%M:%S")


def GetCurrentDate():
    """ 
    Returns current date with the format of day/month/year
    """
    return datetime.today().strftime("%d/%m/%y")



def AddHours(hours:int):
    """
    Adds hours (arg 1) to current time
    """
    return (datetime.now() + timedelta(hours=hours)).strftime('%H:%M:%S')









