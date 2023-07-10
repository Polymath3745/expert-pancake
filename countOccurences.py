def count_occurences(nums, target):
    cnt = 0
    # only have to use range(len()) if it were
    # a list of strings 
    for num in nums:
        if nums[num] == target:
            cnt += 1
    return cnt

def main():
    nums = [1,1,2,3,4,5]
    result = count_occurences(nums, 1)
    print(result)

if __name__ == '__main__':
    main()
