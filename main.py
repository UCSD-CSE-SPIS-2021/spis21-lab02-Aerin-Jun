# The goal of this program is to practice Python constructs

# Getting a number that user wants
def getNumber():
  inputs = ""
  symbols = 0
  
  # Asks for the digits for the number
  while True:
    symbols = input("Enter a digit: ")
    number = int(symbols)
    if number > -1:
      
      #Add the symbols to the inputs
      inputs += symbols
    else:
      break
  
  # Get the number that the user wants
  return(inputs)

# Original example code that added two values, a and b, together
def sumTwo(a,b):

   c = a + b

   return c

# Converts the results from the getNumber function into a string
getnum = getNumber()

# Allows the sumDigits function to add all the values in a string by recognizing only the numbers and turns the numbers into integers
def sumDigits(x):
    return sum(int(x) for x in x if x.isdigit())

# Prints the results compiled from the first function where it gathers the user's input and sums them all before printing the result
print(sumDigits(getnum))
   
# Finds Woman's wage based on the corresponding man's wage in the US and UK 
def convertWageMtoW(mWage):
  
  # Asks which country is the wage based on
  country = input("UK or US? (UK/US):")
  
  # Wage gap in the UK
  if country.upper() == "UK":
    wageGap = 0.1228
  
  # Wage gap in the UK
  elif country.upper() == "US":
    wageGap = 0.1765

  ratio = 1 - wageGap

  return mWage * ratio

print(convertWageMtoW(100))
print(convertWageMtoW(76.2))
print(convertWageMtoW(0))
