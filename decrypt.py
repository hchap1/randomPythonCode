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

print(decryptMessage(2,'''BlyAei|08Td|/|/|/
alyA__NA8PtyMn1|/
arsnBa_op78GaeNANANASciWlfF|08Aa|uyM|NNW|
ilRb .1|JcsnHrio|NNW|
mlaLzyUKON8Ei|uyN|ARE|
arsnEeMRID8Rb|ae|NNW|
rc|oh9NAIz|al|16
aaBlaP||
a acmeAei UCRAN|NNW|
akTlyUKONUKONil|mla1|
odNANANAMre|__|/|
at|e|1NAHrio|enSu||
rc|/|/|/
ah|il .1|
dmRb .UKON8Wl|uyM|0
ako|arsnUKON8Aei|iz|NNW|
rnRb .MRID8Hrio|v|ARE|
uyjmsUKON8GaeJs||/
zyBls1|9Th|el .98Smdsob|mla(NETI)UKON8Jc|il|NNW|NNW
'''))

