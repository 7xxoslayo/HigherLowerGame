import random
import colorama
from colorama import Back, Fore, Style
colorama.init(autoreset=True)

print(f"""
{Fore.YELLOW}  ___ ___ .__       .__                   {Fore.GREEN}.____                               
{Fore.YELLOW} /   |   \|__| ____ |  |__   ___________  {Fore.GREEN}|    |    ______  _  __ ___________ 
{Fore.YELLOW}/    ~    \  |/ ___\|  |  \_/ __ \_  __ \\ {Fore.GREEN}|    |   /  _ \ \/ \/ // __ \_  __ \\
{Fore.YELLOW}\    Y    /  / /_/  >   Y  \  ___/|  | \/ {Fore.GREEN}|    |__(  <_> )     /\  ___/|  | \/
{Fore.YELLOW} \___|_  /|__\___  /|___|  /\___  >__|    {Fore.GREEN}|_______ \____/ \/\_/  \___  |__| 
{Fore.YELLOW}            /_____/                       {Fore.GREEN}
{Style.RESET_ALL}{Style.BRIGHT}  ________                       
 /  _____/_____    _____   ____  
/   \  ___\__  \  /     \_/ __ \\ 
\\    \_\  \/ __ \|  Y Y  \  ___/ 
 \______  (____  /__|_|  /\___  >


                                                {Fore.MAGENTA}By 7xxoslayo
""")

num = random.randint(1, 100)
#This is an awnser so if you want to see the awnsers just remove the hashtag below<3
#print(num)

while True:
    guess = int(input('Enter guess: '))
    if guess == num:
        print(Fore.LIGHTGREEN_EX + 'You got it!')
        break
    elif guess != num and num > guess:
        print(Fore.YELLOW + "Higher")
    elif guess != num and num < guess:
        print(Fore.GREEN + "lower")
    if guess > 100:
        print("Bro, Stop")


