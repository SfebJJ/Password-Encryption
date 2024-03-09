import string

''' 
DATA
    __all__ = ['ascii_letters', 'ascii_lowercase', 'ascii_uppercase', 'cap...
    ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    hexdigits = '0123456789abcdefABCDEF'
    octdigits = '01234567'
    printable = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    whitespace = ' \t\n\r\x0b\x0c'
'''

# Choose the encrption standard to use
def encrpytion_standard(argument: int) -> str:
    switcher = {
        0: string.ascii_lowercase,
        1: string.ascii_letters,
        2: string.printable
    }
    return switcher.get(argument, "nothing - try different input")

# Each character increment by 1 with count (maybe make it so that lower case wraps around lower case instead of going to uppercase for standard 1+)
def encrypt_ver1(phrase: str, encryptList: str) -> str:
    encrypted_phrase = ""
    for i in range(len(phrase)):
        phrase_character_index = encryptList.rfind(phrase[i])
        encrypted_phrase += encryptList[(phrase_character_index+i+1) % len(encryptList)]
    
    return encrypted_phrase

# Each character equally increment by 1
def encrypt_ver2(phrase: str, encryptList: str) -> str:
    encrypted_phrase = ""
    for i in range(len(phrase)):
        phrase_character_index = encryptList.rfind(phrase[i])
        encrypted_phrase += encryptList[(phrase_character_index+1) % len(encryptList)]
    
    return encrypted_phrase

encryptList = encrpytion_standard(2)
inputPhrase = "Jacky" # input("Phrase: ")
encrypted_phrase = encrypt_ver1(inputPhrase, encryptList)
print(encrypted_phrase)
encrypted_phrase = encrypt_ver2(inputPhrase, encryptList)
print(encrypted_phrase)