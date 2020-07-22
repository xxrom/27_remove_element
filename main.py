# time - O(N)
# memory - O(1) (nums - external)
from typing import List

class Solution:
  def removeElement(self, nums: List[int], val: int) -> int:
    prevWrongIndex = 0
    index = 0

    while (index < len(nums)):
      print(index)

      if nums[index] != val:
        nums[prevWrongIndex] = nums[index]
        prevWrongIndex += 1

      index += 1

    return prevWrongIndex

my = Solution()
arr = [0,1,2,2,3,0,4,2]
arr = [2]
n = 3

# correctAns = [0,1,3,0,4]
correctAns = [0,2,2,3,0,4,2]
correctAns = [2]

ans = my.removeElement(arr, n)

fullAns = True
for i in range(ans):
  try:
    if arr[i] != correctAns[i]:
      fullAns = False
    print(arr[i], arr[i] == correctAns[i])
  except:
    print('error')

print("ans", fullAns)

# Runtime: 32 ms, faster than 77.82% of Python3 online submissions for Remove Element.
# Memory Usage: 13.6 MB, less than 94.75% of Python3 online submissions for Remove Element.