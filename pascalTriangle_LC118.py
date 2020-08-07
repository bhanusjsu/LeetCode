# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


# In Pascal's triangle, each number is the sum of the two numbers directly above it.

# Example:

# Input: 5
# Output:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]
class Solution:
    def generate(self, numRows):
        pascalList = [[]]
        if(numRows==0):
            return []
        elif(numRows==1):
            pascalList = [[1]]
            return pascalList
        elif(numRows==2):
            pascalList = [[1],[1,1]]
            return pascalList
        elif(numRows>2):
            pascalList = [[1],[1,1]]
            for i in range(1,numRows-1):
                previousList = pascalList[i]
                newList = []
                newList.append(1)
                for j in range(0,len(previousList)-1):
                    listElemnt = previousList[j]+previousList[j+1]
                    newList.append(listElemnt)
                newList.append(1)
                pascalList.append(newList)
            return pascalList

    
