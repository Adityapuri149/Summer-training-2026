"""age=20
if age>=18:
    print("eligible to vote")
    print("You are eligible to vote.")
    
age =10
if age<18:
    print(" eligible to trvel")
    
    
    
def climbStairs(n):
    if n <= 2:
        return n

    first = 1
    second = 2

    for i in range(3, n + 1):
        third = first + second
        first = second
        second = third

    return second


print(climbStairs(5))    """
"""

def climbStairs(n):
    if n <= 2:
        return n

    first = 1
    second = 2

    for i in range(3, n + 1):
        third = first + second
        first = second
        second = third

    return second


print(climbStairs(5))

age = 20

if age >= 18:
  print("You are an adult")
  print("You can vote")
  print("You have full legal rights")"""
  

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]
        # Return an empty list if no solution is found
        return []