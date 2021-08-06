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
  return(inputs)

def sumTwo(a,b):

   c = a + b

   return c

getnum = getNumber()

def sumDigits(x):
    return sum(int(x) for x in x if x.isdigit())

print(sumDigits(getnum))
   

