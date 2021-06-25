print("To encode a message enter 1.")
print("To decode a message enter 2.")
print("To quit enter any key other than 1 and 2")
choice = input("Enter your choice: ")

#caesar's cipher
#left shift 4
shift = 4

def encode(shift, name, newFName):
    f = open(name, "r")
    ciphermessage = f.read().strip()
    #encrypt the message
    encoded = ""
    for i in range(len(ciphermessage)):
        letter = ord(ciphermessage[i])+ shift
        encoded += chr(letter)

    #create newfile and write the decoded message to it
    fnew = open(newFName, "w")
    fnew.write(encoded)
    f.close()
    fnew.close()
    return

def decode(shift, name, newFName):
    f = open(name, "r")
    ciphermessage = f.read().strip()
    #decode the message
    decoded = ""
    for i in range(len(ciphermessage)):
        letter = ord(ciphermessage[i])- shift
        decoded += chr(letter)
    #create newfile and write the encoded message to it
    fnew = open(newFName, "w")
    fnew.write(decoded)
    f.close()
    fnew.close()
    return

def atbash(name, newFName):
    en = {"a":"z","b":"y","c":"x","d":"w","e":"v","f":"u","g":"t","h":"s","i":"r","j":"q",
           "k":"p","l":"o","m":"n","n":"m","o":"l","p":"k","q":"j","r":"i","s":"h","t":"g",
           "u":"f","v":"e","w":"d","x":"c","y":"b","z":"a"}

    f = open(name, "r")
    ciphermessage = f.read().strip()
    coded = ""
    for i in range(len(ciphermessage)):
        # HELLO
        #hello
        if ciphermessage[i].isupper():
            letter = ciphermessage[i].lower()
            letter = en.get(letter) #s
            coded += letter.upper() # adding S
        elif ciphermessage[i].islower():
            letter = en[ciphermessage[i]]
            coded += letter

        else:
            coded += ciphermessage[i]

    fnew = open(newFName, "w")
    fnew.write(coded)
    f.close()
    fnew.close()
    return

def morseEn(name, newFName):
    MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ',':'--..--', '.':'.-.-.-', '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

    f = open(name, "r")
    ciphermessage = f.read().strip()
    encoded = ""
    #HELLO
    for i in range(len(message)):
        if ciphermessage[i].islower():
            letter = MORSE_CODE_DICT.get(ciphermessage[i].upper())
            encoded += letter + ' '
        elif ciphermessage[i] == ' ':
            encoded += '  '
        else:
            letter = MORSE_CODE_DICT.get(ciphermessage[i])
            encoded += letter + ' '

    fnew = open(newFName, "w")
    fnew.write(encoded)
    fnew.close()
    f.close()
    return


if(choice == "1"):
    #enter file name with message
    name = input("Enter the file name: ")
    #enter file name to create file to put message into
    newFName = input("Enter new file name to save message to: ")
    #encode(shift, name, newFName)
    #atbash(name,newFName)
    morseEn(name, newFName)


elif(choice=="2"):
    #enter file name with message
    name = input("Enter the file name: ")
    #enter file name to create file to put message into
    newFName = input("Enter new file name to save message to: ")
    decode(shift, name, newFName)
    atbash(name,newFName)

else:
    print("Why'd you even run this.")
