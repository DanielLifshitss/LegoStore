from Lego_Searching_Mechanics import Search_Mech_All_Legos
from Shipping_storage import All_Shipping_Locations
from Banners import Banner_Printer
from enum import Enum

class Items():

    def __init__(self, ID, Theme , SetName ,SetNumber ,Pieces ,Age ,PriceDollars ,PricesVIP,Itemsinstock,Avaliable):
        self.ID = ID
        self.Theme = Theme
        self.SetName = SetName
        self.SetNumber = SetNumber
        self.Pieces = Pieces
        self.Age = Age
        self.PriceDollars = PriceDollars
        self.PricesVIP = PricesVIP
        self.Itemsinstock = Itemsinstock
        self.Avaliable = Avaliable
    
class Shipping_Location():
    def __init__(self ,Location ,StandardDelivery,ExpressDelivery,BricksPiecesDelivery,PickBrickDelivery ):
        self.Location  =Location
        self.StandardDelivery  =StandardDelivery
        self.ExpressDelivery  =ExpressDelivery
        self.BricksPiecesDelivery  =BricksPiecesDelivery
        self.PickBrickDelivery  =PickBrickDelivery


class Avaliable(Search_Mech_All_Legos):
    #MANU Section for searching in Avaliable items#
    class Avaliable_Manu_Actions(Enum):
        AVALIABLE_MANU_ACTIONS_AVALIABLE_ITEMS = 1
        AVALIABLE_MANU_ACTIONS_AVALIABLE_NOT_ITEMS = 2
        AVALIABLE_MANU_ACTIONS_BACK = 3

    #Function that Checks if Item is avaliable in stock#
    def items_avaliable_in_stock():
        for item in Search_Mech_All_Legos.all_sets:
            if item.Avaliable == "yes" or item.Avaliable == "Yes":
                print(f"Item Name:{item.SetName} ,Set Number: {item.SetNumber},Pieces: {item.Pieces} ,Age:{item.Age} ,Price:{item.PriceDollars}")

    #Function that Checks if Item is not avaliable in stock#            
    def items_not_avaliable_in_stock():
        for item in Search_Mech_All_Legos.all_sets:
            if item.Avaliable == "no" or item.Avaliable == "No":
                print(f"Item Name:{item.SetName} ,Set Number: {item.SetNumber},Pieces: {item.Pieces} ,Age:{item.Age} ,Price:{item.PriceDollars}")
    
    # Function To Main Packet that containce the flow of searching functions in users avaliable items by his input
    def avaliable_run():
        while True:
            Banner_Printer.print_avaliable_logo()
            print("--------------")
            print("Press To see:\n1)Avaliable Items\n2)Not Avaliable Items\n3)Back to Menu\nEnter :")
            userchoise = Search_Mech_All_Legos.user_choosing_fun_by_int()
            if userchoise == Avaliable.Avaliable_Manu_Actions.AVALIABLE_MANU_ACTIONS_AVALIABLE_ITEMS.value:
                Avaliable.items_avaliable_in_stock()
            elif userchoise == userchoise == Avaliable.Avaliable_Manu_Actions.AVALIABLE_MANU_ACTIONS_AVALIABLE_NOT_ITEMS.value:
                Avaliable.items_not_avaliable_in_stock()
            elif userchoise ==Avaliable.Avaliable_Manu_Actions.AVALIABLE_MANU_ACTIONS_BACK.value:
                break

#function that loads all sets CSV data and for each set creating an Item OOB#
def load_item_database():
    ListOfItems = []
    with open("LegoItems.csv" , "r") as F:
        for item in F:
            ListOfItems.append(item.strip("\n").split(","))

    for item in ListOfItems:
        item = Items(ID=item[0],
                    Theme=item[1],
                    SetName=item[2] ,
                    SetNumber=item[3] ,
                    Pieces=item[4] ,
                    Age=item[5] ,
                    PriceDollars=item[6] ,
                    PricesVIP=item[7],
                    Itemsinstock=item[8],
                    Avaliable=item[9])
        Search_Mech_All_Legos.all_sets.append(item)

#function that loads all shipping locations CSV data and for each set creating an location OOB#
def load_shipping_database():
    ListOfCountryInfo = []
    with open("Shipping.csv" , "r") as F:
        for country in F:
            ListOfCountryInfo.append(country.strip("\n").split(","))

    for location in ListOfCountryInfo:
        location = Shipping_Location(Location=location[0] ,
                                    StandardDelivery=location[1],
                                    ExpressDelivery=location[2],
                                    BricksPiecesDelivery=location[3],
                                    PickBrickDelivery=location[4])
        All_Shipping_Locations.all_shipping_countries.append(location)
     