from os import system, name
import colorama
from colorama import Fore, Back, Style
import time
colorama.init()
clear = lambda: system("clear" if name == "posix" else "cls")

print(Fore.RED + "LOGIN")
print(Style.RESET_ALL)

sys_username = "secretlogin"
sys_password = "Dar.kWor7d"
right_entry = 5
while True:
    username = input("Username: ")
    password = input("Password: ")

    if (sys_username != username and sys_password == password):
        print(Fore.BLUE + "Being checked")
        time.sleep(1)
        print(Fore.RED + "Username is wrong!")
        right_entry -= 1
        print(Fore.BLUE + "Remaining entry:",right_entry)
        print(Style.RESET_ALL)

    elif (sys_username == username and sys_password != password):
        print(Fore.BLUE + "Being checked")
        time.sleep(1)
        print(Fore.RED + "Password is wrong!")
        right_entry -= 1
        print(Fore.BLUE + "Remaining entry:",right_entry)
        print(Style.RESET_ALL)

    elif (sys_username != username and sys_password != password):
        print(Fore.BLUE + "Being checked")
        time.sleep(1)
        print(Fore.RED + "Username and password are wrong!")
        right_entry -= 1
        print(Fore.BLUE + "Remaining entry:",right_entry)
        print(Style.RESET_ALL)

    else:
        print(Fore.BLUE + "Login to the system")
        print(Style.RESET_ALL)
        print("Please wait")
        time.sleep(5)
        clear()
        break

    if (right_entry == 0):
        print(Fore.RED + "Your login has expired")
        exit()

print(Fore.RED + """
 _____          _____  _  __ __          ________ ____  
|  __ \   /\   |  __ \| |/ / \ \        / /  ____|  _ \ 
| |  | | /  \  | |__) | ' /   \ \  /\  / /| |__  | |_) |
| |  | |/ /\ \ |  _  /|  <     \ \/  \/ / |  __| |  _ < 
| |__| / ____ \| | \ \| . \     \  /\  /  | |____| |_) |
|_____/_/    \_\_|  \_\_|\_\     \/  \/   |______|____/ 
""")
print(Style.RESET_ALL)
print(Fore.GREEN + "Security protection active")
print(Style.RESET_ALL)
print(Fore.BLUE + """
**************************************

1. HITMAN (Rent a HITMAN)

2. GEN (Bitcoin Generator)

3. Money World (Fake Money)

4. IdenFaker (Fake Identity)

5. MR.ROBOT (Rent a HACKER)

6. DARK STORE (Phones, drugs, rental girls and more)

7. RED ROOM (Just torture)

8. Surprise box (Top Secret)

9. Dark Chat (Private rooms)

Press 'q' to exit

**************************************
""")
print(Style.RESET_ALL)

while True:
    answer = input("Choose one: ")

    if (answer == "q"):
        print(Fore.RED + "Exiting....")
        time.sleep(1)
        break

    elif (answer == "1"):
        print(Fore.BLUE + """
        _______________________________________________________________________

                                         HITMAN
                                      Rent a HITMAN

         G - With a gun | 100% chance of dying | 0,184 BTC | 1 pc

         S - Strangling | 80% chance of dying | 0,215 BTC | 1 pc

         P - Poisoning | 100% chance of dying | 0,145 BTC | 1 pc

         T - With your tactics | ?% chance of dying | 0,267 BTC | 1 pc

         B - Businessman or protected man | 90% chance of dying | 0,418 BTC | 1 pc

         Press 'q' to exit
        ________________________________________________________________________
        """)
        print(Style.RESET_ALL)

        while True:
            answer_1 = input("Choose One: ")

            if (answer_1 == "q"):
                print(Fore.YELLOW + "Good Bye")
                print(Style.RESET_ALL)
                time.sleep(1)
                break

            elif (answer_1 == "G" or answer_1 == "g"):
                print(Fore.YELLOW + "You can rent your HITMAN after making the payment.")
                print()
                mail_1 = input("TOR MAIL (Leave blank to cancel payment): ")
                btctoken_1 = input("BITCOIN TOKEN (Leave blank to cancel payment): ")
                print("Your HITMAN will be emailed when payment is confirmed.")
                print(Style.RESET_ALL)
                pass

            elif (answer_1 == "S" or answer_1 == "s"):
                print(Fore.YELLOW + "You can rent your HITMAN after making the payment.")
                print()
                mail_1 = input("TOR MAIL (Leave blank to cancel payment): ")
                btctoken_1 = input("BITCOIN TOKEN (Leave blank to cancel payment): ")
                print("Your HITMAN will be emailed when payment is confirmed.")
                print(Style.RESET_ALL)
                pass

            elif (answer_1 == "P" or answer_1 == "p"):
                print(Fore.YELLOW + "You can rent your HITMAN after making the payment.")
                print()
                mail_1 = input("TOR MAIL (Leave blank to cancel payment): ")
                btctoken_1 = input("BITCOIN TOKEN (Leave blank to cancel payment): ")
                print("Your HITMAN will be emailed when payment is confirmed.")
                print(Style.RESET_ALL)
                pass

            elif (answer_1 == "T" or answer_1 == "t"):
                print(Fore.YELLOW + "You can rent your HITMAN after making the payment.")
                print()
                mail_1 = input("TOR MAIL (Leave blank to cancel payment): ")
                btctoken_1 = input("BITCOIN TOKEN (Leave blank to cancel payment): ")
                print("Your HITMAN will be emailed when payment is confirmed.")
                print(Style.RESET_ALL)
                pass

            elif (answer_1 == "B" or answer_1 == "b"):
                print(Fore.YELLOW + "You can rent your HITMAN after making the payment.")
                print()
                mail_1 = input("TOR MAIL (Leave blank to cancel payment): ")
                btctoken_1 = input("BITCOIN TOKEN (Leave blank to cancel payment): ")
                print("Your HITMAN will be emailed when payment is confirmed.")
                print(Style.RESET_ALL)
                pass

            else:
                print(Fore.RED + "Invalid option")
                print(Style.RESET_ALL)
                pass

    elif (answer == "2"):
        print(Fore.BLUE + """
        _______________________________________________________
                                       GEN
                                 BITCOIN GENERATOR

         B1 - BTC GEN2 | 1 BITCOIN | 0,00648 BTC | 1 pc
         B - BTC GEN | The amount you want | 0,00? BTC | 1 pc

         Press 'q' to exit
        ________________________________________________________
        """)
        print(Style.RESET_ALL)

        while True:
            answer_2 = input("Choose One: ")

            if (answer_2 == "q"):
                print(Fore.YELLOW + "Good Bye")
                print(Style.RESET_ALL)
                time.sleep(1)
                break

            elif (answer_2 == "B1" or answer_2 == "b1"):
                print(Fore.YELLOW + "You can get your BITCOIN after making the payment.")
                print()
                mail_2 = input("TOR MAIL (Leave blank to cancel payment): ")
                btctoken_2 = input("BITCOIN TOKEN (Leave blank to cancel payment): ")
                print("Your BITCOIN will be emailed when payment is confirmed.")
                print(Style.RESET_ALL)
                pass

            elif (answer_2 == "B" or answer_2 == "b"):
                print(Fore.YELLOW + "You can get your BITCOIN after making the payment.")
                print()
                mail_2 = input("TOR MAIL (Leave blank to cancel payment): ")
                btctoken_2 = input("BITCOIN TOKEN (Leave blank to cancel payment): ")
                print("Your BITCOIN will be emailed when payment is confirmed.")
                print(Style.RESET_ALL)
                pass

            else:
                print(Fore.RED + "Invalid option")
                print(Style.RESET_ALL)
                pass

    elif (answer == "3"):
        print(Fore.BLUE + """
        ______________________________________________________________
                                    MONEY WORLD
                                    Fake Money

         D - DOLLAR($) | Fake 1000$ | 0,00124 BTC | 1 pc
         E - EURO(€) | Fake 1000€ | 0,00148 BTC | 1 pc
         C - CANADIAN DOLLAR(C$) | Fake 1000C$ | 0,00124 BTC | 1 pc
         P - POUND(£) | Fake 1000£ | 0,00168 BTC | 1 pc
         R - RUBLE(₽) | Fake 1000₽ | 0,00088 BTC | 1 pc
         J - YEN(¥) | Fake 1000¥ | 0,00098 BTC | 1 pc
         T - TL(₺) | Fake 1000₺ | 0,00098 BTC | 1 pc
         CH - YUAN(¥) | Fake 1000¥ | 0,00098 BTC | 1 pc

         Press 'q' to exit
        ________________________________________________________________
        """)
        print(Style.RESET_ALL)

        while True:
            answer_3 = input("Choose One: ")

            if (answer_3 == "q"):
                print(Fore.YELLOW + "Good Bye")
                print(Style.RESET_ALL)
                time.sleep(1)
                break

            elif (answer_3 == "D" or answer_3 == "d"):
                print(Fore.YELLOW + "You can get your fake money after making the payment.")
                print()
                mail_3 = input("TOR MAIL (Leave blank to cancel payment): ")
                btctoken_3 = input("BITCOIN TOKEN (Leave blank to cancel payment): ")
                print("Your fake money will be emailed when payment is confirmed.")
                print(Style.RESET_ALL)
                pass

            elif (answer_3 == "E" or answer_3 == "e"):
                print(Fore.YELLOW + "You can get your fake money after making the payment.")
                print()
                mail_3 = input("TOR MAIL (Leave blank to cancel payment): ")
                btctoken_3 = input("BITCOIN TOKEN (Leave blank to cancel payment): ")
                print("Your fake money will be emailed when payment is confirmed.")
                print(Style.RESET_ALL)
                pass

            elif (answer_3 == "C" or answer_3 == "c"):
                print(Fore.YELLOW + "You can get your fake money after making the payment.")
                print()
                mail_3 = input("TOR MAIL (Leave blank to cancel payment): ")
                btctoken_3 = input("BITCOIN TOKEN (Leave blank to cancel payment): ")
                print("Your fake money will be emailed when payment is confirmed.")
                print(Style.RESET_ALL)
                pass

            elif (answer_3 == "P" or answer_3 == "p"):
                print(Fore.YELLOW + "You can get your fake money after making the payment.")
                print()
                mail_3 = input("TOR MAIL (Leave blank to cancel payment): ")
                btctoken_3 = input("BITCOIN TOKEN (Leave blank to cancel payment): ")
                print("Your fake money will be emailed when payment is confirmed.")
                print(Style.RESET_ALL)
                pass

            elif (answer_3 == "R" or answer_3 == "r"):
                print(Fore.YELLOW + "You can get your fake money after making the payment.")
                print()
                mail_3 = input("TOR MAIL (Leave blank to cancel payment): ")
                btctoken_3 = input("BITCOIN TOKEN (Leave blank to cancel payment): ")
                print("Your fake money will be emailed when payment is confirmed.")
                print(Style.RESET_ALL)
                pass

            elif (answer_3 == "J" or answer_3 == "j"):
                print(Fore.YELLOW + "You can get your fake money after making the payment.")
                print()
                mail_3 = input("TOR MAIL (Leave blank to cancel payment): ")
                btctoken_3 = input("BITCOIN TOKEN (Leave blank to cancel payment): ")
                print("Your fake money will be emailed when payment is confirmed.")
                print(Style.RESET_ALL)
                pass

            elif (answer_3 == "T" or answer_3 == "t"):
                print(Fore.YELLOW + "You can get your fake money after making the payment.")
                print()
                mail_3 = input("TOR MAIL (Leave blank to cancel payment): ")
                btctoken_3 = input("BITCOIN TOKEN (Leave blank to cancel payment): ")
                print("Your fake money will be emailed when payment is confirmed.")
                print(Style.RESET_ALL)
                pass

            elif (answer_3 == "CH" or answer_3 == "ch"):
                print(Fore.YELLOW + "You can get your fake money after making the payment.")
                print()
                mail_3 = input("TOR MAIL (Leave blank to cancel payment): ")
                btctoken_3 = input("BITCOIN TOKEN (Leave blank to cancel payment): ")
                print("Your fake money will be emailed when payment is confirmed.")
                print(Style.RESET_ALL)
                pass

            else:
                print(Fore.RED + "Invalid option")
                print(Style.RESET_ALL)
                pass

    elif (answer == "4"):
        print(Fore.BLUE + """
        ___________________________________________________________
        
                                 IDENFAKER
                               Fake Identity
                  
         UK - United Kingdom | Fake Identity | 0,0025 BTC | 1 pc
        
         US - United States Of America | Fake Identity | 0,0035 BTC | 1 pc
        
         DE - Germany | Fake Identity | 0,0023 BTC | 1 pc
        
         RF - Russia | Fake Identity | 0,0021 BTC | 1 pc
        
         CA - Canada | Fake Identity | 0,0019 BTC | 1 pc
        
         CH - Switzerland | Fake Identity | 0,0020 BTC | 1 pc
        
         SE - Sweden | Fake Identity | 0,0027 BTC | 1 pc
        
         CN - Chinese | Fake Identity | 0,0032 BTC | 1 pc
        
         JP - Japan | Fake Identity | 0,0017 BTC | 1 pc
        
         TR - Turkey | Fake Identity | 0,0014 BTC | 1 pc
         
         Press 'q' to exit
        ___________________________________________________________
        """)
        print(Style.RESET_ALL)

        while True:
            answer_4 = input("Choose One: ")

            if (answer_4 == "q"):
                print(Fore.YELLOW + "Good Bye")
                print(Style.RESET_ALL)
                time.sleep(1)
                break

            elif (answer_4 == "UK" or answer_4 == "uk"):
                print(Fore.YELLOW + "You can get your Fake ID after making the payment.")
                print()
                mail_4 = input("TOR MAIL (Leave blank to cancel payment): ")
                btctoken_4 = input("BITCOIN TOKEN (Leave blank to cancel payment): ")
                print("Your Fake ID will be emailed when payment is confirmed.")
                print(Style.RESET_ALL)
                pass

            elif (answer_4 == "US" or answer_4 == "us"):
                print(Fore.YELLOW + "You can get your Fake ID after making the payment.")
                print()
                mail_4 = input("TOR MAIL (Leave blank to cancel payment): ")
                btctoken_4 = input("BITCOIN TOKEN (Leave blank to cancel payment): ")
                print("Your Fake ID will be emailed when payment is confirmed.")
                print(Style.RESET_ALL)
                pass

            elif (answer_4 == "DE" or answer_4 == "de"):
                print(Fore.YELLOW + "You can get your Fake ID after making the payment.")
                print()
                mail_4 = input("TOR MAIL (Leave blank to cancel payment): ")
                btctoken_4 = input("BITCOIN TOKEN (Leave blank to cancel payment): ")
                print("Your Fake ID will be emailed when payment is confirmed.")
                print(Style.RESET_ALL)
                pass

            elif (answer_4 == "RF" or answer_4 == "rf"):
                print(Fore.YELLOW + "You can get your Fake ID after making the payment.")
                print()
                mail_4 = input("TOR MAIL (Leave blank to cancel payment): ")
                btctoken_4 = input("BITCOIN TOKEN (Leave blank to cancel payment): ")
                print("Your Fake ID will be emailed when payment is confirmed.")
                print(Style.RESET_ALL)
                pass

            elif (answer_4 == "CA" or answer_4 == "ca"):
                print(Fore.YELLOW + "You can get your Fake ID after making the payment.")
                print()
                mail_4 = input("TOR MAIL (Leave blank to cancel payment): ")
                btctoken_4 = input("BITCOIN TOKEN (Leave blank to cancel payment): ")
                print("Your Fake ID will be emailed when payment is confirmed.")
                print(Style.RESET_ALL)
                pass

            elif (answer_4 == "CH" or answer_4 == "ch"):
                print(Fore.YELLOW + "You can get your Fake ID after making the payment.")
                print()
                mail_4 = input("TOR MAIL (Leave blank to cancel payment): ")
                btctoken_4 = input("BITCOIN TOKEN (Leave blank to cancel payment): ")
                print("Your Fake ID will be emailed when payment is confirmed.")
                print(Style.RESET_ALL)
                pass

            elif (answer_4 == "SE" or answer_4 == "se"):
                print(Fore.YELLOW + "You can get your Fake ID after making the payment.")
                print()
                mail_4 = input("TOR MAIL (Leave blank to cancel payment): ")
                btctoken_4 = input("BITCOIN TOKEN (Leave blank to cancel payment): ")
                print("Your Fake ID will be emailed when payment is confirmed.")
                print(Style.RESET_ALL)
                pass

            elif (answer_4 == "CN" or answer_4 == "cn"):
                print(Fore.YELLOW + "You can get your Fake ID after making the payment.")
                print()
                mail_4 = input("TOR MAIL (Leave blank to cancel payment): ")
                btctoken_4 = input("BITCOIN TOKEN (Leave blank to cancel payment): ")
                print("Your Fake ID will be emailed when payment is confirmed.")
                print(Style.RESET_ALL)
                pass

            elif (answer_4 == "JP" or answer_4 == "jp"):
                print(Fore.YELLOW + "You can get your Fake ID after making the payment.")
                print()
                mail_4 = input("TOR MAIL (Leave blank to cancel payment): ")
                btctoken_4 = input("BITCOIN TOKEN (Leave blank to cancel payment): ")
                print("Your Fake ID will be emailed when payment is confirmed.")
                print(Style.RESET_ALL)
                pass

            elif (answer_4 == "TR" or answer_4 == "tr"):
                print(Fore.YELLOW + "You can get your Fake ID after making the payment.")
                print()
                mail_4 = input("TOR MAIL (Leave blank to cancel payment): ")
                btctoken_4 = input("BITCOIN TOKEN (Leave blank to cancel payment): ")
                print("Your Fake ID will be emailed when payment is confirmed.")
                print(Style.RESET_ALL)
                pass

            else:
                print(Fore.RED + "Invalid option")
                print(Style.RESET_ALL)
                pass

    elif (answer == "5"):
        print(Fore.BLUE + """
        _______________________________________________________________
                                         MR.ROBOT
                                       Rent a HACKER
                                       
         A - ATTACK HACKER | Any attack you want | 0,00393 BTC | 1 pc
         D - DEFENSE HACKER | All kinds of defense | 0,00315 BTC | 1 pc
         
         Press 'q' to exit
        _______________________________________________________________
        """)
        print(Style.RESET_ALL)

        while True:
            answer_5 = input("Choose One: ")

            if (answer_5 == "q"):
                print(Fore.YELLOW + "Good Bye")
                print(Style.RESET_ALL)
                time.sleep(1)
                break

            elif (answer_5 == "A" or answer_5 == "a"):
                print(Fore.YELLOW + "You can rent your Hacker after making the payment.")
                print()
                mail_5 = input("TOR MAIL (Leave blank to cancel payment): ")
                btctoken_5 = input("BITCOIN TOKEN (Leave blank to cancel payment): ")
                print("Your rental hacker will be emailed when payment is confirmed.")
                print(Style.RESET_ALL)
                pass

            elif (answer_5 == "D" or answer_5 == "d"):
                print(Fore.YELLOW + "You can rent your Hacker after making the payment.")
                print()
                mail_5 = input("TOR MAIL (Leave blank to cancel payment): ")
                btctoken_5 = input("BITCOIN TOKEN (Leave blank to cancel payment): ")
                print("Your rental hacker will be emailed when payment is confirmed.")
                print(Style.RESET_ALL)
                pass

            else:
                print(Fore.RED + "Invalid option")
                print(Style.RESET_ALL)
                pass

    elif (answer == "6"):
        print(Fore.BLUE + """
        ______________________________________________________________________
                                       DARK STORE
                            Phones, drugs, rental girls and more

         P - PHONE | Any phone you want | 0,00348 BTC | 1 pc
         D - DRUG | Any drug you want | 0,00410 BTC | 1 pc
         RG - RENTAL GIRLS | Rental Girls | 0,00274 BTC | 1 pc
         FT - FAKE TICKETS | Any tickets you want | 0,00111 BTC | 1 pc
         FC - FAKE CARD | Fake card passing anywhere (without balance) | 0,000241 BTC | 1 pc
         C - CREDIT CARD | Balance card | 0,00673 BTC | 1 pc

         Press 'q' to exit
        ______________________________________________________________________
        """)
        print(Style.RESET_ALL)

        while True:
            answer_6 = input("Choose One: ")

            if (answer_6 == "q"):
                print(Fore.YELLOW + "Good Bye")
                print(Style.RESET_ALL)
                time.sleep(1)
                break

            elif (answer_6 == "P" or answer_6 == "p"):
                print(Fore.YELLOW + "You can get your Phone after making the payment.")
                print()
                mail_6 = input("TOR MAIL (Leave blank to cancel payment): ")
                btctoken_6 = input("BITCOIN TOKEN (Leave blank to cancel payment): ")
                print("Your Phone will be emailed when payment is confirmed.")
                print(Style.RESET_ALL)
                pass

            elif (answer_6 == "D" or answer_6 == "d"):
                print(Fore.YELLOW + "You can get your Drug after making the payment.")
                print()
                mail_6 = input("TOR MAIL (Leave blank to cancel payment): ")
                btctoken_6 = input("BITCOIN TOKEN (Leave blank to cancel payment): ")
                print("Your Drug will be emailed when payment is confirmed.")
                print(Style.RESET_ALL)
                pass

            elif (answer_6 == "RG" or answer_6 == "rg"):
                print(Fore.YELLOW + "You can get your Rental Girl after making the payment.")
                print()
                mail_6 = input("TOR MAIL (Leave blank to cancel payment): ")
                btctoken_6 = input("BITCOIN TOKEN (Leave blank to cancel payment): ")
                print("Your Rental Girl will be emailed when payment is confirmed.")
                print(Style.RESET_ALL)
                pass

            elif (answer_6 == "FT" or answer_6 == "ft"):
                print(Fore.YELLOW + "You can get your Fake Ticket after making the payment.")
                print()
                mail_6 = input("TOR MAIL (Leave blank to cancel payment): ")
                btctoken_6 = input("BITCOIN TOKEN (Leave blank to cancel payment): ")
                print("Your Fake Ticket will be emailed when payment is confirmed.")
                print(Style.RESET_ALL)
                pass

            elif (answer_6 == "FC" or answer_6 == "fc"):
                print(Fore.YELLOW + "You can get your Fake Card after making the payment.")
                print()
                mail_6 = input("TOR MAIL (Leave blank to cancel payment): ")
                btctoken_6 = input("BITCOIN TOKEN (Leave blank to cancel payment): ")
                print("Your Fake Card will be emailed when payment is confirmed.")
                print(Style.RESET_ALL)
                pass

            elif (answer_6 == "C" or answer_6 == "c"):
                print(Fore.YELLOW + "You can get your Card after making the payment.")
                print()
                mail_6 = input("TOR MAIL (Leave blank to cancel payment): ")
                btctoken_6 = input("BITCOIN TOKEN (Leave blank to cancel payment): ")
                print("Your Card will be emailed when payment is confirmed.")
                print(Style.RESET_ALL)
                pass

            else:
                print(Fore.RED + "Invalid option")
                print(Style.RESET_ALL)
                pass

    elif (answer == "7"):
        print(Fore.BLUE + """
        _____________________________________________________________________
                                       THE RED ROOM
                                       Just Torture

         L - LOBBY | Only viewers can participate | 0,400000 BTC | 1 pc
         C - COMMANDER | Organizer of torture | 0,600000 BTC | 1 pc
         M - MASTER | Tortures the victim (ability to kill with extra BTC) | 1,500000 BTC | 1 pc
         V - VIP | Online viewing and suggesting torture | 0,200000 BTC | 1 pc

         Press 'q' to exit
        _____________________________________________________________________
        """)
        print(Style.RESET_ALL)

        while True:
            answer_7 = input("Choose One: ")

            if (answer_7 == "q"):
                print(Fore.YELLOW + "Good Bye")
                print(Style.RESET_ALL)
                time.sleep(1)
                break

            elif (answer_7 == "L" or answer_7 == "l"):
                print(Fore.YELLOW + "You can get your Ticket after making the payment.")
                print()
                mail_7 = input("TOR MAIL (Leave blank to cancel payment): ")
                btctoken_7 = input("BITCOIN TOKEN (Leave blank to cancel payment): ")
                print("Your Ticket will be emailed when payment is confirmed.")
                print(Style.RESET_ALL)
                pass

            elif (answer_7 == "C" or answer_7 == "c"):
                print(Fore.YELLOW + "You can get your Ticket after making the payment.")
                print()
                mail_7 = input("TOR MAIL (Leave blank to cancel payment): ")
                btctoken_7 = input("BITCOIN TOKEN (Leave blank to cancel payment): ")
                print("Your Ticket will be emailed when payment is confirmed.")
                print(Style.RESET_ALL)
                pass

            elif (answer_7 == "M" or answer_7 == "m"):
                print(Fore.YELLOW + "You can get your Ticket after making the payment.")
                print()
                mail_7 = input("TOR MAIL (Leave blank to cancel payment): ")
                btctoken_7 = input("BITCOIN TOKEN (Leave blank to cancel payment): ")
                print("Your Ticket will be emailed when payment is confirmed.")
                print(Style.RESET_ALL)
                pass

            elif (answer_7 == "V" or answer_7 == "v"):
                print(Fore.YELLOW + "You can get your Ticket after making the payment.")
                print()
                mail_7 = input("TOR MAIL (Leave blank to cancel payment): ")
                btctoken_7 = input("BITCOIN TOKEN (Leave blank to cancel payment): ")
                print("Your Ticket will be emailed when payment is confirmed.")
                print(Style.RESET_ALL)
                pass

            else:
                print(Fore.RED + "Invalid option")
                print(Style.RESET_ALL)
                pass

    elif (answer == "9"):
        print(Fore.BLUE + "Very Soon")
        print(Style.RESET_ALL)
        pass

    elif (answer == "8"):
        print(Fore.YELLOW + "You can get your Surprise Box after making the payment.")
        print()
        mail_6 = input("TOR MAIL (Leave blank to cancel payment): ")
        btctoken_6 = input("BITCOIN TOKEN (Leave blank to cancel payment): ")
        adress = input("Your Home Adress(Leave blank to cancel payment): ")
        print("Your Surprise Box will be emailed when payment is confirmed.")
        print(Style.RESET_ALL)
        pass

    else:
        print("Invalid option")
        pass
# Written by ottoman505