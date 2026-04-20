class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_1 = 0
        num_2 = len(numbers)-1

        while num_1 < num_2:
            total = numbers[num_1]+numbers[num_2]
         
            if total < target:
                num_1+=1
            elif total > target:
                num_2-=1
            else: 
                break
        
        return [num_1+1,num_2+1]