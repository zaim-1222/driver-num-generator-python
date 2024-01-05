#task 1 and  task 2 

def personalDetailsRequest():  
  global firstName
  # makes variable (firstName) visible to whole system
  firstName = input("enter first name:") 
  firstNameValidCheck = firstName.isalpha() 
  #checks to see whether input is all letters
  while firstNameValidCheck == False: 
       firstName = input("only letters allowed. enter first name:") 
    #prompts user to reenter input if they use characters other than letters
       firstNameValidCheck = firstName.isalpha() 
  firstName = firstName.upper() 
  global middleName
  middleName = input("enter middle name. press enter if you do not have one:")  
  middleNameValidCheck = middleName.isalpha() 
  while middleNameValidCheck == False: 
      if middleName == "":
        break
      middleName = input("only letters allowed. enter middle name:")  
      middleNameValidCheck = middleName.isalpha() 
  middleName = middleName.upper()  
  global surname  
  surname = input("enter surname:") 
  surnameValidCheck = surname.isalpha() 
  while surnameValidCheck == False: 
    surname = input("only letters allowed. enter surname:") 
    surnameValidCheck = surname.isalpha() 
  surname = surname.upper()  
  global gender
  gender = input("enter gender:")  
  while gender != "male" and gender != "female":
    gender = input("enter male or female:")
  global birthYear  
  birthYear = input("enter birth year:")
  birthYearValidCheck = birthYear.isdigit()
  while birthYearValidCheck == False or len(birthYear)!= 4:
    birthYear = input("use 4 numbers. enter birth year:")
    birthYearValidCheck = birthYear.isdigit()
  global birthMonth 
  birthMonth = input("enter birth month:")
  birthMonthValidCheck = birthMonth.isdigit()
  while birthMonthValidCheck == False or len(birthMonth) != 2:
    birthMonth = input("use 2 numbers. enter birth month:")  
    birthMonthValidCheck = birthMonth.isdigit()
  while int(birthMonth) < 1 or int(birthMonth) > 12:
    birthMonth = input("only enter numbers from 1-12 in a two digit format, eg 01:")
  global birthDay  
  birthDay = input("enter birth day:")  
  birthDayValidCheck = birthDay.isdigit()
  while birthDayValidCheck == False or len(birthDay) != 2:
    birthDay = input("only use two numbers. enter birth day:")  
    birthDayValidCheck = birthDay.isdigit()
  while birthMonth == "02" and int(birthDay) > 28:
    birthDay = input("february birthdays only go up to 28 unless it is a leap year.enter birthday again:")
  while int(birthDay) < 1 or int(birthDay) > 30:
    birthMonth = input("only enter numbers from 1-30 in a two digit format, eg 01:")  
  return firstName, middleName, surname, gender, birthYear, birthMonth, birthDay  
inputDetails = personalDetailsRequest()  
print(inputDetails) 
#task 3 starts
def nameChars(firstName, middleName, surname):
  global first5Chars
  first5Chars = surname[:5]
  while len(first5Chars) != 5:
    surname = surname + "9"
    first5Chars = surname[:5]
  global chars12And13  
  if len(middleName) == 0:
    chars12And13 = firstName[0] + "9"
  else:  
   chars12And13 = firstName[0] + str(middleName[0])
  return first5Chars, chars12And13
chars1to5 = nameChars(firstName, middleName, surname)
print(first5Chars, chars12And13)
def dateChars(birthYear, birthMonth, birthDay):
  global char6
  char6 = birthYear[2]
  global chars7And8 
  if gender == "female":
    if birthMonth[0] == "0":
     birthMonth = "5" + birthMonth[1]
    elif birthMonth[0] == "1":
      birthMonth = "6" + birthMonth[1]
  chars7And8 = birthMonth
  global chars9And10
  chars9And10 = birthDay
  global char11
  char11 = birthYear[3]
birthDateChars = dateChars(birthYear, birthMonth, birthDay)
print(char6, chars7And8, chars9And10, char11)
def randomChars():
  global char14
  char14 = 9
  import random
  alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
  #creates array which has entries that can randomly be selected
  global chars15And16
  chars15And16 = random.choice(alphabet) + random.choice(alphabet)
randomCharacters = randomChars()
print(char14, chars15And16)
#task 5 ends
#task 6 starts
def finalDriverNum(first5Chars, char6, chars7And8, chars9And10, char11, chars12And13, char14, chars15And16):
  global driverNum 
  driverNum = str(first5Chars) + str(char6) + str(chars7And8) + str(chars9And10) + str(char11) + str(chars12And13) + str(char14) + str(chars15And16)
  return driverNum 
finalNum = finalDriverNum(first5Chars, char6, chars7And8, chars9And10, char11, chars12And13, char14, chars15And16)  
print("Your driver number is",driverNum)
#task 6 ends
