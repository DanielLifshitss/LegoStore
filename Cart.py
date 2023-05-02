from Banners import Banner_Printer
from enum import Enum
from Lego_Searching_Mechanics import Search_Mech_All_Legos
from Shipping_storage import All_Shipping_Locations


class Cart():
    #MANU Section for searching in Cart#
    class Cart_Menu(Enum):
        ITEMS_IN_CART = 1
        ADD_ITEM_TO_CART = 2
        REMOVE_ITEM_FROM_CART = 3
        SPECIFY_SHIPPING = 4
        TOTAL_VALUE = 5
        CART_MENU_EXIT =6
    
    #MANU Section for adding or removing item by#
    class BY_NAME_OR_NUM(Enum):
        BY_SET_NAME = 1
        BY_SET_NUMBER = 2
    
    MyCart = []
    MyTotal = 0
    MyTotalinVIP = 0
    
    #Funcation that add items to cart by lego set name and adds Lego sets Price in Dollars and VIP Points from our cart to my Totalif its avaliable in stock#
    def add_item_to_cart_by_name(setname):
        for item in Search_Mech_All_Legos.all_sets:
            if item.SetName == str(setname) and item.Avaliable == "yes" or item.Avaliable == "Yes":
                Cart.MyCart.append(item)
                Cart.MyTotal += float(item.PriceDollars)
                Cart.MyTotalinVIP += float(item.PricesVIP)
            
                
                
    #Funcation that add items to cart by lego set number and adds Lego sets Price in Dollars and VIP Points from our cart to my Totalif its avaliable in stock#    
    def add_item_to_cart_by_number(setnum):
        for item in Search_Mech_All_Legos.all_sets:
            if item.SetNumber == str(setnum) and item.Avaliable == "yes" or item.Avaliable == "Yes":
                Cart.MyCart.append(item)
                Cart.MyTotal += float(item.PriceDollars)
                Cart.MyTotalinVIP += float(item.PricesVIP)
            
                
                
    #Funcation that removes items from cart by lego set number and removes Lego sets Price in Dollars and VIP Points from our cart from my Total#
    def remove_item_from_cart_by_number(setnum):
        for item in Cart.MyCart:
            if item.SetNumber == str(setnum):
                Cart.MyCart.remove(item)
                Cart.MyTotal -= float(item.PriceDollars)
                Cart.MyTotalinVIP -= float(item.PricesVIP)

    #Funcation that removes items from cart by lego set name and removes Lego sets Price in Dollars and VIP Points from our cart from my Total#
    def remove_item_from_cart_by_name(setname):
        for item in Cart.MyCart:
            if item.SetName == str(setname):
                Cart.MyCart.remove(item)
                Cart.MyTotal -= float(item.PriceDollars)
                Cart.MyTotalinVIP -= float(item.PricesVIP)

    #Function that show all items that added to Cart#
    def show_items_in_cart():
        for item in Cart.MyCart:
            if Cart.MyCart == []:
                print("Cart is Empty")
            else:
                print(f"Theme:{item.Theme} ,Item Name:{item.SetName}, Set Number: {item.SetNumber},Pieces: {item.Pieces} ,Age:{item.Age} ,Price:{item.PriceDollars}")
    
    


    #Function To Main Packet that containce the flow of searching functions in users cart by his input#
    def cart_run():
        while True:
            Banner_Printer.print_cart_logo()
            print("--------------")
            print("1)See Items in my Cart\n2)Add Item to my Cart\n3)Remove Item from my CartEnter\n4)Specify Shipping\n5)Total Value\n6)Back to Menu\nEnter:")
            userchoise = Search_Mech_All_Legos.user_choosing_fun_by_int()
            #If user chooses to see the Items in his cart#
            if userchoise == Cart.Cart_Menu.ITEMS_IN_CART.value:
                Cart.show_items_in_cart()
            #If user chooses to add Items to his cart#
            elif userchoise == Cart.Cart_Menu.ADD_ITEM_TO_CART.value:
                while True:
                    print("\n")
                    print("1)Add set by name\n2)Add set by number\n3)Back to menu")
                    userchoise = Search_Mech_All_Legos.user_choosing_fun_by_int()
                    if userchoise == Cart.BY_NAME_OR_NUM.BY_SET_NAME.value:
                        print("Enter Set Name:")
                        userchoise = Search_Mech_All_Legos.user_choosing_fun_by_strr()
                        Cart.add_item_to_cart_by_name(setname=userchoise)
                    elif userchoise == Cart.BY_NAME_OR_NUM.BY_SET_NUMBER.value:
                        print("Enter Set Number:")
                        userchoise = Search_Mech_All_Legos.user_choosing_fun_by_int()
                        Cart.add_item_to_cart_by_number(setnum=userchoise)
                    else:
                        break
            #If user chooses to remove Items to his cart#
            elif userchoise == Cart.Cart_Menu.REMOVE_ITEM_FROM_CART.value:
                while True:
                    print("\n")
                    print("1)Remove set by name\n2)Remove set by number\n3)Back to menu")
                    userchoise = Search_Mech_All_Legos.user_choosing_fun_by_int()
                    if userchoise == Cart.BY_NAME_OR_NUM.BY_SET_NAME.value:
                        userchoise = Search_Mech_All_Legos.user_choosing_fun_by_strr()
                        Cart.remove_item_from_cart_by_name(setname=userchoise)
                    elif userchoise == Cart.BY_NAME_OR_NUM.BY_SET_NUMBER.value:
                        userchoise = Search_Mech_All_Legos.user_choosing_fun_by_int()
                        Cart.remove_item_from_cart_by_number(setnum=userchoise)
                    else:
                        break
            #If user chooses to Specify his delivery - each delivery has different price with added to total.#
            elif userchoise == Cart.Cart_Menu.SPECIFY_SHIPPING.value:
                print("Enter Your country:")
                userchoise = Search_Mech_All_Legos.user_choosing_fun_by_strr()
                islocationavaliable =All_Shipping_Locations.search_specific_location(userlocation=userchoise)
                if userchoise == islocationavaliable:
                    print("Enter Delivery Type:\n1)Standart Delivery\n2)Express Delivery\n3)Bricks & Pieces Delivery\n4)Pick Brick Delivery\n5)change delivery\nEnter:")
                    userchoise1 = Search_Mech_All_Legos.user_choosing_fun_by_int()
                    #If user chose a delivery and wants to change it to other delivery options. it removes old delivry price from total and add the new one#
                    if userchoise == All_Shipping_Locations.Delivery_Prices.REMOVEDELIVERY.value:
                        print("Enter Your Last Delivery:")
                        userchoise = Search_Mech_All_Legos.user_choosing_fun_by_int()
                        delivery = All_Shipping_Locations.price_by_delivery_type(userdelivery=userchoise)
                        Cart.MyTotal -= float(delivery)
                        print("Delivery removed, Enter your new delivery type:")
                        userchoise = Search_Mech_All_Legos.user_choosing_fun_by_int()
                        delivery = All_Shipping_Locations.price_by_delivery_type(userdelivery=userchoise)
                        Cart.MyTotal += float(delivery)
                        print(f"Your Total is: {Cart.MyTotal}$ , Or {Cart.MyTotalinVIP} in VIP Points")
                    else:
                        delivery = All_Shipping_Locations.check_country_delivery_avaliable(userchoise1=userchoise , userchoise2=userchoise1)
                        try:
                            Cart.MyTotal += float(delivery)
                        except:
                            print("shipping unavaliable")
                        print(f"Your Total is: {Cart.MyTotal}$ , Or {Cart.MyTotalinVIP} in VIP Points")
                elif userchoise != islocationavaliable:
                    print(f"we are bot shipping to{userchoise}")
            #If user chooses to his total price in Dollars and VIP Points#
            elif userchoise == Cart.Cart_Menu.TOTAL_VALUE.value:
                print(f"Your Total is: {Cart.MyTotal}$ , Or {Cart.MyTotalinVIP} in VIP Points")
            #If user chooses to go back to the main page of the website#
            elif userchoise == Cart.Cart_Menu.CART_MENU_EXIT.value:
                break

    