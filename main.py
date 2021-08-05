# The goal of this program is to practice Python constructs

def getNumber():
  inputs = []
  symbols = 0
  while symbols >=0:
    symbols = int(input("Enter a digit: "))
    if symbols > -1:
      inputs.append(symbols)
    else:
      break
  print(sum(inputs))

def sumTwo(a,b):

   c = a + b

   return c



x = sumTwo(3,5)

print(x)
getNumber()

