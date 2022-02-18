#import pyperclip,
import math

def decryptMessage(key, message):

    numOfColumns = int(math.ceil(len(message) / float(key)))

    numOfRows = key

    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)

    plainText = [""] * numOfColumns

    column = 0

    row = 0

    for symbol in message:

        plainText[column] += symbol

        column += 1

        if column == numOfColumns or (column == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            column = 0
            row += 1

    return "".join(plainText)
