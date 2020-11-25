import sys

def rot(text,key=13):
    abc = "abcdefghijklmnopqrstuvwxyz"
    translated = ""
    for c in text:
        if c in abc:
            translated += abc[(abc.find(c)+key)%26]
        elif c in abc.upper():
            translated += abc.upper()[(abc.upper().find(c)+key)%26]
        else:
            translated += c 
    return translated
    
if __name__ == "__main__":
    args = sys.argv

    if len(args) == 1: # if the user forgot to add arguments
        print("example call: python rot.py <path to file> <key> \nthe key is optional, defualts to 13")
        sys.exit()
    
    path = args[1]
    text = open(path,"rt").read()
    
    if len(args) == 3:
        key = int(str(args[2]))
    
        print(rot(text,key))
    else:
        print(rot(text))

    

    
