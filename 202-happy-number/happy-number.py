class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        while(n!=1):
            total=0
            while n:
                rem=n%10
                total+=rem**2
                n=n//10

            if total in seen:
                return False
            seen.add(total)
            n=total
        return True;            