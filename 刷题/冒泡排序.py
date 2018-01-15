
def bubble(lst):
    for i in range(1,len(lst)-1):
        for j in range(1,len(lst)-i):
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
    print lst


def main():
    bubble([1,2,2,6,3,2,1,2])

if __name__ == '__main__':
    main()
