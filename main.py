# The goal of this program is to practice Python constructs

def getNumber():
  inputs = ""
  symbols = 0
  while True:
    symbols = input("Enter a digit: ")
    number = int(symbols)
    if number > -1:
      inputs += symbols
    else:
      break
  print(inputs)

def sumTwo(a,b):

   c = a + b

   return c

getNumber()

x = sumTwo(3,5)

print(x)


def sumDigits(x):

   # You will need to complete this function

   return sum


