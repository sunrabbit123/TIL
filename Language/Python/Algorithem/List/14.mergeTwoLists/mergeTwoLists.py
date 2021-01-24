import typing

input1 = [[1,2,4], [1, 3, 4]]
output1 = [1,1,2,3,4,4]

def mergeTwoLists(l1, l2, i = 0, j = 0):
    try:
        if (not l1[i:]) or (l2 and l1[i] > l2[j]):
            l1[i], l2[j] = l2[j], l1[i]
        if l1[i:]:
            l1.append(mergeTwoLists(l1,l2,i,j))
    except IndexError:
        return l1
    return l1
    
if __name__ == "__main__":
    mergeTwoLists(input1[0], input1[1])