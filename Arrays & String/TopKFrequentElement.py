class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        frequency={}
        for num in nums:
            if num in frequency:
                frequency[num]+=1
            else:
                frequency[num]=1
        frequency_list=[(num,freq) for num, freq in frequency.items()]
        frequency_list.sort(key=lambda x: x[1], reverse = True)
        top_k=[num for num , freq in frequency_list[:k]]
        return top_k