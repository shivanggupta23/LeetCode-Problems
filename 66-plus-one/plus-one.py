class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=0
        for i in digits:
            num=num*10+i

        num=num+1
        List1=[]
        while(num!=0):
                rem=num%10
                num=num//10
                List1.insert(0,rem)

        # List1.reverse()        
        return List1        


    #     class Solution:
    # def plusOne(self, digits: List[int]) -> List[int]:
    #     for i in range(len(digits) - 1, -1, -1):
    #         if digits[i] < 9:
    #             digits[i] += 1
    #             return digits

    #         digits[i] = 0

    #     return [1] + digits