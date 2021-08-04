class Solution(object):
    def getsum(self, arr,n):
        sum = 0
        for i in range(n):
            sum = sum + arr[i]
        return sum



def main():
    T = int(input())
    if T>0:
        a = [int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.getsum(a,T))
        
if __name__ == "__main__":
    main()
