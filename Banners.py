#Banner Printer for Website Page Change#
class Banner_Printer():
    def print_menu():
        with open("loggingbanner.txt" , "r") as banner:
            for i in banner:
                print(i , end="")
           
    def print_enternce_logo():
        banner = """
    
    █████       ██████████   █████████     ███████        █████████  █████   █████    ███████    ███████████ 
    ░░███       ░░███░░░░░█  ███░░░░░███  ███░░░░░███     ███░░░░░███░░███   ░░███   ███░░░░░███ ░░███░░░░░███
     ░███        ░███  █ ░  ███     ░░░  ███     ░░███   ░███    ░░░  ░███    ░███  ███     ░░███ ░███    ░███
     ░███        ░██████   ░███         ░███      ░███   ░░█████████  ░███████████ ░███      ░███ ░██████████ 
     ░███        ░███░░█   ░███    █████░███      ░███    ░░░░░░░░███ ░███░░░░░███ ░███      ░███ ░███░░░░░░  
     ░███      █ ░███ ░   █░░███  ░░███ ░░███     ███     ███    ░███ ░███    ░███ ░░███     ███  ░███        
     ███████████ ██████████ ░░█████████  ░░░███████░     ░░█████████  █████   █████ ░░░███████░   █████       
    ░░░░░░░░░░░ ░░░░░░░░░░   ░░░░░░░░░     ░░░░░░░        ░░░░░░░░░  ░░░░░   ░░░░░    ░░░░░░░    ░░░░░   
     
    ⠀⠀                                        ⣠⣤⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣤⣄⠀⠀
⠀                                            ⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀
                                            ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
                                            ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
                                            ⢸⣿⣿⣿⠏⠁⢸⣿⠋⠀⠀⠀⡹⠋⠁⠀⠀⠙⡿⠋⠀⠀⠈⢻⣿⡇
                                            ⢸⣿⣿⠏⠀⢀⣾⠃⠀⠰⠿⣿⠃⠀⣼⠯⢤⣼⠁⠀⣼⠇⠀⣸⣿⡇
                                            ⢸⣿⡟⠀⢀⣼⡏⠀⢀⣤⣴⡇⠀⢸⣅⠀⠀⠇⠀⢸⡟⠀⢀⣿⣿⡇
                                            ⢸⣿⠁⠀⠈⠉⡇⠀⠈⠉⢹⡇⠀⠈⠁⢀⣼⡀⠀⠈⠁⢀⣾⣿⣿⡇
                                            ⢸⣿⣷⣶⣶⣾⣿⣶⣤⣶⣿⣿⣶⣴⣶⣿⣿⣿⣶⣴⣶⣿⣿⣿⣿⡇
                                            ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
                                            ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠀                                            ⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀
⠀⠀                                            ⠙⠛⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠛⠋⠀⠀                     
    ~By Daniel Lifshits ᕦ(⌐■ ͜ʖ■)ᕥ ~                  
                                                                                                          """
        return print(banner)

    def print_theme_logo():
        banner = """
    ,---------. .---.  .---.     .-''-.  ,---.    ,---.    .-''-.     .-'''-.  
    \          \|   |  |_ _|   .'_ _   \ |    \  /    |  .'_ _   \   / _     \ 
     `--.  ,---'|   |  ( ' )  / ( ` )   '|  ,  \/  ,  | / ( ` )   ' (`' )/`--' 
        |   \   |   '-(_{;}_). (_ o _)  ||  |\_   /|  |. (_ o _)  |(_ o _).    
        :_ _:   |      (_,_) |  (_,_)___||  _( )_/ |  ||  (_,_)___| (_,_). '.  
        (_I_)   | _ _--.   | '  \   .---.| (_ o _) |  |'  \   .---..---.  \  : 
       (_(=)_)  |( ' ) |   |  \  `-'    /|  (_,_)  |  | \  `-'    /\    `-'  | 
        (_I_)   (_{;}_)|   |   \       / |  |      |  |  \       /  \       /  
        '---'   '(_,_) '---'    `'-..-'  '--'      '--'   `'-..-'    `-...-'   
"""
        return print(banner)
    
    def print_shipping_logo():
        banner = """
    ███████╗██╗  ██╗██╗██████╗ ██████╗ ██╗███╗   ██╗ ██████╗     
    ██╔════╝██║  ██║██║██╔══██╗██╔══██╗██║████╗  ██║██╔════╝     
    ███████╗███████║██║██████╔╝██████╔╝██║██╔██╗ ██║██║  ███╗    
    ╚════██║██╔══██║██║██╔═══╝ ██╔═══╝ ██║██║╚██╗██║██║   ██║    
    ███████║██║  ██║██║██║     ██║     ██║██║ ╚████║╚██████╔╝    
    ╚══════╝╚═╝  ╚═╝╚═╝╚═╝     ╚═╝     ╚═╝╚═╝  ╚═══╝ ╚═════╝                                                                      
⠀⠀⢔⢁⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢠⣭⣿⠟⣒⣒⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⠤⠤⠄⠀⣀⣀⣀⣀⣀⣀⣀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢟⢻⡍⠉⣽⢛⠷⢤⣤⣴⣶⣶⣾⡇⠡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠈⠉⠉⠉⠉⠉⠉⠒⠒⠒⠒⠒⠒⠒⠒⠲⠤⠤⠤⠤⠤⠤⠄⣤⣀⣤⣤⣤⣴⣿⣦⣄⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢊⣸⡿⠿⡌⢷⡀⠧⣌⠓⣤⣯⡉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⣉⢹⣛⠏⢹⠉⠙⠋⠉⠉⠙⠒⠒⠒⠒⠒⠒⠒⠲⠤⠤⠤⠤⠤⠤⠤⢤⣀⣀⣀⣀⣀⡀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠸⡘⣧⠀⠈⢿⠛⠙⣿⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⡀⠀⡗⠩⢿⠩⣍⣀⣀⣀⣀⣠⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠈⠉⠉⠉⠉⠉⠀⠒⠒⠒⠒⠂
⠀⠀⠀⠀⠀⢱⠹⣇⠀⠘⣏⠁⠘⡝⠇⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⡤⢴⠶⠶⠿⠿⠿⠶⠶⠶⠶⣶⠶⠤⠦⠤⠤⠤⡞⠋⡿⣿⠚⠲⠒⠦⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢣⣻⡄⠂⠘⡆⢀⠈⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠄⣲⣿⣴⣾⣿⣿⣿⣶⣿⣿⣿⣷⣾⣶⣶⣾⣾⣩⣭⣿⠓⢿⠸⡏⠁⣷⠻⣧⡀⠀⠀⠀⣿⣿⠉⠙⠒⠤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠱⠿⣄⣠⠿⡬⠤⠚⢆⠀⠀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣠⣄⣠⣤⠤⢤⣤⣤⣤⣤⣰⣦⠶⢒⣮⣷⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡙⠛⠙⣒⣟⣰⡇⠀⣷⢠⡽⢧⣀⣀⣈⣿⣿⣶⡀⠀⠀⠈⠋⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠄⠶⠶⠿⡟⣻⡷⠤⠿⡿⠶⠾⠿⠿⠿⠛⠟⠛⠛⠛⠛⠛⠛⡛⠛⠋⠛⠉⠉⠉⠉⠉⠉⠉⠉⡏⠉⠉⠉⠉⠁⠈⠀⠉⠉⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣽⣿⣿⣍⠩⢀⠠⡽⡉⠙⢚⠻⢿⣿⣿⣽⣭⣓⡶⢦⣄⣰⠿⣿⠉⠙⠒⢶⣴⣶⣴⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⡴⢋⣿⣤⣶⣶⣧⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣧⣦⣶⣶⣶⣶⣴⣦⣶⣴⣦⣶⣷⣤⣤⣤⣤⣤⣤⣴⣴⣶⣼⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⢳⠛⠉⠛⠉⠉⠉⠉⠉⠋⢹⡉⠚⠛⠛⠛⠛⠛⠿⠿⣈⡉⠉⡿⢶⠛⠍⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣴⡿⠛⠉⠁⠈⠛⠙⠛⠛⠛⠛⠛⠛⠛⠛⣟⣛⡛⠛⠛⠿⠿⠿⠿⠿⠿⠿⠿⢿⡿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣿⣿⣿⣿⣤⣀⣀⣀⣀⣀⣀⣀⣀⣸⣁⣀⣀⣀⣀⣀⣀⣀⣀⣤⣾⣿⣧⣈⠻⠾⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠘⠾⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠁⠀⠐⠘⠓⠒⠀⠒⠉⠙⠛⠟⠛⠛⠛⠛⠛⠛⠛⢻⣿⡏⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⢹⣿⣿⣿⡿⣿⢿⣿⣿⣛⠉⠉⡏⢉⣽⡟⠉⠉⢻⣿⠿⠉⠉⠉⠉⠉⠉⠈⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⠛⠛⠉⠉⠉⠉⠉⠉⠀⢀⣧⡾⠃⠀⠀⠴⠿⠿⠦⠤⠤⠤⠤⠤⠤⠦⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣴⣶⣾⣟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣞⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀              
"""
        return print(banner)
    
    def print_search_logo():
        banner = """
    ███████╗███████╗ █████╗ ██████╗  ██████╗██╗  ██╗
    ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝██║  ██║
    ███████╗█████╗  ███████║██████╔╝██║     ███████║
    ╚════██║██╔══╝  ██╔══██║██╔══██╗██║     ██╔══██║
    ███████║███████╗██║  ██║██║  ██║╚██████╗██║  ██║
    ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝                                                         
    ⠀⠀⣀⠠⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠈⠉⠙⠛⠿⠶⠶⣖⣢⣔⣶⡄⠀⠀⠀⠀⠀⢤⣀⣀⣀⣀⣀⣠⣤⣴⣶⡲⠆⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀
    ⢀⣀⣤⣤⡖⠛⣭⡉⠓⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⢴⠒⠒⠒⠦⢄⡀⠀⠀
    ⠙⣇⠀⠀⣷⡀⠛⠃⢀⡇⠙⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡿⠟⠉⢿⠀⠿⠃⢀⡇⠈⣱⣦
    ⠀⠈⠳⣄⠀⠙⠓⠋⠉⣀⡔⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣦⡀⠘⠷⠦⠶⠋⢀⡴⠋⠀
    ⠀⠀⠀⠈⠓⠦⠤⠖⠚⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠷⣦⣤⣶⠞⠉⠀⠀⠀
    """
        return print(banner)
    
    def print_avaliable_logo():
        banner = """
     █████╗ ██╗   ██╗ █████╗ ██╗██╗      █████╗ ██████╗ ██╗     ███████╗    ███████╗████████╗ ██████╗  ██████╗██╗  ██╗
    ██╔══██╗██║   ██║██╔══██╗██║██║     ██╔══██╗██╔══██╗██║     ██╔════╝    ██╔════╝╚══██╔══╝██╔═══██╗██╔════╝██║ ██╔╝
    ███████║██║   ██║███████║██║██║     ███████║██████╔╝██║     █████╗      ███████╗   ██║   ██║   ██║██║     █████╔╝ 
    ██╔══██║╚██╗ ██╔╝██╔══██║██║██║     ██╔══██║██╔══██╗██║     ██╔══╝      ╚════██║   ██║   ██║   ██║██║     ██╔═██╗ 
    ██║  ██║ ╚████╔╝ ██║  ██║██║███████╗██║  ██║██████╔╝███████╗███████╗    ███████║   ██║   ╚██████╔╝╚██████╗██║  ██╗
    ╚═╝  ╚═╝  ╚═══╝  ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝    ╚══════╝   ╚═╝    ╚═════╝  ╚═════╝╚═╝  ╚═╝
"""
        return print(banner)
    
    def print_exit_logo():
        banner = """


 
                                                                                    
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠤⠤⠄⠀⠤⠤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ___                      __                __      __   __   __   __   __       ___            
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⢁⣠⡀⠀⠀⠀⠀⠀⠈⠑⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  |  |__|  /\  |\ | |__/ /__`     /\  |\ | |  \    / _` /  \ /  \ |  \ |__) \ / |__       
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⠁⢀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  |  |  | /~~\ | \| |  \ .__/    /~~\ | \| |__/    \__> \__/ \__/ |__/ |__)  |  |___
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣅⣶⠟⢻⠉⠉⠛⠛⠳⠶⢤⣤⣀⡀⠀⢸⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡟⣸⡏⠀⠸⠀⠀⣀⠀⠀⠀⠀⠀⠉⠙⢷⣾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠃⣾⠀⠀⡇⠀⠸⣿⠇⠀⠀⣠⣄⠀⠀⠀⣿⣷⠀⠀⠀⢀⣠⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⡄⢿⠀⠀⠀⣿⣷⣶⣤⣄⣀⣙⣋⠀⠀⠀⣿⡏⠀⠀⢠⣿⣿⣿⡄⠀⣰⣷⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢾⡏⠧⠌⠳⠶⠤⠼⠿⣿⣛⡻⢿⣿⣿⠃⠀⢰⢻⠇⠀⠀⢿⣿⣿⣿⡇⣠⣿⣿⣷⡀
⠀⠀⠀⠀⠀⠀⠀⠐⣿⣷⡶⣤⣄⡀⠀⠀⠀⠀⠉⢻⠚⠿⣅⣀⣀⡎⡜⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⡇
⠀⠀⠀⢀⣄⣀⡀⠀⠈⣿⣿⡖⠈⠉⠛⢶⣶⣤⣤⣾⠀⠀⠀⠉⠛⢶⡁⠀⠀⠀⠀⢠⣿⣿⡻⠿⣿⣿⡿⠁
⠀⠀⠀⢸⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣤⣤⣴⡾⠃⠀⠀⠀⣼⣿⢿⣿⣿⣿⡛⠋⠀⠀
⠀⠀⢀⣼⣿⡿⠿⠿⢿⣿⡉⠁⠀⠀⠉⠉⠛⠻⠿⠿⠿⠿⠧⢤⣄⣀⠀⠀⠀⣰⣿⣿⠙⠛⠾⣿⠃⠀⠀⠀
⠀⢠⣿⣿⣶⣶⣶⣶⣤⣬⣿⡇⠀⠀⠀⠀⢀⣀⡀⠀⠀⠀⠀⠀⠀⠈⠱⣴⣾⣿⣿⣿⠸⠀⢀⡏⠀⠀⠀⠀
⠀⢼⣿⣿⢟⡂⢀⡈⠭⣿⣿⡇⠀⠀⠀⣴⠟⠋⠙⠓⣦⠀⣾⢛⣿⣿⠀⢸⣿⣿⣿⡟⠀⠀⣼⠀⠀⠀⠀⠀
⠀⠈⣿⣿⡯⠃⠈⠉⠉⠛⢿⡄⠀⢀⣠⣿⠀⢀⣤⣴⣿⣿⡿⠿⠿⠋⠀⠈⣿⣿⣿⣿⠀⣤⠇⠀⠀⠀⠀⠀
⠀⠀⣿⠏⠁⠀⠀⠀⠀⠀⢰⡇⠀⠸⣿⣽⣿⣿⠿⣿⣥⠏⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⡴⠋⠀⠀⠀⠀⠀⠀
⠀⢰⣿⣤⣀⣀⣀⡀⠀⠀⢸⠀⠀⠀⠀⠀⠈⠙⠛⠛⠁⠀⠀⠀⠀⠀⠀⠀⢸⠿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀
⠰⣿⣿⣿⣛⣯⡭⢽⣷⣦⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⣿⣿⣿⠉⠀⣀⡀⠀⠙⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠙⣿⣿⣿⣿⠟⠛⢿⣶⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣿⣿⣿⣿⡂⠀⢸⣿⡃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠈⢹⣿⣿⠗⠆⠘⢻⠿⠉⠉⠉⠉⠙⠒⠀⠒⠀⠀⠀⠠⠤⢄⡀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀                                                                       
    """
        return print(banner)

    def print_cart_logo():
        banner = """
███╗   ███╗██╗   ██╗     ██████╗ █████╗ ██████╗ ████████╗
████╗ ████║╚██╗ ██╔╝    ██╔════╝██╔══██╗██╔══██╗╚══██╔══╝
██╔████╔██║ ╚████╔╝     ██║     ███████║██████╔╝   ██║   
██║╚██╔╝██║  ╚██╔╝      ██║     ██╔══██║██╔══██╗   ██║   
██║ ╚═╝ ██║   ██║       ╚██████╗██║  ██║██║  ██║   ██║   
╚═╝     ╚═╝   ╚═╝        ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝ 
"""
        return print(banner)
      