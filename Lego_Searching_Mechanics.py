from enum import Enum
from Banners import Banner_Printer

#All Legos Searching Mechanict by Sections and By diffirents Parameters#
class Search_Mech_All_Legos():
    #Main Menu Actions#
    class Manu_Actions(Enum):
        MANU_ACTION_BrowsThemes = 1
        MANU_ACTION_CountryShipping = 2
        MANU_ACTION_SpesificItem = 3
        MANU_ACTION_AvaliableItems = 4
        MANU_ACTION_MyCart = 5
        MANU_ACTION_CloseWebsite = 6
    
    all_sets = []
    
    def __init__(self, item):
        self.item = item
        
    
    #User input function (by int type)#
    @staticmethod
    def user_choosing_fun_by_int():
        try:
            userchoise = int(input())
            if type(userchoise) is int:
                return userchoise
            else:
                pass
        except ValueError as Valuex:
            print(f"Invalid search, {Valuex}")
    
    #User input function (by str type)#
    @staticmethod
    def user_choosing_fun_by_strr():
        try:
            userchoise = str(input())
            if type(userchoise) is str:
                return userchoise
            else:
                pass
        except ValueError as Valuex:
            print(f"Invalid search, {Valuex}")
    
#Theme Searching Mech#
class Theme_Search_Mech(Search_Mech_All_Legos):
    #Theme Manu Actions#
    class Theme_Manu_Actions(Enum):
        THEME_MANU_ACTIONS_BACK = 1
        THEME_MANU_ACTIONS_SEARCH = 2
    
    #Function thats show all lego Themes#
    def show_all_lego_themes():
        themeset = set()
        for item in Search_Mech_All_Legos.all_sets:
            themeset.add(item.Theme)
            
        for theme in themeset:
            print(theme)
      
    #Function thats show all sets by user Theme choose#      
    def show_sets_by_theme(usertheme):
        for item in Search_Mech_All_Legos.all_sets:
            if item.Theme == usertheme:
                print(f"Item Name:{item.SetName} ,Set Number: {item.SetNumber},Pieces: {item.Pieces} ,Age:{item.Age} ,Price:{item.PriceDollars}")
    
    #Function To Main Packet that containce the flow of searching functions in Theme section by his input#  
    def Theme_run():
        while True:
            Banner_Printer.print_theme_logo()
            print("--------------")
            Theme_Search_Mech.show_all_lego_themes()
            print("1) Back to Menu\n2)Enter your Theme to see their Sets\nEnter:")
            userchoise = Search_Mech_All_Legos.user_choosing_fun_by_int()
            if userchoise== Theme_Search_Mech.Theme_Manu_Actions.THEME_MANU_ACTIONS_BACK.value:
                break
            elif userchoise== Theme_Search_Mech.Theme_Manu_Actions.THEME_MANU_ACTIONS_SEARCH.value:
                print("Enter Theme Name: ")
                theme_user_choise = Search_Mech_All_Legos.user_choosing_fun_by_strr()
                Theme_Search_Mech.show_sets_by_theme(usertheme=theme_user_choise)
                while True:
                    print("would you like to see other Theme?\n1)No (Back to Menu)\n2)Yes\nEnter: ")
                    theme_user_choise = Search_Mech_All_Legos.user_choosing_fun_by_int()
                    if theme_user_choise == Theme_Search_Mech.Theme_Manu_Actions.THEME_MANU_ACTIONS_BACK.value:
                        break
                    else:
                        print("Enter Theme Name: ")
                        theme_user_choise = Search_Mech_All_Legos.user_choosing_fun_by_strr()
                        Theme_Search_Mech.show_sets_by_theme(usertheme=theme_user_choise)


class Item_Search_By(Search_Mech_All_Legos):
    #Item Serch by different Parameters Menu Actions#
    class Specific_Item_Manu_Actions(Enum):
        SPECIFIC_SERACH_BY_NUM = 1
        SPECIFIC_SERACH_BY_AGE = 2
        SPECIFIC_SERACH_BY_PRICES = 3
        SPECIFIC_SERACH_BY_PIECES = 4
        SPECIFIC_SERACH_BY_EXIT = 5
    
        
    #Function To Main Packet that containce the flow of searching functions in Item Search By section by his input#
    def item_search_by_run():
        Banner_Printer.print_search_logo()
        print("--------------")
        print("\n")
        while True:
            print("Searching By?\n1)Set Number\n2)Age\n3)Prices\n4)Pieces\n5)Back To Menu\nEnter: ")
            userchoise = Search_Mech_All_Legos.user_choosing_fun_by_int()
            if userchoise == Item_Search_By.Specific_Item_Manu_Actions.SPECIFIC_SERACH_BY_NUM.value:
                Item_Search_By_Set_Number.search_set_by_num_run()
            elif userchoise == Item_Search_By.Specific_Item_Manu_Actions.SPECIFIC_SERACH_BY_AGE.value:
                Item_Search_By_Set_Age.search_set_by_age_run()   
            elif userchoise == Item_Search_By.Specific_Item_Manu_Actions.SPECIFIC_SERACH_BY_PRICES.value:
                Item_Search_By_Set_Prices.search_set_by_prices_run()
            elif userchoise == Item_Search_By.Specific_Item_Manu_Actions.SPECIFIC_SERACH_BY_PIECES.value:
                Item_Search_By_Set_Pieces.search_set_by_pieces_run()
            elif userchoise == Item_Search_By.Specific_Item_Manu_Actions.SPECIFIC_SERACH_BY_EXIT.value:
                break

#Class for Searching Items By Number- from class Item_Search_By#
class Item_Search_By_Set_Number(Item_Search_By):
    #Searching by set number menu action"
    class Item_Bt_Num_Search(Enum):
        ITEM_BY_NUM_EXIT = 1
        ITEM_BY_NUM_SEARCH_AGAIN = 2
    
    #Function that search lego set by number by users input and prints it#
    def search_set_by_number(setnum):
        for item in Search_Mech_All_Legos.all_sets:
            if item.SetNumber == str(setnum):
                print(f"Theme:{item.Theme} ,Item Name:{item.SetName},Pieces: {item.Pieces} ,Age:{item.Age} ,Price:{item.PriceDollars}")
        
        return item
                

    #Function To Item_Serch_by_run that containce the flow of searching functions in Item Search By NUmber section by his input#
    def search_set_by_num_run():
         while True:
                    print("Enter Set Number: ")
                    user_set_num_enter = Search_Mech_All_Legos.user_choosing_fun_by_int()
                    Item_Search_By_Set_Number.search_set_by_number(setnum=user_set_num_enter)
                    print("1) Back to Menu\n2)search something else(By set Number)\nEnter: ")
                    user_set_num_enter_second_choise = Search_Mech_All_Legos.user_choosing_fun_by_int()
                    if user_set_num_enter_second_choise ==  Item_Search_By_Set_Number.Item_Bt_Num_Search.ITEM_BY_NUM_EXIT.value:
                        break
                    elif user_set_num_enter_second_choise ==  Item_Search_By_Set_Number.Item_Bt_Num_Search.ITEM_BY_NUM_SEARCH_AGAIN.value:
                        print("Enter Set Number: ")
                        user_set_num_enter = Search_Mech_All_Legos.user_choosing_fun_by_int()
                        Item_Search_By_Set_Number.search_set_by_number(setnum=user_set_num_enter)


#Class for Searching Items By Age Range- from class Item_Search_By# 
class Item_Search_By_Set_Age(Item_Search_By):
    #Item Serch by Age Menu Actions#
    class Item_By_Age_Search(Enum):
        ITEM_BY_AGE_RANGE_4_12 = 1
        ITEM_BY_AGE_RANGE_12_15 = 2
        ITEM_BY_AGE_RANGE_15_20 = 3
        ITEM_BY_AGE_RANGE_20_99 = 4
        ITEM_BY_AGE_EXIT = 5
        
    #Function that search lego set by age ranges by users input and prints it#
    def search_set_by_age(agerange):
        if agerange == Item_Search_By_Set_Age.Item_By_Age_Search.ITEM_BY_AGE_RANGE_4_12.value:
            for item in Search_Mech_All_Legos.all_sets:
                try:
                    if 4 <=  int(item.Age) <= 12:
                        print(f"Theme:{item.Theme} ,Item Name:{item.SetName},Pieces: {item.Pieces} ,Age:{item.Age} ,Price:{item.PriceDollars}")
                except:
                    pass
        elif agerange == Item_Search_By_Set_Age.Item_By_Age_Search.ITEM_BY_AGE_RANGE_12_15.value:
            for item in Search_Mech_All_Legos.all_sets:
                try:
                    if 12 <  int(item.Age) <= 15:
                        print(f"Theme:{item.Theme} ,Item Name:{item.SetName},Pieces: {item.Pieces} ,Age:{item.Age} ,Price:{item.PriceDollars}")
                except:
                    pass
        elif agerange == Item_Search_By_Set_Age.Item_By_Age_Search.ITEM_BY_AGE_RANGE_15_20.value:
            for item in Search_Mech_All_Legos.all_sets:
                try:
                    if 15 <  int(item.Age) <= 20:
                        print(f"Theme:{item.Theme} ,Item Name:{item.SetName},Pieces: {item.Pieces} ,Age:{item.Age} ,Price:{item.PriceDollars}")
                except:
                    pass
        elif agerange == Item_Search_By_Set_Age.Item_By_Age_Search.ITEM_BY_AGE_RANGE_20_99:
            for item in Search_Mech_All_Legos.all_sets:
                try:
                    if 20 <  int(item.Age) <= 99:
                        print(f"Theme:{item.Theme} ,Item Name:{item.SetName},Pieces: {item.Pieces} ,Age:{item.Age} ,Price:{item.PriceDollars}")
                except:
                    pass
    
    #Function To Item_Serch_by_run that containce the flow of searching functions in Item Search By Age section by his input#    
    def search_set_by_age_run():
        while True:
            print("\n")
            print("Choose your Age range:\n1)4-12\n2)12-15\n3)15-20\n4)20-99\n5)Back to Menu\nEnter :")
            user_set_age_enter = Search_Mech_All_Legos.user_choosing_fun_by_int()
            Item_Search_By_Set_Age.search_set_by_age(agerange=user_set_age_enter)
            if user_set_age_enter == Item_Search_By_Set_Age.Item_By_Age_Search.ITEM_BY_AGE_EXIT.value:
                break                

#Class for Searching Items By Prices Range- from class Item_Search_By# 
class Item_Search_By_Set_Prices(Item_Search_By):
    #Item Serch by Prices Menu Actions#
    class Item_By_Prices_Search(Enum):   
        ITEM_BY_PRICE_LOWEST_HIGHEST = 1
        ITEM_BY_PRICE_HIGHEST_LOWEST =2
        ITEM_BY_PRICE_SPECIFIC_BUDGET = 3
        ITEM_BY_PRICE_EXIT = 4
     
    #Function that search lego sets from lowest to highest price#
    def search_set_by_price_lowest_highst():
        FromLowestPrice = []
        for item in Search_Mech_All_Legos.all_sets:
            try:
                FromLowestPrice.append([float(item.PriceDollars) ,item.Theme,item.SetName,item.SetNumber])
            except:
                pass
        FromLowestPrice.sort(key = lambda x: x[0])
        for item in FromLowestPrice:
            if item[0] == 'Price in Dollars':
                pass
            else:
                print(item)
        
        return FromLowestPrice
    
    #Function that search lego sets from highest to lowest price#
    def search_set_by_price_highst_lowest():
            FromHighestPrice = Item_Search_By_Set_Prices.search_set_by_price_lowest_highst()
            FromHighestPrice.sort(reverse=True)
            for item in FromHighestPrice:
                if item[0] == 'Price in Dollars':
                    pass
                else:
                    print(item)
    
    #Function that search lego sets by users budget input#
    def search_set_by_price_budget(usernum1 ,usernum2):
        MySets = []
        for item in Search_Mech_All_Legos.all_sets:
            try:
                MySets.append([float(item.PriceDollars) ,item.Theme,item.SetName,item.SetNumber])
            except:
                pass
            
        for item in MySets:
            if float(usernum1) < float(item[0]) and float(item[0]) < float(usernum2):
                print(item)
            else:
                pass   
            
    #Function To Item_Serch_by_run that containce the flow of searching functions in Item Search By Prices section by his input#    
    def search_set_by_prices_run():
        while True:
            print("\n")
            print("Searching by Price:\n1)Lowest to Highest\n2)Highest to Lowest\n3)Specific Budget\n4)Back to Menu\nEnter :")
            user_set_price_enter = Search_Mech_All_Legos.user_choosing_fun_by_int()
            if user_set_price_enter == Item_Search_By_Set_Prices.Item_By_Prices_Search.ITEM_BY_PRICE_LOWEST_HIGHEST.value:
                Item_Search_By_Set_Prices.search_set_by_price_lowest_highst()
            elif user_set_price_enter == Item_Search_By_Set_Prices.Item_By_Prices_Search.ITEM_BY_PRICE_HIGHEST_LOWEST.value:
                Item_Search_By_Set_Prices.search_set_by_price_highst_lowest()
            elif user_set_price_enter == Item_Search_By_Set_Prices.Item_By_Prices_Search.ITEM_BY_PRICE_SPECIFIC_BUDGET.value:
                print("Enter Lowest Budget Price:")
                user_lowest_bug_enter = Search_Mech_All_Legos.user_choosing_fun_by_int()
                print("Enter Highest Budget Price:")
                user_highest_bug_enter = Search_Mech_All_Legos.user_choosing_fun_by_int()
                Item_Search_By_Set_Prices.search_set_by_price_budget(usernum1=float(user_lowest_bug_enter) , usernum2=float(user_highest_bug_enter))
            elif user_set_price_enter == Item_Search_By_Set_Prices.Item_By_Prices_Search.ITEM_BY_PRICE_EXIT.value:
                break  

#Class for Searching Items By Pieces Range- from class Item_Search_By# 
class Item_Search_By_Set_Pieces(Item_Search_By):
    #Item Serch by Pieces Menu Actions#
    class Item_By_Pieces_Search(Enum):
        ITEM_BY_Pieces_LOWEST_HIGHEST = 1
        ITEM_BY_Pieces_HIGHEST_LOWEST =2
        ITEM_BY_Pieces_SPECIFIC_BUDGET = 3
        ITEM_BY_Pieces_EXIT = 4
        
    #Function that search lego sets from lowest to highest Pieces#
    def search_set_by_Pieces_lowest_highst():
        FromLowestPieces = []
        for item in Search_Mech_All_Legos.all_sets:
            try:
                FromLowestPieces.append([float(item.Pieces) ,item.Theme,item.SetName,item.SetNumber])
            except:
                pass
        FromLowestPieces.sort(key = lambda x: x[0])
        for item in FromLowestPieces:
            if item[0] == 'Pieces':
                pass
            else:
                print(item)
        
        return FromLowestPieces
    
    #Function that search lego sets from highest to lowest Pieces#
    def search_set_by_Pieces_highst_lowest():
            FromHighestPieces = []
            for item in Search_Mech_All_Legos.all_sets:
                try:
                    FromHighestPieces.append([float(item.Pieces) ,item.Theme,item.SetName,item.SetNumber])
                except:
                    pass
            FromHighestPieces.sort(reverse=True)
            for item in FromHighestPieces:
                if item[0] == 'Pieces':
                    pass
                else:
                    print(item)
    
    #Function that search lego sets by users range of Pieces input#
    def search_set_by_Pieces_budget(usernum1 ,usernum2):
        MySets = []
        for item in Search_Mech_All_Legos.all_sets:
            try:
                MySets.append([float(item.Pieces) ,item.Theme,item.SetName,item.SetNumber])
            except:
                pass
            
        for item in MySets:
            if float(usernum1) < float(item[0]) and float(item[0]) < float(usernum2):
                print(item)
            else:
                pass
    
    #Function To Item_Serch_by_run that containce the flow of searching functions in Item Search By Pieces section by his input#
    def search_set_by_pieces_run():
        while True:
            print("\n")
            print("Searching by Price:\n1)Lowest to Highest\n2)Highest to Lowest\n3)Specific Pieces Range?\n4)Back to Menu\nEnter :")
            user_set_price_enter = Search_Mech_All_Legos.user_choosing_fun_by_int()
            if user_set_price_enter == Item_Search_By_Set_Pieces.Item_By_Pieces_Search.ITEM_BY_Pieces_LOWEST_HIGHEST.value:
                Item_Search_By_Set_Pieces.search_set_by_Pieces_lowest_highst()
            elif user_set_price_enter == Item_Search_By_Set_Pieces.Item_By_Pieces_Search.ITEM_BY_Pieces_HIGHEST_LOWEST.value:
                Item_Search_By_Set_Pieces.search_set_by_Pieces_highst_lowest()
            elif user_set_price_enter == Item_Search_By_Set_Pieces.Item_By_Pieces_Search.ITEM_BY_Pieces_SPECIFIC_BUDGET.value:
                print("Enter Lowest Number of Pieces:")
                user_lowest_bug_enter = Search_Mech_All_Legos.user_choosing_fun_by_int()
                print("Enter Highest Number of Pieces:")
                user_highest_bug_enter = Search_Mech_All_Legos.user_choosing_fun_by_int()
                Item_Search_By_Set_Pieces.search_set_by_Pieces_budget(usernum1=float(user_lowest_bug_enter) , usernum2=float(user_highest_bug_enter))
            elif user_set_price_enter == Item_Search_By_Set_Pieces.Item_By_Pieces_Search.ITEM_BY_Pieces_EXIT.value:
                break


#Class for Searching Items By Name - from class Item_Search_By# 
class Item_Search_By_Set_Name(Item_Search_By):
     def search_set_by_name(setname):
        for item in Search_Mech_All_Legos.all_sets:
            if item.SetName == str(setname):
                print(f"Theme:{item.Theme} ,Item Name:{item.SetName},Pieces: {item.Pieces} ,Age:{item.Age} ,Price:{item.PriceDollars}")
        
        return item


