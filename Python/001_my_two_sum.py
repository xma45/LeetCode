class Solution(object):    
    def twoSum(self, nums, target):
            # two point
            nums_index = [(v, index) for index, v in enumerate(nums)]
            nums_index.sort()
            begin, end = 0, len(nums) - 1
            while begin < end:
                curr = nums_index[begin][0] + nums_index[end][0]
                if curr == target:
                    return [nums_index[begin][1], nums_index[end][1]]
                elif curr < target:
                    begin += 1
                else:
                    end -= 1


    def twoSum(nums, target):
        number_index = [(v, index) for index, v in enumerate(nums)]
        number_index.sort()
        begin, end = 0, len(nums) - 1
        while begin < end:
            current_number = number_index[begin][0] + number_index[end][0]
            if current_number = target:
                return [number_index[begin][1], number_index[end][1]]
                elif current_number < target:
                    begin += 1
                    else:
                        end -= 1


if __name__ == '__main__':
    # begin
    s = Solution()
    print s.twoSum([3, 2, 4], 6)