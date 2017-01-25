def removeChar(string, idx):
    return string[:idx] + string[idx+1:]
def keyGen():
    import random
    alphabet = 'abcdefghijklmnopqrstuvwxyz '
    key = ""
    for i in range(len(alphabet)):
        ch = random.randint(0,26-i)
        key += alphabet[ch]
        alphabet = removeChar(alphabet,ch)
    return key

#CipherAlphabet = keyGen()
alphabet = "abcdefghijklmnopqrstuvwxyz "

def SubEncryption(string):
    CipherText = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    string = string.lower()
    for ch in string:
        idx = alphabet.find(ch)
        CipherText += CipherAlphabet[idx]
    return CipherText
#print(SubEncryption("the lazy student never gets paid."))

def SubDecyrption(CipherText2):
    string2 = ""
    for ch in CipherText2:
        idx = CipherAlphabet.find(ch)
        string2 += alphabet[idx]
    return string2
print(SubDecyrption(" lyzerptzm wgyn znyxykziy mzsrugz"))
