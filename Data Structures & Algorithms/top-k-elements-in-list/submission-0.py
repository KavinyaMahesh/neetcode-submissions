class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp={}
        for num in nums:
            if num not in mp:
                mp[num]=1
            mp[num]+=1

            arr=[]
        for num, cnt in mp.items():
            arr.append([cnt,num])
        arr.sort()

        res=[]
        while len(res)<k:
            res.append(arr.pop()[1])
        return res        


        