def count_occurences(nums, target):
    cnt = 0
    # only have to use range(len()) if it were
    # a list of strings 
    for num in nums:
        if nums[num] == target:
            cnt += 1
    return cnt

def remove_duplicates(nums):
    for i in range(len(nums)-1, 0, -1):
        if nums[i] == nums[i-1]:
            nums.remove(nums[i])
    return nums

def move_zeros(nums):
    for i in range(len(nums) - 1, 0, -1):
        if nums[i] == 0:
            nums.remove(nums[i])
            nums.append(0)

def reverse_list(nums):
    reverse = []
    for i in range(len(nums)-1, -1, -1):
        reverse.append(nums[i])
    return reverse

def find_max_product(nums):
    max_prod = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if(nums[i] != nums[j]):
                prod = nums[i] * nums[j]
                if (prod > max_prod):
                    max_prod = prod
    return max_prod

def find_max_element(nums):
    max = 0
    for num in range(len(nums)):    
        if(nums[num] > max):
            max = nums[num]
    return max


def main():
    nums = [1, 2, 0, 3 ,3, 0, 4, 5, 0, 5]
    #move_zeros(nums)
    #result = remove_duplicates(nums)
    print(reverse_list(nums))


if __name__ == '__main__':
    main()