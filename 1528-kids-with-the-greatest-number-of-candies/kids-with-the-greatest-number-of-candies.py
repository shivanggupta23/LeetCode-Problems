class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_ele=max(candies)
        list=[False]*len(candies)
        for i in range(len(candies)):

            sum=candies[i]+extraCandies
            if sum>=max_ele:
                list[i]=True


        return list        
