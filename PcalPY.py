#This is a percentage calculator
import time
import colorama
from colorama import Fore, Back, Style
colorama.init()
print(Fore.LIGHTGREEN_EX)

print(''' ██▓███   ▄████▄   ▄▄▄       ██▓     ██▓███ ▓██   ██▓
▓██░  ██▒▒██▀ ▀█  ▒████▄    ▓██▒    ▓██░  ██▒▒██  ██▒
▓██░ ██▓▒▒▓█    ▄ ▒██  ▀█▄  ▒██░    ▓██░ ██▓▒ ▒██ ██░
▒██▄█▓▒ ▒▒▓▓▄ ▄██▒░██▄▄▄▄██ ▒██░    ▒██▄█▓▒ ▒ ░ ▐██▓░
▒██▒ ░  ░▒ ▓███▀ ░ ▓█   ▓██▒░██████▒▒██▒ ░  ░ ░ ██▒▓░
▒▓▒░ ░  ░░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░▓  ░▒▓▒░ ░  ░  ██▒▒▒ 
░▒ ░       ░  ▒     ▒   ▒▒ ░░ ░ ▒  ░░▒ ░     ▓██ ░▒░ 
░░       ░          ░   ▒     ░ ░   ░░       ▒ ▒ ░░  
         ░ ░            ░  ░    ░  ░         ░ ░     
         ░                                   ░ ░     
''')
print("Tool Name: Pcalpy")
print("Version: 1.0.0")
print("License : LS MARTIN")



print(Fore.LIGHTRED_EX)
#Options Section
print("[-]Press 1 To Find Percentage")
print("[-]Press 2 To Find Total Number")
print("[-]Press 3 To Find Number")
print("[-]Enter 4 To Exit")
time.sleep(1)
#What to find:
print("                                                                           ")


q = int(input("[ - ] Enter Choice: "))
# a = Your marks 
# b = total marks 
# p = Percentage
if q==1:
    a = int(input("Enter Your Marks: "))
    b = int(input("Enter Total Marks: "))
    p = (a*100/b)
    print("Your Percentagae is:",p)

elif q==2:
    p = int(input("Enter Your Percetage: "))
    a = int(input("Enter Your Marks: "))
    b = (a*100/p)
    print("Total Marks is: ",b)

elif q==3:
    p = int(input("Enter Your Percetage: "))
    b = int(input("Enter Total Marks: "))
    a = (p*b/100)
    print("Your Marks is: ",a)

elif q==4:
    time.sleep(1)
    print(Fore.LIGHTGREEN_EX)
    print("Thanks For using this Tool")
    print("This tool will be developed Further")
    time.sleep(4)
    exit()
else:
    print("Invalid Input")



time.sleep(2)

#Outro Section
print(Fore.MAGENTA)
print("Thanks For using this Tool")
print("This tool will be developed Further")
time.sleep(5)





