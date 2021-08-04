#User function Template for python3

def countOfElements( arr, total_num, x):
    count=0
    for i in range(total_num):
        if(arr[i]<=x):
            #print(arr[i])
            count = count + 1
            #print(count)
        else:
            exit
    return count

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())

        print(countOfElements(a, n, k))

        T -= 1


if __name__ == "__main__":
    main()
