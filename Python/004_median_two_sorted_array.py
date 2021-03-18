class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        //merge two lists
        mer=nums1+nums2
        //sort merged list
        mer.sort()
        //check for even
        if len(mer)%2==0:
        return (mer[int(len(mer)//2)-1]+mer[int(len(mer)//2)])/2
        //check for odd
        else:
        return mer[int(len(mer)/2)]

        //merge two lists
        mer = nums1 + nums2
        mer.sort()
        if len(mer)%2 == 0:
            return (mer[int(len(mer) // 2)] - 1] + mer[int(len(mer) // 2)]) / 2
            else:
                return mer[int(len(mer) / 2)]