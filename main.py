print("Welcome to the TRANSPOSITION cipher.\n")

import encrypt, decrypt, pyperclip, sys

key = False

while True:

    if True:
    #try:

        action = input("(E)ncrypt,(D)ecrypt,(N)ew key,(R)ead text?\n = ")

        if action.lower()[:1] == "e" or action.lower()[:1] == "d":

            if not key == False:
        
                if action.lower()[:1] == "e":

                    message = input("\nWhat do you want to encrypt?\n = ")

                    encryptedMessage = encrypt.encryptMessage(key,message)

                    print("\nYour encrypted message:\n" + encryptedMessage + "|")

                elif action.lower()[:1] == "d":

                    message = input("\nWhat do you want to decrypt?\n = ")

                    decryptedMessage = decrypt.decryptMessage(key,message)

                    print("\nYour decrypted message is:\n" + decryptedMessage + "|")

            else:

                print("\nYou need a key first! (N) instead, to enter a new key!\n")

        if action.lower()[:1] == "n":

            completed = False

            while not completed:

                key = int(input("What is the key?\n = "))

                action = input(str(key) + " is the new key. Is this (C)orrect or (I)ncorrect?\n = ")

                if action.lower()[:1] == "c":

                    completed = True

                else:

                    completed = False

        if action.lower()[:1] == "r":


            with open("textFile.txt",'r') as f:
                lines = f.readlines()

                action = input("\n(E)ncrypt the file, (D)ecrypt the file, or (R)ead it?\n = ")

                if action.lower()[:1] == "e":

                    print("\n")

                    lines = str(lines)

                    lines = " ".join(lines.split()).strip("[]'")

                    encryptedMessage = encrypt.encryptMessage(key,lines)

                    f.close()

                    with open("textFile.txt","wt") as f:

                        f.write(encryptedMessage)

                elif action.lower()[:1] == "d":

                    print("\n")

                    lines = str(lines)

                    lines = " ".join(lines.split()).strip("[]'")

                    decryptedMessage = decrypt.decryptMessage(key,lines)

                    f.close()

                    with open("textFile.txt","wt") as f:

                        f.write(decryptedMessage)
                

    #except:

        #print("\nSomething went wrong. You most likely entered a string/float into an integer input, such as the key.\n")
        

        
