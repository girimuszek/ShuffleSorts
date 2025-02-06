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
    global listA
    global listB
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

        
# If b is < a, but bigger than last output, plug b OR if output is empty (Rule 2 and 3)

def rule2And3():

    if (len(listA) != 0) and (len(listB) != 0):
        
        # Rule 3
        if ((listA[0] > listB[0]) and (len(listC) == 0)):
            
            # insert the leftmost value of listB to the very end of listC
            listC.insert(len(listC), listB[0])
            # Remove the leftmost value of ListB
            listB.pop(0)

     
            
            rule4and5()
        
        #Rule 2    
        elif ((listA[0] > listB[0]) and (listB[0] > listC[-1])):
            # insert the leftmost value of listB to the very end of listC
            listC.insert(len(listC), listB[0])
            # Remove the leftmost value of ListB
            listB.pop(0)

        
            
            rule4and5()
        else:    
        

            rule4and5()
    else:
        rule6()            


#--------------------------------------------------------------------------------------------------#
        

def rule4and5():

    # if a and b still exist. 
    if (len(listA) != 0) and (len(listB) != 0):
        
        # (rule 4) if a < b 
        if (listA[0] < listB[0]):
            listC.insert(len(listC), listA[0])
            listA.pop(0)
            
            rule2And3()
        # (rule 5) b is smaller than last entry, pop a to end 
        elif (listB[0] < listC[-1]):
            listC.insert(len(listC), listA[0])
            listA.pop(0)
            
           
            
            rule2And3()
        else: 
            rule2And3()
    else: 
        rule6()


#--------------------------------------------------------------------------------------------------#

                
# Inserts to the length of listC (the end of the list), the leftmost value of listA or listB (always [0]).
# Afterwards, removes the leftmost value of listA and repeats the process until there's nothing in either listA or listB.
def rule6():
    
    
    for i in range(len(listA)):
            
            listC.insert(len(listC), listA[0])
            
            listA.pop(0)
  
    for i in range(len(listB)):
            
        listC.insert(len(listC), listB[0])
            
        listB.pop(0)

    
    # Calls the driver to do another iteration
    driver()    


#--------------------------------------------------------------------------------------------------#

def driver(theInput = []):
   
    global copy
    global copy2
    global inputStr
    global original 
    global inputList 

    good = 0
    
    
    # First iteration, other part of driver is therefore unnecessary. 
    
    if iterationCount == 0:
        
        inputList = theInput
 

        splitter()
        
    else:    
        # Copies are necessary, because deleting old lists means deleting parts of the list history, 
        # and future inputList
        copy = listC.copy()
        copy2 = listC.copy()
        imageHistory.append(copy)
        inputList.clear()
        
        # Writes down elements from copy2 to the inputList. 
        # Instead of EX: inputList = [[1,2,3]], it does: inputList[1,2,3]
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
            
            
            print(listC)
            
        
        # List is not in numerical order    
        else:
            
            listA.clear()
            listB.clear()
            listC.clear()
            
            splitter()

#--------------------------------------------------------------------------------------------------#

#Initiates the sorting algorithm
driver([1,8,2,3,5,4,7,9,6])

#--------------------------------------------------------------------------------------------------#


# def PRE_graph(n):
#     '''input rank n and outputs PRE_graph of S_n'''
    

#     S = SymmetricGroup(n)
#     perms = [list(Permutation(s)) for s in S]
    
#     edges = []
#     vertices = []

#     for p in perms:
#         vertices.append(tuple(p))
#     for p in perms:
#         new_p = inputList(p)
#         if p!=new_p:
#             edges.extend([(tuple(p),tuple(new_p))])

#     G = Graph(to_graph(vertices,edges))
#     return G
    

# def to_graph(v, e):
#     """ turn the input v,e (premade vertices and edges) into a graph Graph(v,e) """
#     d = {}
    
#     for i in v:
#         d[i] = {}

#     g = DiGraph(d)

#     g.add_edges(e)
    
#     return g

# def c(L, remove_labels=False):
#     """
#     Quick way to visualize a digraph

#     Input: digraph
#     Output: image

#     """
#     if not isinstance(L, list):
#         L = [L]

#     for x in L:
#         try:
#             x.set_latex_options(
#                 format='dot2tex',
#                 prog='dot',
#                 edge_labels=True,
#                 )
#         except AttributeError:
#             pass


#     return view(L, tightpage=True)