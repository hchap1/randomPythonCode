import random
import time

alphabet = [":", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", ":", "?", "!", ",", ".", "'", "/", "=", "+", "@", "+", "(", ")", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ";", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
a = ""
print(len(alphabet))


print("Welcome to [Cryptobean V4.2]\n")
keyCompletion = False

time.sleep(1)



a = input("Generate a random key (Y), or enter a set key (N)?\n = ")



key = ""

if a.lower() == "y":
    print("\nOk... generating...\n")

    time.sleep(1)

    for i in range(32):
        key += alphabet[random.randint(0,len(alphabet) - 1)]
        

    print("\nKEY:\n" + key)


else:

    while keyCompletion == False:

        key = input("Please enter a valid, 256 bit, (32 CHAR) encryption key.\n = ")
        #key = "y9@nsfgo8sxxputh97euny82kc7dzelu"

        if len(key) > 32 or len(key) < 32:
            print("INVALID KEY: Must be 32 characters.")

            time.sleep(1)

        else:
            keyCompletion = True


    

def encrypt(key,message):

    keyVal = 0
    keyIndex = []
    messageIndex = []
    encryptedIndex = []
    encryptedString = ""

    for i in key:
        
        keyIndex.append(alphabet.index(i))
        keyVal += alphabet.index(i)

        
            

    for i in message:
        messageIndex.append(alphabet.index(i))

    for i in messageIndex:

        rand = random.randint(0,len(key)-1)

        randKey = keyIndex[rand]
        
        temp = int(i)
        
        

        temp = temp * randKey



        encryptedIndex.append(str(int(temp)))
        encryptedIndex.append("|")
        encryptedIndex.append(str(int(rand*keyVal)))
        encryptedIndex.append(":")
                              

    for i in encryptedIndex:
        encryptedString += i

    return encryptedString
        
def decrypt(key,message):

    devMode = input("DevMode? (y/n)\n = ")

    if devMode.lower() == "y":
        devMode = True

    elif devMode.lower() == "n":
        devMode = False

    else:
        print("\nYou entered an invalid answer. DevMod has been defaulted to (OFF)\n")


    keyVal = 0
    keyIndex = []
    messageIndex = []
    decryptedIndex = []
    decryptedString = ""
    randomIndex = []
    thing = []
    temp = ""

    for i in key:
        keyIndex.append(alphabet.index(i))
        keyVal += alphabet.index(i)

    messageIndex = message.split(":")

    for i in range(len(messageIndex) - 1):
        
        temp = messageIndex[i].split("|")
        if devMode:

            print(temp)
            time.sleep(0.2)
            print("Calculating...")

        thing.append(temp[0])
        randomIndex.append(temp[1])
        

    for i in range(len(thing)):
        rand = int(randomIndex[int(i)])
        rand = rand / keyVal
        
        randKey = int(keyIndex[int(rand)])

        temp = thing[i]
        
        temp = int(temp) / int(randKey)
        
        decryptedIndex.append((alphabet[int(temp)]))
    

    for i in decryptedIndex:
        decryptedString += i

    return str(decryptedString)

    
    
    
    

while True:
    if True:
    #try:
        task = input("Encrypt (E), or Decrypt (D)?\n = ")

        if task.lower() == "e":
            print("\nYou've chosen encrypt.\n")
            message = input("What do you want to encrypt?\n = ")

            print(encrypt(key,message))

        if task.lower() == "d":
            print("\nYou've chosen decrypt.\n")
            message = input("What do you want to decrypt?\n = ")

            print(decrypt(key,message))

    #except:
        #print("FATAL ERROR")
        

