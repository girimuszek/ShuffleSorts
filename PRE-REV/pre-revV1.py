# Prefix-Preserving Shuffle: PRE V2
# Kacper Zalewski | Github: https://github.com/girimuszek

# Rule 1 - At the moment at first descent, split the number into 2 lists. ListA and ListB
# Rule 2 - If b is < a, but bigger than last output, plug in leftmost b 
# Rule 3 - Plug in leftmost b if output is empty
# Rule 4 - a < b
# Rule 5 - Rule 4, OR if b is smaller than the output
# Rule 6 - If one of the lists in A or B are empty, insert all the outputs in the remaining list to the end of the output


global imageHistory 
global inputStr
global theInput
global inputList 
iterator = 0
inputStr = 0
sequenceNum = 0
iterationCount = 0
imageHistory = []

inputList = [] 
listC = []
listB = []
listA = []

#--------------------------------------------------------------------------------------------------#   

# Splits the input into lists "listA" and "listB" 
#aka Rule 1
def splitter():
    
    global testSplitA
    global testSplitB
    global listA # = first half
    global listB # second half
    global listC
    global iterationCount
    # Start from the beginning of the list
    testSplitA = 0
    testSplitB = 1

  
    i = 0
     
    iterationCount += 1
    # Iterates over the input list. Checks first 2 elements from left to right
    for i in range(len(inputList)-1):

        
       
        # If the left element is smaller than the right, move the elements to the right by one each.

        if inputList[testSplitA] < inputList[testSplitB]:
            
            
            testSplitA += 1
            testSplitB += 1    

    # Create listA and listB. listA includes the left side until the first descent, listB contains all other elements
    
    listA = inputList[:testSplitB]
    listB = inputList[testSplitB:]
   
    part1()    


#--------------------------------------------------------------------------------------------------#

        
# If b is < a, but bigger than last output, plug b OR if output is empty (Rule 2 and 3)

def part1():
    if (len(listA) != 0) and (len(listB) != 0):

        if ((listB[-1] < listA[0]) or (listB[-1] < listA[0] and len(listA)==0)):
            
            listC.insert(len(listC), listB[-1])
            
            listB.pop(-1)   
            part2()

        elif (len(listA) != 0) and (len(listB) != 0):
            if ((listA[0] < listB[-1]) or listB[-1] < listC[-1]):
                
                listC.insert(len(listC), listA[0])
                
                listA.pop(0)
                part2()
        
def part2():        
    if (len(listA) != 0) and (len(listB) != 0):
        if (((listB[-1] < listA[0]) and (listB[-1] > listC[-1])) or (listB[-1] < listA[0] and len(listA)==0)):

            listC.insert(len(listC), listB[-1])
            listB.pop(-1)   
            part2()

        elif (len(listA) != 0) and (len(listB) != 0):
            if ((listA[0] < listB[-1]) or listB[-1] < listC[-1]):

                listC.insert(len(listC), listA[0])
                listA.pop(0)
                part2()
    else:
        part3()
    
    
def part3():    
    if (len(listA) == 0): 
        for i in range(len(listB)):
            
            listC.insert(len(listC), listB[-1])
        
            listB.pop(-1)
    
    else:    
        for j in range(len(listA)):
            
            listC.insert(len(listC), listA[0])
        
            listA.pop(0)

    

  

    
#--------------------------------------------------------------------------------------------------#

def driver(tester):
   
    global copy
    global copy2
    global inputStr
    global original 
    global inputList 
    global iterator
    global activSplitter
    
    inputList = tester
    iterator = 0
    activSplitter = False
    while inputList != sorted(inputList):
        listC.clear()  
        splitter()
        print(listC)      
        inputList = listC.copy()    
    return listC
        
#--------------------------------------------------------------------------------------------------#

driver([6,5,4,3,2,1])
