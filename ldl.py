import pygame
import time
from colorama import Fore, Style, init


init(autoreset=True)


pygame.mixer.init()
pygame.mixer.music.load("ldfinal.mp3")  
pygame.mixer.music.play()

time.sleep(1)


lyrics = [
    ("Jodi Biroho Thake, Amio Thaki.", 3),
    ("Ke Bolo Shesh Hobe Age?", 3.7),
    ("Keno Je Eto Bhalobasha More Jay?", 3.8),
    ("Shudhu Shomoy Mone Rakhe.", 3.8), 
    ("",0),
    ("Eto Shunnota, E Mone Rakhi Je Ami.", 3.4),
    ("Dekhe Na Keu To Ar, Bole Eshob-I Paglami.", 3.89),
    ("Kate Na Jamini, Biroho Jeno Kete Jay.", 3.99),
    ("Thame Na Borsha, Tomare Daki Je Ami", 3.6),
    ("Ar", 2),
    ("Shey Thake Kar Voroshay?",2.3),
]

print(Fore.CYAN + "\nLong Distance Love by Coke Studio Bangla 🤍\n")


for line, total_delay in lyrics:
    num_chars = len(line)
    char_delay = total_delay / max(num_chars, 1)  

    for char in line:
        print(Fore.YELLOW + Style.BRIGHT + char, end="", flush=True)
        time.sleep(char_delay)
    print()  
    time.sleep(0.4) 

while pygame.mixer.music.get_busy():
    time.sleep(1)


 