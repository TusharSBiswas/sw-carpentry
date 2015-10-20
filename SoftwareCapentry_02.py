
# coding: utf-8

# In[21]:

# Here we are going to plan the program

# Open the zodiac descriptions
ZodiacText = open('zodiacDescriptions.txt','r')
#for thing in ZodiacText:
 #   print(thing)


# Read the file. We are going to make a list with each line of the file
# as a list item.
ZodiacList = []
for animal in ZodiacText:
    if animal != '\n':
        ZodiacList.append(animal)
    
print(ZodiacList)

# Ask the user for input
# We're just going to assign a variable for moment. Come back later.
try:
    birthYear = int(input("What year were you born? "))

    
except ValueError:
    print("You did not provide a year in the form of an integer.")
    
    
    


#birthYear = int(birthYear)
#birthYear = 1985
# Do some fancy figuring stuff out (little bit of math)
#John lied to us and gave us the wrong list
# To fix this we need to offset birthYear by 4
zodiacIndex = (birthYear-4) % 12
# print(zodiacIndex)

# Tell user the result
print("Your Chinese Zodiac Animal is a ", ZodiacList[zodiacIndex])
# Repeat
print (ZodiacList[1])
# Close the file
ZodiacText.close()


# In[27]:

# Here we are going to plan the program

# Open the zodiac descriptions
ZodiacText = open('zodiacDescriptions.txt','r')
#for thing in ZodiacText:
 #   print(thing)


# Read the file. We are going to make a list with each line of the file
# as a list item.
ZodiacList = []
for animal in ZodiacText:
    if animal != '\n':
        ZodiacList.append(animal)
    
print(ZodiacList)

# Ask the user for input
# We're just going to assign a variable for moment. Come back later.
try:
    birthYear = int(input("What year were you born? "))
    zodiacIndex = (birthYear-4) % 12
    print("Your Chinese Zodiac Animal is a ", ZodiacList[zodiacIndex])

except ValueError:
    print("You did not provide a year in the form of an integer.")
    
    
    


#birthYear = int(birthYear)
#birthYear = 1985
# Do some fancy figuring stuff out (little bit of math)
#John lied to us and gave us the wrong list
# To fix this we need to offset birthYear by 4

# print(zodiacIndex)

# Tell user the result
# Repeat
# print (ZodiacList[1])
# Close the file
ZodiacText.close()


# In[28]:

# You should write description here

# Open the zodiac descriptions
ZodiacText = open('zodiacDescriptions.txt','r')
#for thing in ZodiacText:
 #   print(thing)


# Read the file. We are going to make a list with each line of the file
# as a list item.
ZodiacList = []
for animal in ZodiacText:
    if animal != '\n':
        ZodiacList.append(animal)

# Close the file as soon as we are done with it
# 
ZodiacText.close()    
print(ZodiacList)

# Ask the user for input
# We're just going to assign a variable for moment. Come back later.
try:
    birthYear = int(input("What year were you born? "))
    # Do some fancy figuring stuff out (little bit of math)
    # John lied to us and gave us the wrong list
    # To fix this we need to offset birthYear by 4
    zodiacIndex = (birthYear-4) % 12
    # Tell user the result
    print("Your Chinese Zodiac Animal is a ", ZodiacList[zodiacIndex])

except ValueError:
    print("You did not provide a year in the form of an integer.")
    
    
    
# Repeat
zodiacList = ZodiacSetup()

birthYear = 0
while type(birthYear) is int:
    birthYear = zodiacCalculation()


# In[39]:

# You should write description here
# ZodiacSetup will do all the opening, loading, and closing of files/data
#It will return ZodiacList
def ZodiacSetup():
    # Open the zodiac descriptions
    ZodiacText = open('zodiacDescriptions.txt','r')
    #for thing in ZodiacText:
    #   print(thing)

    # Read the file. We are going to make a list with each line of the file
    # as a list item.
    ZodiacListTemp = []
    for animal in ZodiacText:
        if animal != '\n':
            ZodiacListTemp.append(animal)

    # Close the file as soon as we are done with it
    # Although in this case the end would be ok too
    ZodiacText.close() 
    return ZodiacListTemp

#ZodiacCalculation will collect a birth year and determine the Chinese 
#zodiac animal and then display it. With error trapping.
#It will return the birthyear
def ZodiacCalculation():
    # Ask the user for input
    # We're just going to assign a variable for moment. Come back later.
   
    try:
        birthYear = int(input("What year were you born? "))
        # Do some fancy figuring stuff out (little bit of math)
        # John lied to us and gave us the wrong list
        # To fix this we need to offset birthYear by 4
        zodiacIndex = (birthYear-4) % 12
        # Tell user the result
        print("Your Chinese Zodiac Animal is a ", ZodiacList[zodiacIndex])
    
        return birthYear
    
    except ValueError:
        print("You did not provide a year in the form of an integer.")
    
#     return birthYear
    
    
# Repeat
ZodiacList = ZodiacSetup()

birthYear = 0
while type(birthYear) is int:
    birthYear = ZodiacCalculation()


# In[42]:

# You should write description here
# ZodiacSetup will do all the opening, loading, and closing of files/data
#It will return ZodiacList
def ZodiacSetup():
    # Open the zodiac descriptions
    ZodiacText = open('zodiacDescriptions.txt','r')
    #for thing in ZodiacText:
    #   print(thing)

    # Read the file. We are going to make a list with each line of the file
    # as a list item.
    ZodiacListTemp = []
    for animal in ZodiacText:
        if animal != '\n':
            ZodiacListTemp.append(animal)

    # Close the file as soon as we are done with it
    # Although in this case the end would be ok too
    ZodiacText.close() 
    return ZodiacListTemp

#ZodiacCalculation will collect a birth year and determine the Chinese 
#zodiac animal and then display it. With error trapping.
#It will return the birthyear
def ZodiacCalculation():
    # Ask the user for input
    # We're just going to assign a variable for moment. Come back later.
    birthYear = input("What year were you born? ")
    try:
        birthYear = int(birthYear)
        # Do some fancy figuring stuff out (little bit of math)
        # John lied to us and gave us the wrong list
        # To fix this we need to offset birthYear by 4
        zodiacIndex = (birthYear-4) % 12
        # Tell user the result
        print("Your Chinese Zodiac Animal is a ", ZodiacList[zodiacIndex])
    
    
    except ValueError:
        print("You did not provide a year in the form of an integer.")
    
    return birthYear
   
#     return birthYear
    
    
# Repeat
ZodiacList = ZodiacSetup()

birthYear = 0
while type(birthYear) is int:
    birthYear = ZodiacCalculation()


# In[ ]:



