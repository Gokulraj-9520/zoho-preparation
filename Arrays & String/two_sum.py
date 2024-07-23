#General
class Solution:
    def twoSum(self, nums,target):
        for i in range(0, len(nums)-1):
            for j in range( i+1, len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
obj=Solution()
nums=[2,7,11,15]
target=9
print(obj.twoSum(nums, target))
print("This method takes 0(N2) time complexity")


#Hashing
class Solution:
    def twoSum(self, nums, target):
        map={}
        for i in range(len(nums)):
            if (target-nums[i]) in map:
                return [map[target-nums[i]],i]
            else:
                map[nums[i]]=i
obj=Solution()
nums=[2,7,11,15]
target=9
print(obj.twoSum(nums, target))



#Two Pointers
class Solution:
    def twoSum(self, nums,target):
        numsWithIndices=[[nums[index],index] for index in range(len(nums))]
        numsWithIndices.sort()
        start=0
        end=len(nums)-1
        while start<end:
            if numsWithIndices[start][0]+numsWithIndices[end][0]==target:
                return numsWithIndices[start][1],numsWithIndices[end][1]
            elif numsWithIndices[start][0]+numsWithIndices[end][0] <=target:
                start +=1
            else:
                end-=1
obj=Solution()
nums=[2,7,11,15]
target=13
print(obj.twoSum(nums,target))