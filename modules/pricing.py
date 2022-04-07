""" 
Car Park Machine - Pricing module
"""




def GetHourlyRate(hours:int):
    if hours <= 4: return hours, 1.85
    elif hours <= 7: return hours, 1.50
    elif hours <= 11: return hours, 1.40
    elif hours <= 24: return hours, 1.30
    else: None
