def add(ele1, ele2):
   elements = []                                      # Assigned an empty list to append matrix elements in
   for item in range(0, len(ele1)):
      elements.append(ele1[item] + ele2[item])        # Loopping through to add the elements of matrix
   return elements
ele1 = [[1,2], [3,4]]                                 # Elements to add
ele2 = [[4,5],[6,7]]
result = []                                           # Assigned an empty list to append the result of elements
for item in range(0, len(ele1)):
   result.append(add(ele1[item], ele2[item]))
print("Addition of matrix is:- ", result)             # Print's the output of matrix


def substract(ele1, ele2):
   elements = []                                      # Assigned an empty list to append matrix elements in
   for item in range(0, len(ele1)):
      elements.append(ele1[item] - ele2[item])        # Loopping through to substract the elements of matrix
   return elements
ele1 = [[1,2], [3,4]]                                 # Elements to substract 
ele2 = [[4,5],[6,7]]
result = []                                           # Assigned an empty list to append the result of elements
for item in range(0, len(ele1)):
   result.append(substract(ele1[item], ele2[item]))
print("Substraction of matrix is:- ", result)         # Print's the output of matrix