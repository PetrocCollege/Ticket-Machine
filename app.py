""" 
The mainstream for the entire program, this will use all the code from "modules/"
"""

from modules import (
    interface,
    time_handler,
    pricing
)




def AskForHours():
    while True:
        try: amount_of_hours = float(input(     "Amount Of Hours: ")); return amount_of_hours
        except: print("Not a valid number, re-type."); return None


def PaymentMethod():
    ...
    

def BuyTicket():
    interface.PrintMain()
    CorrectValueType = False
    licence_number = input(     "Car Licence Plate Number: ")
    while True:
        hours = AskForHours()
        if hours != None: break
    
    try: hours, hourly_rate = pricing.GetHourlyRate(hours)
    except: BuyTicket()
    total_price = f"£{round(hours * hourly_rate, 2)}"
    while True:
        if input(f"\n[CONFIRMATION] This ticket will cost {total_price}, type 'yes' if you want to buy: ").lower().strip() == "yes":
            print("payment ")
            break
        else:
            BuyTicket()
    
    


def Main():
    interface.PrintMain()
    input("     Press enter to buy a ticket... ")
    interface.TriggerLoading()
    BuyTicket()
    
     



if __name__ == "__main__":
    Main()
