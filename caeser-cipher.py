def get_cipherletter(new_key, letter):
    #still need alpha to find letters
    alphaUpper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphaLower = "abcdefghijklmnopqrstuvwxyz"
    if letter in alphaUpper:
        return alphaUpper[new_key]
    elif letter in alphaLower:
        return alphaLower[new_key]
    else:
        return letter

def encrypt(key, message):
    alphaUpper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphaLower = "abcdefghijklmnopqrstuvwxyz"    
    result = ""

    for letter in message:
        if letter.isupper():
            new_key = (alphaUpper.find(letter) + key) % len(alphaUpper)
            result = result + get_cipherletter(new_key, letter)
        else :
            new_key = (alphaLower.find(letter) + key) % len(alphaLower)
            result = result + get_cipherletter(new_key, letter)

    return result

def decrypt(key, message):
    alphaUpper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphaLower = "abcdefghijklmnopqrstuvwxyz"    
    result = ""

    for letter in message:
        if letter.isupper():
            new_key = (alphaUpper.find(letter) - key) % len(alphaUpper)
            result = result + get_cipherletter(new_key, letter)
        else :
            new_key = (alphaLower.find(letter) - key) % len(alphaLower)
            result = result + get_cipherletter(new_key, letter)

    return result

operation = input("Enter 'e' to encrypt a message and 'd' to decrypt a message: ")

if (operation == 'e'):
    message = input("Enter the message to encrypt: ")
    key = int(input("Enter the shift value: "))
    print ("Text  : " + message )
    print ("Shift : " + str(key) )
    print("Cipher: " + encrypt(key, message))
else :
    message = input("Enter the message to decrypt: ")
    key = int(input("Enter the shift value: "))
    print ("Text  : " + message )
    print ("Shift : " + str(key) )
    print("Cipher: " + decrypt(key, message))