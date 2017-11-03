''' A very basic challenge:

In this challenge, the

input is are : 3 numbers as arguments

output: the sum of the squares of the two larger numbers.

Your task is to write the indicated challenge.

'''


nums = input('Input three numbers in the form 1/2/3 :  ')

nums = sorted(nums.split('/'))
ans = (float(nums[1]) ** 2) + (float(nums[2]) ** 2)
print(ans)
