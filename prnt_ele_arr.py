def ArrayElements(arr,T):
    for i in range(T):
        print(arr[i])


def main():
    T = int(input())
    if T > 0:
        arr = [int(x) for x in input().strip().split() ]
        ArrayElements(arr,T)

if __name__ == "__main__":
    main()
