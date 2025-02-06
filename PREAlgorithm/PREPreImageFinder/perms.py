from itertools import permutations

global inputList 
global preimages

# Insert input here.
inputList = [2,3,4,1]
preimages = []




#Finds ai 

def pFinder():
   
    ai1 = []
    l2 = []
    l3 = []

    for i in range(len(inputList) - 1):
     
        if (inputList[i] > inputList[i+1]):
            l = list(permutations(inputList[:i+1]))
            ai1 = inputList[i+1:]
            break
        
    

    #cycles through perms
    for perm in l:
        for j in range(len(perm) - 1):
            if (perm[-1] > ai1[0]):
                l2.append(perm)
                break
            

    l2Copy = l2[:]            
            
    for perm2 in l2:

        tDescs = 0
    
        #iterates through a specific perm, if it has more than 1 descent, it gets removed from the list of permutations
        for k in range(len(perm2) - 1):   
            if (tDescs <= 1): 
                
                if (perm2[k] > perm2[k+1]):
                    tDescs +=1
            else: 
                l2.remove(perm2)


  

    for perm3 in l2Copy :
        l3.append(perm3 + tuple(ai1))


    return l3

result = pFinder()
print(result)
print("Total preimages to inputList is: " + str(len(result) - 1) )