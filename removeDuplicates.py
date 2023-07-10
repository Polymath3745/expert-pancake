
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


def main():
    nums = [1, 2, 0, 3 ,3, 0, 4, 5, 0, 5]
    #move_zeros(nums)
    #result = remove_duplicates(nums)
    print(reverse_list(nums))
    


if __name__ == '__main__':
    main()