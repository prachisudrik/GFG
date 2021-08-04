
class Solution:
    def duplicates(self, arr, n):
        arr.sort()
        arr1= []
        for i,j in zip(range(0,n), range(0,n)):
            if(arr[i] == arr[j+1]):
                print('I',arr[i])
                print('J',arr[j])
                arr1.append(arr[i])
        return arr1



#{
#  Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends
