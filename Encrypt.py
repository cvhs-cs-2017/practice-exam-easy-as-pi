"""Write a code that will take (AnyString) and substitute all vowels with
character's like $#%^&* etc..... but DO NOT USE ' or " as any of your characters."""

def SubVowels(AnyString):
    CipherText = ""
    CipherSub = "$#%^&"
    anyString = AnyString.lower()
    for ch in AnyString:
        if ch == "a":
            ch = CipherSub[0]
            CipherText += ch
        elif ch == "e":
            ch = CipherSub[1]
            CipherText += ch
        elif ch == "i":
            ch = CipherSub[2]
            CipherText += ch
        elif ch == "o":
            ch = CipherSub[3]
            CipherText += ch
        elif ch == "u":
            ch = CipherSub[4]
            CipherText += ch
        else:
            CipherText += ch
    return CipherText

print(SubVowels("The Quick Brown Fox Jumped Over The Lazy Dog."))
