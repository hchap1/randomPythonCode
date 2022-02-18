
import random, math, sys, time

bulletCount = 10

money = 0

bulletType = "normal"

types = ["normal", "untraceable", "self-aiming"]

def clear():

    for i in range(100):
        print("\n")

    print("    --    --    --")
    print("   /  \  /  \  /  \ ")
    print("  / <> \/ <> \/ <> \ ")
    print("  \    /\    /\    / ")
    print("   ~~~~  ~~~~  ~~~~")
    print("\nRANDOM MURDER\n")
    print("Swiss bank account: $%s\n" % money)

    for i in range(10):
        print("\n")

    print("NEXT CRIME SCENE... who will it be?\n")


def rng(chance):

    if random.randint(0,100) <= chance:

        return True

    else:

        return False

def nameGen(gender):

    randNamesFB = [
        "John",
        "Jack",
        "Tim",
        "Dave",
        "Ralph",
        "Dick",
        "Tobias",
        "Riley",
        "Tom",
        "Jim",
        "Gibbs",
        "Robert",
        "Gavin",
        "Gale",
        "Chang",
        "Sugin",
        "Bruce",
        "Ollie",
        "Dean",
        "Shawn",
        "Max",
        "Sean"
        ]

    randNamesFG = [
        "Angelina",
        "Charlotte",
        "Bean-soup",
        "Chonk-burger",
        "Amelia",
        "Isabelle",
        "Josephine",
        "Harriet",
        "Julia",
        "Julie",
        "Aleta",
        "Jade",
        "Sienna",
        "Elizabeth",
        "Yuran",
        "Hotel",
        "Emma",
        "Alice",
        "Kiera",
        "Kate",
        "Caitlin"
        ]

    randNamesLA = [
        "Anderson",
        "Burgess",
        "Yournan",
        "Stevenson",
        "Smith",
        "Holderson",
        "Corn",
        "Thiccpig",
        "Chong",
        "Ching",
        "Robertson",
        "Turing",
        "Einstein",
        "Barvger",
        "Bahr",
        "Esahyson",
        "Sawyer",
        "Diapernuts",
        "Agrociate",
        "Squisheied", 
        "Doddly",
        "Diddy",
        "Happyface"
        ]

    if gender.lower() == "male":

        name = randNamesFB[random.randint(0,len(randNamesFB) - 1)] + " " + randNamesLA[random.randint(0,len(randNamesLA) - 1)]

    elif gender.lower() == "female":

        name = randNamesFG[random.randint(0,len(randNamesFG) - 1)] + " " + randNamesLA[random.randint(0,len(randNamesLA) - 1)]

    return name

def generateCrimeScene(victimGender):

    crimeScenes = [
        "Amusement park",
        "Wharf",
        "Church",
        "Police-station",
        "Eifel Tower",
        "London sugar-fest",
        "Mt. Everest",
        "Chess club",
        "Beach",
        "Ballet studio",
        "Food stall",
        "Supermarket",
        "Secret island base",
        "Bunker",
        "White-house toilets",
        "School playground",
        "Brother's house",
        "Empire State Building",
        "Power lines",
        "Bus-stop",
        "Art studio",
        "Third floor of dungeons",
        "Highway",
        "Helicopter",
        "Military base",
        "Tomato farm",
        "Festival",
        "Drug lab",
        "Dad's office",
        "Headquaters of Beijing corn"
    ]

    target = [
        "my ice-cream",
        "my dog",
        "my kittens",
        "my balls",
        "my nipples",
        "my shirt",
        "my computer",
        "my business",
        "my chair",
        "my eyes",
        "my oral-cavity",
        "my mum",
        "my car",
        "my house",
        "my bike",
        "my tire",
        "my bed",
        "my SANITY",
        "my life",
        "my plane",
        "my stomach",
        "my liver",
        "my balls",
        "my pet rock",
        "my gaming mouse",
        "my ethernet cables",
        "my quad-bike",
        "my farming tool",
        "my wife",
        "my dad",
        "my highly esteemed job as a midwife",
        "the inspectors in my basment",
        "my sausages",
        "dinner",
        "my father",
        "my other father",
        "my lego",
        "my power button",
        "my skin"
        ]

    actions = [
        "stomped",
        "licked",
        "ate",
        "tickled",
        "broke",
        "googled",
        "delved into",
        "deviled",
        "took",
        "stole",
        "devoured",
        "yoinked",
        "bonked",
        "drank",
        "slurped",
        "consumed",
        "yeeted",
        "kicked",
        "punched",
        "slapped"
        ]

    if victimGender == "male":

        pronoun = "he"

    else:

        pronoun = "she"
    
    sentence = "I followed " + nameGen(victimGender) + " to the " + crimeScenes[random.randint(0,len(crimeScenes) - 1)] + " because " + pronoun +  " " + actions[random.randint(0,len(actions) - 1)] + " " + target[random.randint(0,len(target) - 1)] + "!"

    return sentence

while True:

    clear()

    if random.randint(0,1) == 1:

        genderPicked = "male"

    else:

        genderPicked = "female"

    print(generateCrimeScene(genderPicked) + "\n")

    chanceToBeCaught = random.randint(0,20)

    reward = random.randint(5,15)

    if random.randint(0,1) == 1:

        genderToUse = "male"

    else:

        genderToUse = "female"

    print("When you murder them, you have a %s%s chance of being caught, and will be paid $%s by %s" % (chanceToBeCaught, "%", reward, nameGen("male")))

    print("\nYou currently have $%s!" % money)

    action = input("\nPurchase: (U)ntraceable bullets $10 (1/4 chance to get caught), (S)self-aiming bullets $10, (M)urder them, (Q)uit, (S)kip ($10)?\n = ")

    print("\n")

    if action.lower() == "s":

        if money >= 10:

            money -= 10

            bulletType = "self-aiming"

            action = "m"

        else:

            print("You cannot afford this!\n")

    if action.lower() == "u":

        if money >= 10:

            money -= 10

            bulletType = "untraceable"

            action = "m"

        else:

            print("You cannot afford this!\n")

    bulletCount = 10

    if action.lower() == "m":

        hit = False

        while hit == False:

            input("ENTER TO FIRE! You have %s bullets!" % bulletCount)

            print("\nYou take the shot...\n")

            if bulletType == "self-aiming":

                print("Since you were using self-aiming bullets, you hit the shot!\n")

                hit = True

            else:

                if rng(69):

                    print("Tssk, tssk, tssk. You missed!\n")

                    bulletCount -= 1

                else:

                    print("You hit the target after %s shots!\n" % (10 - bulletCount + 1))

                    hit = True

        print("\nThe target has been eliminated. If you can get out of the crimescence, you'll be able to collect the dough.\n")
                    
        if bulletType != "untraceable":

            print("Your bullet stays in the target... Hopefully the police can't match it!\n")

            if rng(chanceToBeCaught):

                print("\nYou've been caught! Game over!\n")

                sys.exit("FAILURE: The police took you, crunched your balls, and left you rotting in a cell for the rest of your life. Should have used untraceable bullets!")

        else:

            print("\nYour untraceable bullet disolves in the corpse, leaving no evidence.\n")

            if rng(round(chanceToBeCaught/4)):

                print("\nYou still got caught... FAILURE\n")

                sys.exit("FAILURE: Despite the untraceable bullets, you still got caught. I guess you're losing your touch, eh? The police left you to rot in a cell for the rest of your miserable life.\n")

        money += reward

        randMessages = ["You collect the dough", "You swipe the money", "Your payment has been fufilled", "Time to go open a Swiss bank"]

        print(randMessages[random.randint(0,len(randMessages) - 1)] + " of $%s" % reward)

        print("ONTO THE NEXT JOB!")

        input("Hit ENTER to receive a new Job.\n\nAWAITING APPROVAL")

        

            

            

            

    
        
        
                                                                                 
        





    
