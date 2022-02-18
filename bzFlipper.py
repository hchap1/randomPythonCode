import requests
import json
import math
import random



errorcode = [
  "ERROR",
  "Hmm... You need at least 5000 to invest!",
  "Please enter (Y/N)",
  " has no readable orders.",
]

responsecode = [
  "The current item with the highest profit margins, based off of entered information, is "
]

def findProducts(minPrice, maxPrice, budget):
    data = requests.get("https://api.hypixel.net/skyblock/bazaar")



    productList = data.json()["products"]

    eligible = []
    
    for i in productList:
        x = productList[i]
        y = x["product_id"]
        z = x["sell_summary"]

        try:
            topBuyOrder = z[0]
            topBuy = topBuyOrder["pricePerUnit"]
            if topBuy >= minPrice and topBuy <= maxPrice:
                eligible.append(i)

        except:
            print("\n")

    bestProfit = [0,"Product ID","Qty","Cost","Cost per item","Sell per item"]
 

    for i in eligible:
      
        x = productList[i]
        y = x["product_id"]
        buyOrders = x["sell_summary"]
        sellOrders = x["buy_summary"]
        quickStat = x["quick_status"]
        amountOfBuy = quickStat["buyOrders"] 
        amountOfSell = quickStat["sellOrders"]
        boughtInWeek = quickStat["buyMovingWeek"]
        soldInWeek = quickStat["sellMovingWeek"]
        
        try:
            topBuyOrder = buyOrders[0]
            topSellOrder = sellOrders[0]
            topBuyOrderPrice = topBuyOrder["pricePerUnit"]
            topSellOrderPrice = topSellOrder["pricePerUnit"]
            spentInWeek = boughtInWeek * ((topBuyOrderPrice + topSellOrderPrice) / 2)
            
            qty = math.floor(budget / (topBuyOrderPrice + 0.1))
            profitPer = (topSellOrderPrice - 0.1) - (topBuyOrderPrice + 0.1)
            profit = profitPer * qty

            if profit > bestProfit[0] and amountOfBuy > 150 and amountOfSell > 100 and spentInWeek > 300000000:
              
              bestProfit[0] = profit
              bestProfit[1] = str(y)
              bestProfit[2] = str(qty)
              bestProfit[3] = str(qty * (topBuyOrderPrice + 0.1))
              bestProfit[4] = str(topBuyOrderPrice + 0.1)
              bestProfit[5] = str(topSellOrderPrice - 0.1)
  
              
            
        except:
            print("No orders for " + i["product_id"])
    return bestProfit

keys = [
"bazaar",
"hamburger",
"legoman",
"abcdef",
"gronk"
]

print("Welcome to TimeParadoz_'s bazaar flipping program. The min price is the min price PER ITEM. So, put 5 coins if you are not sure. Max price doesn't matter, it's an advanced feature. Just put like 10000. Make sure to actually type the digits, not putting 'k'. Bidget is the money you want to spend, so put how much you have in your purse. Put n for bean and response, they are for my friend. Then, hit enter. Assuming you entered the data correctly, it'll give you prices. Then, hit 'y', and then enter to refresh the prices. Happy flipping!")

while True:
  try:
    print("For the next three run-questions, enter valid integers.")
    a = int(input("What is the minimum price per item?"))
    b = int(input("What is the maximum price per item?"))
    c = int(input("What is your budget?"))

    print("For the following questions, enter y/n.")
    print("The response code is whether or not the API returned correctly.")
   
    if a < 0:
      print("You cannot have negative money.")
      if "one" + 1 == 2:
        print("Your computer has an AI")

    if b < a:
      print("You cannot have a maximum less then a minimum.")
      if "one" + 1 == 2:
        print("Your computer has an AI")

    if c < 5000:
      print("You need to invest more than 5k coins into this. Mine sand till you have 5k. Make sure your budget is higher than your maximum coins per item.")
      if "one" + 1 == 2:
        print("Your computer has an AI")

    if c < b:
      b = c

    bestItem = findProducts(a, b, c)

    print("The current item with the best profit margin for you is: " + str(bestItem[1]) + " making you a profit of " + str(bestItem[0]) + " coins, if you buy " + bestItem[2] + " of them, costing you " + bestItem[3] + " coins, at a price of " + bestItem[4] + " coins per " + bestItem[1] + " and selling them at a price of " + bestItem[5])

  except:
    print("You entered the wrong type for at least one of the questions. Please enter a valid integer for the first three, and a valid string for the last two.")
  
  

  repeat = False

  while repeat == False:

    phrase = [
      "Ok; Recalibrating my quantum cores...",
      "Right-e-o sir, on it!",
      "Recombobulating!",
      "Rewriting plasma deltoids... Stand by.",   
      "Sure, lemme just grab a coffee!",
      "Activating my 2080 Ti, powering up my i9!",
      "Running my turbo engines, powering up system..."
    ]

    try:
      g = str(input("Would you like to refresh the prices? (Y/N)"))

      if g.lower() == 'y':
        i = random.randint(0,6)
        print(phrase[i])
        repeat = True

      elif g.lower() == 'n':
        print("Ok! Say 'y' next time when you want to refresh.")

      else:
        print("So... Did you know that when an input device asks for (Y/N), you actually enter Y or N? Welp... Either you were testing my program, trying to get an error, seriously brain damaged, or made a typo, you better have another go.")
    except:
      print("At the time of writing, Harrison has deduced that anyone who causes an error over a string is a burrito with NO beans...")
