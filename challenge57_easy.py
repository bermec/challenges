''' Input: A sequence of integers either +ve or -ve

Output : a part of the sequence in the list with the maximum sum. 
'''
nums = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]
temp_total = 0
ex = 0
why = 0
largest_sequence = 0
for x in range(0, len(nums)):
    for y in range(x + 2, len(nums)):
        temp_total = sum(nums[x:y])
        if temp_total > largest_sequence:
            largest_sequence = temp_total
            ex = x
            why = y

print(largest_sequence, ex, why, nums[ex:why])



