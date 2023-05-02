from Banners import Banner_Printer
from enum import Enum
from Lego_Searching_Mechanics import Search_Mech_All_Legos

#All shipping locations#
class All_Shipping_Locations():
    #ALL shippinh Menu actions#
    class All_Shipping_Menu(Enum):
        SHIPPING_MANU_ACTIONS_SEARCH_LOCATION = 1
        SHIPPING_MANU_ACTIONS_BACK = 2
    
    #ALL shipping prices Menu actions#
    class Delivery_Prices(Enum):
        StandardDelivery_PRICE = 1
        ExpressDelivery_PRICE = 2
        BricksPiecesDelivery_PRICE = 3
        PickBrickDelivery_PRICE = 4
        REMOVEDELIVERY = 5
        
    all_shipping_countries = []
    
    def __init__(self, location):
        self.location = location
    
    #Functions that prints all shipping locations#
    def print_all_shipping_locations():
        for location in All_Shipping_Locations.all_shipping_countries:
            print(f"{location.Location}, Types of delivery:\nStandard Delivery: {location.StandardDelivery}\nExpress Delivery: {location.StandardDelivery}\nBricks & Pieces Delivery: {location.StandardDelivery}\nPick a Brick Delivery: {location.StandardDelivery}\n--------------")
    
    #Functions that prints  shipping location by users input#
    def search_specific_location(userlocation):
        for location in All_Shipping_Locations.all_shipping_countries:
            if location.Location == userlocation:
                print(f"{location.Location}, Types of delivery:\nStandard Delivery: {location.StandardDelivery}\nExpress Delivery: {location.StandardDelivery}\nBricks & Pieces Delivery: {location.StandardDelivery}\nPick a Brick Delivery: {location.StandardDelivery}\n--------------")
                return str(location.Location)
    
    #Functions that prints shipping price by delivry type and ands it in cart to total#
    def price_by_delivery_type(userdelivery):
            if All_Shipping_Locations.Delivery_Prices.StandardDelivery_PRICE.value == userdelivery:
                print("price of Standart Selivery is 10$")
                return 10
            elif All_Shipping_Locations.Delivery_Prices.ExpressDelivery_PRICE.value == userdelivery:
                print("price of Express Delivery is 20$")
                return 20
            elif All_Shipping_Locations.Delivery_Prices.BricksPiecesDelivery_PRICE.value == userdelivery:
                print("price of Brick and Pieces delivery is 7.5$")
                return 7.5
            elif All_Shipping_Locations.Delivery_Prices.PickBrickDelivery_PRICE.value == userdelivery:
                print("price of Pick a Brick Delivery delivery is 7.5$")
                return 7.5
            
    def check_country_delivery_avaliable(userchoise1, userchoise2):
        for location in All_Shipping_Locations.all_shipping_countries:
            if location.Location == userchoise1:
                if location.StandardDelivery != "unavailable" and userchoise2 == All_Shipping_Locations.Delivery_Prices.StandardDelivery_PRICE.value:
                    print("price of Standart Selivery is 10$")
                    return 10
                elif location.ExpressDelivery != "unavailable" and userchoise2 == All_Shipping_Locations.Delivery_Prices.ExpressDelivery_PRICE.value:
                    print("price of Standart Selivery is 20$")
                    return 10
                elif location.BricksPiecesDelivery != "unavailable" and userchoise2 == All_Shipping_Locations.Delivery_Prices.BricksPiecesDelivery_PRICE.value:
                    print("price of Standart Selivery is 7.5$")
                    return 10
                elif location.PickBrickDelivery != "unavailable" and userchoise2 == All_Shipping_Locations.Delivery_Prices.PickBrickDelivery_PRICE.value:
                    print("price of Standart Selivery is 7.5$")
                    return 10
                    
                    
                    
    #Function To Main Packet that containce the flow of searching functions in users shipping locations by his input#                   
    def All_Shipping_Location_run():
        while True:
            Banner_Printer.print_shipping_logo()
            print("--------------")
            All_Shipping_Locations.print_all_shipping_locations()
            print("1)Search Specific Country\n2)Back To Menu\nEnter :")
            userchoise = Search_Mech_All_Legos.user_choosing_fun_by_int()
            if userchoise == All_Shipping_Locations.All_Shipping_Menu.SHIPPING_MANU_ACTIONS_SEARCH_LOCATION.value:
                while True:
                    print("Enter Country Name:")
                    user_country_choise = Search_Mech_All_Legos.user_choosing_fun_by_strr()
                    All_Shipping_Locations.search_specific_location(userlocation=user_country_choise)
                    print("1)Search Specific Country\n2)Back To Menu\nEnter :")
                    userchoise = Search_Mech_All_Legos.user_choosing_fun_by_int()
                    if userchoise == All_Shipping_Locations.All_Shipping_Menu.SHIPPING_MANU_ACTIONS_BACK.value:
                        break
            else:
                break
                               