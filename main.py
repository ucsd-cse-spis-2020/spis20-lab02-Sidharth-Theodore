#1: sum of two integers
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
def convertWageMtoW(mWage,can):
  
  if(can == True):
    wageGap = 17.6
  else:
    wageGap = 0.182

  ratio = 1-wageGap

  return mWage*ratio

#5: Word Guessing game
def hangman(word):
  answerKey = word
  guessKey = ""
  for i in range(len(word)):
    guessKey += "_ "
#  print("answerKey = " + answerKey)
  print("guessKey = " + guessKey)
  while True:
    guessChar = input("Guess a character: ")
    if guessChar in answerKey:
      guessKey[answerKey.find(guessChar)] = guessChar
      print

#a = getNumber()
#print("Number: ",a)

#x = sumDigits(345)
#print("sum: ",x)

#print(convertWageMtoW(100))
print(hangman("monkey"))