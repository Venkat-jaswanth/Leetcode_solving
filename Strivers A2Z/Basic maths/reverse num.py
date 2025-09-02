class Solution:
    def reverse(self, x: int) -> int:
        rev=0
        flg=True if x<0 else False
        x=abs(x)
        while x!=0:
            d=x%10
            rev=rev*10+d
            x=x//10
        if flg:
            rev=-rev
        if rev>((1<<31)-1) or rev<-(1<<31):
            return 0
        return rev