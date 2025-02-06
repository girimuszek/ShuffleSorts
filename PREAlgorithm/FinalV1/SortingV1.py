# Prefix-Preserving Shuffle: PRE
# Kacper Zalewski | Github: https://github.com/girimuszek


global imageHistory
global inputStr
global inputList  



iterationCount = 0
imageHistory = []

inputStr = 0
inputList = [] 
listC = []
listB = []
listA = []


#--------------------------------------------------------------------------------------------------#   

# Splits the input into lists "listA" and "listB"
def split():
    
    global testSplitA
    global testSplitB
    global listA
    global listB
    global inputList
    global iterationCount
    # Start from the beginning of the list
    testSplitA = 0
    testSplitB = 1
    i = 0
     
    iterationCount += 1
    # Iterates over the input list. Checks first 2 elements from left to right
    for i in range(len(inputList)):
       
        # If the left element is smaller than the right, move the elements to the right by one each.
        if inputList[testSplitA] < inputList[testSplitB]:
            
            testSplitA += 1
            testSplitB += 1    

    # Create listA and listB. listA includes the left side until the first descent, listB contains all other elements
    listA = inputList[:testSplitB]
    listB = inputList[testSplitB:]

    
    rule2And3()    


#--------------------------------------------------------------------------------------------------#


def driver():

    global copy
    global copy2
    
    good = 0
    
    
    # First iteration, other part of driver is therefore unnecessary. 
    
    if iterationCount == 0:
        
        # First input 
        print("Insert your input in the format: 1 2 4 7 8 9   :")
        inputStr = input()
        for k in inputStr.split():
            inputList.append(int(k))
        
        split()
        
    else:    
        # Copies are necessary, because deleting old lists means deleting parts of the list history, 
        # and future inputList
        copy = listC.copy()
        copy2 = listC.copy()
        imageHistory.append(copy)
        inputList.clear()
        
        # Writes down elements from copy2 to the inputList. 
        # Instead of EX: inputLit = [[1,2,3]], it does: inputList[1,2,3]
        j = 0
        for j in range(len(copy2)):
            inputList.insert(len(inputList), copy2[0])
            copy2.pop(0)
    
        # Compares the elements and sees if they are in numerical order. 
        for i in range(len(listC) - 1):
            
            if listC[i] <= listC[i + 1]:
                good += 1
        
        # List is in numerical order
        if good == len(listC) - 1: 
            
            
            print("All Images: ")
            print("")
            # Enumerates the image history 
            print(list(enumerate(imageHistory)))
            print("")
            print("Final Image: ")
            print(listC)
            print("")
            print("Number of Iterations: ")
            print(iterationCount)
        
        # List is not in numerical order    
        else:
            
            listA.clear()
            listB.clear()
            listC.clear()
            
            split()


#--------------------------------------------------------------------------------------------------#

        
# If b is < a, but bigger than last output, plug b OR if output is empty (Rule 2 and 3)

def rule2And3():

    if (len(listA) != 0) and (len(listB) != 0):

        if ((listA[0] > listB[0]) and (len(listC) == 0)) or ((listA[0] > listB[0]) and (listB[0] > listC[-1])) :
            
            # insert the leftmost value of listB to the very end of listC
            listC.insert(len(listC), listB[0])
            # Remove the leftmost value of ListB
            listB.pop(0)
            rule4()
        else:
            rule4()
    else:
        rule5()            


#--------------------------------------------------------------------------------------------------#
        

def rule4():

    # if a and b still exist. 
    if (len(listA) != 0) and (len(listB) != 0):
        
        # if a < b OR b is smaller than last entry, pop a to end (rule 4)
        if (listA[0] < listB[0]) or (listB[0] < listC[-1]):
            listC.insert(len(listC), listA[0])
            listA.pop(0)
            
            rule2And3()

        else:
            rule2And3()
    
    else: 
        rule5()


#--------------------------------------------------------------------------------------------------#

                
# Inserts to the length of listC (the end of the list), the leftmost value of listA or listB (always [0]).
# Afterwards, removes the leftmost value of listA and repeats the process until there's nothing in either listA or listB.
def rule5():
    
    
    for i in range(len(listA)):
            
            
            listC.insert(len(listC), listA[0])
            
            listA.pop(0)
  
    for i in range(len(listB)):
            
        listC.insert(len(listC), listB[0])
            
        listB.pop(0)

    # Calls the driver to do another iteration
    driver()    


#--------------------------------------------------------------------------------------------------#


#Initiates the sorting algorithm

driver()
