import re
from colorama import Fore,Style,init

init(autoreset=True)

def check_pass(password):
        length=len(password)>=8
        upper=bool(re.search(r'[A-Z]',password))
        lower=bool(re.search(r'[a-z]',password))
        digit=bool(re.search(r'\d',password))
        special=bool(re.search(r'[!@#$%^&*(),.?":{}|<>]',password))

        score=sum([length,upper,lower,digit,special])

        if score<=2:
                return "Weak", Fore.RED
        elif score==3 or score ==4:
                return "Moderate", Fore.YELLOW
        else:
                return "Strong", Fore.GREEN

def main():
        print(Fore.CYAN + "Password Strength Checker")
        print(Style.DIM + "--------------------------------------")

        while True:
                password = input("\nEnter a password to check (or type 'exit' to quit): ")
        
        
                if password.lower() == 'exit':
                    print(Fore.MAGENTA + "Exiting Password Strength Checker. Goodbye!")
                    break

                #if password==' ':
                 #       print(Fore.YELLOW+"Password cannot be empty. Try again."
                  #      continue
                
                strength, color = check_pass(password)
                print(f"Password strength: {color}{strength}")
        

if __name__ =="__main__":
        main()
        input("\nPress Enter to exit...")
