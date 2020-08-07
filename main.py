#1: sum of two integers
import pandas as pd

def sumTwo(a,b):

   c = a + b

   return c

#2: gets a number based on user input
def getNumber():
    nums = [] #list of numbers that the user inputs
    cont = True #decides wether the loop continues

    while cont:
      digit = input("Please enter a digit  ")#user input of a number
      number = int(digit) #turning input into an int
      if number >= 0: #only adds to list if positive
          nums.append(number)
      else: #if not the loop stops
        cont = False
    
    finalNum = 0 #the initialization of the digit sum variable

    for a in range(len(nums)): #for each number in nums
      length = len(nums)-1
      powerIndex = length-a #set the power value to the inverse of its index in the list
      thisNum = nums[a] #get the value of the number from the list
      varNum = thisNum*(10**powerIndex) #set the new number in its unit form as a function of a power of ten
      finalNum+=varNum #add this to the final number
    return finalNum

#3: getting the sum of digits in a number
def sumDigits(num): 
  sum = 0
  while num != 0:
    #adds "ones" digit to sum
    sum += num % 10
    #chops off previous "ones" digit
    num = int(num/10)
  return sum
  


#4: Wage Converter
data = pd.read_csv('wagegap.csv')#reading the wage gap data
wageframe = pd.DataFrame(data[["LOCATION","VALUE"]])#create a dataframe based on the data we need 



def convertWageMtoW(mWage, location):
    newframe = wageframe.loc[wageframe['LOCATION']==location,"VALUE"] #creating a specific dataframe based on the country input
    values = [] #list that holds the values of the wagegap percentages
    for row in newframe:
        values.append(row)#adding each wagegap value from this country to the list

    wageGap = sum(values)/len(values) #finding he average wagegap value

    wageGap /= 100 #making that value a percentage

    ratio = 1-wageGap #subtracting the percentage from 1 to create a multipliable ratio
    wWage = mWage*ratio
    return "Womens' wage: " + str(wWage) + " Man's Wage: "+ str(mWage)+ " Country: "+ location
    #womens' salary as a ration of the mens salary in the specified country

new = convertWageMtoW(100,"CAN")
print(new)

#5: Word Guessing game
def hangman(word, lives):
  lives = lives
  answerKey = word
  guessKey = []
  for i in range(len(word)):
    guessKey += "_"
#  print("answerKey = " + answerKey)
  print(str(guessKey))
  while lives > 1:
    print("Lives: " + str(lives))
    guessChar = input("Guess a character: ")
    if guessChar in answerKey:
      findIndex = 0
      for i in range(len(word)):
        guessKey[answerKey.find(guessChar,findIndex)] = guessChar
        findIndex = answerKey.find(guessChar,findIndex) + 1
        print(str)
    else:
      lives -= 1
    print(guessKey)
    if "_" in guessKey:
      continue
    else:
      print("Congratulations, you win!")
      break

#a = getNumber()
#print("Number: ",a)

#x = sumDigits(345)
#print("sum: ",x)

#print(convertWageMtoW(100))
hangman("molasses", 8)