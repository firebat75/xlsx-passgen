# GLOBAL VARIABLES
NUM_PASSWORDS = 200  # How many password
PASSWORD_LENGTH = 10  # Length of generated password
CHARACTERS = (
    []
)  # List of available characters (upper and lower letters, 0-9, ['*', '+', ',', '-', '.', '/'])

from openpyxl import Workbook
import random

workbook = Workbook()
sheet = workbook.active

# create list of available chars
for i in range(42, 57):
    CHARACTERS.append(chr(i))
for i in range(65, 90):
    CHARACTERS.append(chr(i))
for i in range(97, 122):
    CHARACTERS.append(chr(i))

# generate random password from available chars
def passGen(passLen=PASSWORD_LENGTH):
    pswd = ""
    for i in range(passLen):
        pswd += CHARACTERS[random.randrange(len(CHARACTERS))]
    if pswd[0] == "=":
        pswd = CHARACTERS[random.randrange(15, len(CHARACTERS))] + pswd[1:]
    return pswd


# pass passwords into empty sheet
for i in range(1, NUM_PASSWORDS + 1):
    sheet[("A" + str(i))] = passGen()

# export workbook
workbook.save(filename="passwords.xlsx")
