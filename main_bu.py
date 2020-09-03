import json, requests
from difflib import get_close_matches as gcm

print("DICTIONARY\n(press enter to exit)\n")

while True:
    lev = input("Select the level of DICTIONARY (Enter 1 or 2): ")
    if lev == "1":
        dat = json.load(open("dict.json"))
        break
    elif lev == "2":
        r = requests.get("https://raw.githubusercontent.com/matthewreagan/WebstersEnglishDictionary/master/dictionary.json")
        dat = r.json()
        break
    else:
        print("Please enter either '1' or '2'")
print()

def defi(w):
    global word
    w = w.lower()
    if w in dat:
        return dat[w]
    elif len(gcm(w, dat.keys(), n=3, cutoff=0.75)) > 0:
        i = 0
        l = gcm(w, dat.keys(), n=3, cutoff=0.75)
        print("Enter Y(y) if yes or N(n) if no.")
        while i < len(l):
            yn = input("Did you mean '%s' instead?: " %l[i])
            if yn == "Y" or yn == "y":
                word = l[i]
                return dat[word]
            elif yn == "N" or yn == "n":
                i += 1
        return "'%s' ain't in my dictionary." %w
    else:
        return "Is '%s' a real word? Please double check it." %w


word = "`"
while True:
    word = input("Enter your search word: ")
    op = defi(word)
    if word == "":
        if input("Press enter again to end: ") == "":
            break
    elif type(op) == list:
        i = 1
        print()
        print(word.title())
        for j in op:
            print(i, " -> ", j)
            i += 1
    else:
        print(op)
    print()

print("END")
