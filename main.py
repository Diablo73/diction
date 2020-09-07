import json, requests
from difflib import get_close_matches as gcm
from colorama import Fore, Back, Style

print(Back.BLUE + Fore.WHITE + "DICTIONARY" + Style.RESET_ALL)
print("(press enter to exit)\n")

def enter():
    print()
    word = "`"
    while True:
        word = input("Enter your search word: ")
        op = defi(word)
        if word == "":
            if input(Back.BLACK + Fore.RED + "EXIT!?!?" + Style.RESET_ALL + " Press enter again to end.") == "":
                break
        elif type(op) == list:
            i = 1
            print()
            print(Back.GREEN + Fore.WHITE + op[0].title() + Style.RESET_ALL)
            if type(op[1]) == list:
                for j in op[1]:
                    print(i, " -> ", j)
                    i += 1
            else:
                print(op[1])
        else:
            print(op)
        print()

def defi(w):
    w = w.lower()
    if w in dat:
        return [w, dat[w]]
    elif len(gcm(w, dat.keys(), n=3, cutoff=0.75)) > 0:
        i = 0
        l = gcm(w, dat.keys(), n=3, cutoff=0.75)
        print("Enter Y(y) if yes or N(n) if no.")
        while i < len(l):
            yn = input("Did you mean '%s' instead?: " %l[i])
            if yn == "Y" or yn == "y":
                return [l[i], dat[l[i]]]
            elif yn == "N" or yn == "n":
                i += 1
        return Back.RED + Fore.WHITE + w + Style.RESET_ALL + " ain't in my dictionary."
    else:
        return "Is " + Back.YELLOW + Fore.WHITE + w + Style.RESET_ALL + " a real word? Please double check it."


while True:
    lev = input("Select the level of DICTIONARY (Enter 1 or 2): ")
    if lev == "1":
        dat = json.load(open("dict.json"))
        enter()
        break
    elif lev == "2":
        r = requests.get("https://raw.githubusercontent.com/matthewreagan/WebstersEnglishDictionary/master/dictionary.json")
        dat = r.json()
        enter()
        break
    elif lev == "":
        if input(Back.BLACK + Fore.RED + "EXIT!?!?" + Style.RESET_ALL + " Press enter again to end.") == "":
            break
print()

print(Back.WHITE + Fore.BLACK + "END" + Style.RESET_ALL)