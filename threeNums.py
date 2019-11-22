class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        n=len(nums)
        res=[]
        if(not nums or n<3):
            return []
        nums.sort()
        res=[]
        for i in range(n):
            if(nums[i]>0):
                return res
            if(i>0 and nums[i]==nums[i-1]):
                continue
            L=i+1
            R=n-1
            while(L<R):
                if(nums[i]+nums[L]+nums[R]==0):
                    res.append([nums[i],nums[L],nums[R]])
                    while(L<R and nums[L]==nums[L+1]):
                        L=L+1
                    while(L<R and nums[R]==nums[R-1]):
                        R=R-1
                    L=L+1
                    R=R-1
                elif(nums[i]+nums[L]+nums[R]>0):
                    R=R-1
                else:
                    L=L+1
        return res



def quickSort(list):
    if len(list) <= 1:
        return list
    high = []
    low = []
    pivot = list.pop()
    for x in list:
        if x >= pivot:
            high.append(x)
        else:
            low.append(x)
    return quickSort(low) + [pivot] + quickSort(high)


def threeSum(nums):
    length = len(nums)
    if not nums or length < 3:
        return []
    numlist = []
    nums = quickSort(nums)
    for first in range(length):
        if nums[first] > 0:
            return numlist
        if first > 0 and nums[first] == nums[first - 1]:
            continue
        R = length - 1
        L = (R - first) // 2 + first
        flag=0
        while first<R-1 and L<R:
            if L<=first:
                while(L<R and nums[L]==nums[L+1]):
                    L=L+1
                L=first+1
                break
            elif L>=R:
                L=first+1
                while(L<R and nums[L]==nums[L+1]):
                    L=L+1
                while(L<R and nums[R]==nums[R-1]):
                    R=R-1
                L=L+1
                R=R-1
                break
            elif nums[first]+nums[L]+nums[R]==0:
                numlist.append([nums[first],nums[L],nums[R]])
                while(L<R and nums[L]==nums[L+1]):
                    L=L+1
                while(L<R and nums[R]==nums[R-1]):
                    R=R-1
                L=L+1
                R=R-1
                break
            elif nums[first]+nums[L]+nums[R]>0:
                if flag==0:
                    L=first+1
                else:
                    L=L-1
                break
            elif  nums[first]+nums[L]+nums[R]<0:
                flag=1
                while L<R and nums[L]==nums[L+1]:
                    L+=1
                L+=1

        while L<R:
            if L<=first:
                L+=1
            if R<=L:
                R+=1
            if R>=length:
                break
            if(nums[first]+nums[L]+nums[R]==0):
                numlist.append([nums[first],nums[L],nums[R]])
                while(L<R and nums[L]==nums[L+1]):
                    L=L+1
                while(L<R and nums[R]==nums[R-1]):
                    R=R-1
                L=L+1
                R=R-1
            elif(nums[first]+nums[L]+nums[R]>0):
                R=R-1
            else:
                L=L+1
    return numlist

nums3=[-2,-3,0,0,-2,1]
print(threeSum(nums3))
