import requests

def checkIfBought(uuid):

    data = requests.get("https://api.hypixel.net/skyblock/auctions_ended").json()["auctions"]

    for i in data:

        if i["seller"] == uuid:

            sellerName = "ANONYMOUS"

            buyerData = requests.get("https://api.mojang.com/user/profiles/%s/names" % i["buyer"]).json()

            for i in buyerData:

                sellerName = i["name"]

            print("Your auction has sold for %s to %s!" % (i["price"], sellerName))

            return True

        else:

            False

    return False

def findUuid(username):


    try:

        data = requests.get("https://api.mojang.com/users/profiles/minecraft/%s" % username).json()

        return data["id"]

    except:

        print("INVALID USERNAME!\n")

        return False

uuid = findUuid("TimeParadox_")

while True:

    if checkIfBought(uuid):

        break

print("END")


    


