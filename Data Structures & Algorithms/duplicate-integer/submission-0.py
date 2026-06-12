class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mp={}
        for num in nums:
            if num in mp:
                mp[num]+=1
            else:
                mp[num]=1

        if any(value>1 for value in mp.values()):
            return True
        else:
            return False             
        