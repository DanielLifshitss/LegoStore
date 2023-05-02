from Lego_Searching_Mechanics import Search_Mech_All_Legos,Theme_Search_Mech,Item_Search_By
from Banners import Banner_Printer
from Shipping_storage import All_Shipping_Locations
from Cart import Cart
from Inventory import Avaliable,load_item_database,load_shipping_database
print("starting")

load_item_database()
load_shipping_database()
#MAIN#
while True:
    Banner = Banner_Printer
    Banner.print_enternce_logo()
    Banner.print_menu()
    print("\n")
    print("Enter your choise: ")
    userchoise = Search_Mech_All_Legos.user_choosing_fun_by_int()
    if userchoise == Search_Mech_All_Legos.Manu_Actions.MANU_ACTION_CloseWebsite.value:
         break
    elif userchoise == Search_Mech_All_Legos.Manu_Actions.MANU_ACTION_BrowsThemes.value:
        Theme_Search_Mech.Theme_run()
    elif userchoise == Search_Mech_All_Legos.Manu_Actions.MANU_ACTION_CountryShipping.value:
        All_Shipping_Locations.All_Shipping_Location_run()
    elif userchoise == Search_Mech_All_Legos.Manu_Actions.MANU_ACTION_SpesificItem.value:
        Item_Search_By.item_search_by_run()
    elif userchoise == Search_Mech_All_Legos.Manu_Actions.MANU_ACTION_MyCart.value:
        Cart.cart_run()
    elif userchoise == Search_Mech_All_Legos.Manu_Actions.MANU_ACTION_AvaliableItems.value:
        Avaliable.avaliable_run()
Banner.print_exit_logo()


    
    
    