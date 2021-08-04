class Solution:
    def longest(self, names, n):
    	fixed_len = 0
    	len1 = 0
    	for i in range(n):
    	    len1 = len(names[i])
    	    if(len1 > fixed_len):
    	        op = names[i]
    	    fixed_len = len1
    	return op

def main():
    T = int(input())
    if T>0:
        names=[]
        for i in range(T):
            names.append(input())
        obj = Solution()
        print(obj.longest(names,T))

if __name__ == "__main__":
    main()
