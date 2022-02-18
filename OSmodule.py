import os

sep = r"/"

path = r"C:/Users/hchap/OneDrive/DOCUMENTS"

temp = os.listdir(path)

for i in temp:

    if i.lower() == "valuableinformation":

        path += sep

        path += i

        temp = os.listdir(path)

        tempPath = path

        for i in temp:

            tempPath += sep

            tempPath += temp[0]

            with open(tempPath, "r") as file:

                print("Path: " + tempPath)

                removedText = file.readlines()
                
                print(str(removedText).strip("[]'"))

                action = input("\nWould you like to (W)ipe this .txt document?\n = ")

                if action.lower()[:1] == "w":

                    file.close()

                    with open(tempPath, "w") as file:

                        file.write("This information has been WIPED!")

                        action = input("\nThe information has been wiped. Would you like to (R)estore it?\n = ")

                        if action.lower()[:1] == "r":

                            file.write(str(removedText))

                            print("The information (LOOK BELOW) has been restored.\n" + str(removedText))

                        

                

            
                
           
