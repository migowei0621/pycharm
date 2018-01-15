# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def isListSorted(lst):
    return sorted(lst) == lst or sorted(lst, reverse=True) == lst

def solution(A):
    # write your code in Python 2.7
    global indexA
    global indexB
    i = 0
    while(i < len(A)-1):
        if(A[i] > A[i+1]):
            indexA = i
            break
        else:
            indexA = -999999
        i += 1

    if (indexA == -999999):
        return True
    else:
        j = len(A)-1
        while(j > indexA):
            if(A[j] < A[indexA]):
                indexB = j
                break
            else:
                indexB = -999999
            j -= 1

        for k,num in enumerate(A):
            if num == A[indexA]:
                indexA = k
                break
        if(indexB != -999999):
            A[indexA],A[indexB]  = A[indexB],A[indexA]
            if isListSorted(A):
                return True
            else:
                return False



def main():
    A = [1,2,2,4,4,3]
    # A = [1,5,3,3,7]
    # A = [1,3,5,3,4]
    # A = [1,3,5]
    solution(A)


if __name__=='__main__':
    main()