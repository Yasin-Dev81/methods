"""
- two-sum
    * توی لیست میگرده و اون دو عددی که جمعشون میشه تارگت ما رو برمیگردونه

"""

def tow_sum(nums, target):
    p1 = 0
    p2 = len(nums)-1
    while p1<p2:
        s = nums[p1]+nums[p2]
        if s==target:
            return [nums[p1], nums[p2]]
        elif s>target:
            p2 -= 1
        else:
            p1 += 1

print(tow_sum([2, 7, 11, 15], 18))
