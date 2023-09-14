class Solution:
    def countLargestGroup(n: int) -> int:
        result={}

        for i in range(1, n+1, 1):
            sum = 0
            s=str(i)
            for i in s:
                sum += int(i)
            try:
                result[sum] += 1
            except:
                result[sum] = 1
        maximun = max(list(result.values()))
        count=0
        for i in result.values():
            if i == maximun:
                count+=1
        return(count)
            
    
    print(countLargestGroup(13))
    

